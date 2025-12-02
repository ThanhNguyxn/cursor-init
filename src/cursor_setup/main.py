"""
cursor-setup: A CLI tool for initializing .cursorrules files.

This module contains the main CLI logic using Typer and Rich.
Supports both local templates and dynamic remote registry.
Features smart caching and self-upgrade capabilities.

Version: 2.1.0
"""
import subprocess
import sys
from pathlib import Path
from typing import Optional

import requests
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.text import Text

from cursor_setup.templates import TEMPLATES

# Initialize Typer app and Rich console
app = typer.Typer(
    name="cursor-setup",
    help="🚀 Initialize your Cursor AI context in seconds.",
    add_completion=False,
)
console = Console()

# Constants
CURSORRULES_FILENAME = ".cursorrules"
REMOTE_REGISTRY_URL = "https://raw.githubusercontent.com/ThanhNguyxn/cursor-setup/main/rules.json"
REQUEST_TIMEOUT = 5  # seconds
CACHE_DIR = Path.home() / ".cursor-setup" / "cache"


def get_cache_path(name: str) -> Path:
    """
    Get the cache file path for a template.
    
    Args:
        name: Template name (e.g., 'python', 'react').
        
    Returns:
        Path to the cache file.
    """
    return CACHE_DIR / f"{name}.cursorrules"


def ensure_cache_dir() -> None:
    """Create cache directory if it doesn't exist."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


def load_from_cache(name: str) -> Optional[str]:
    """
    Load template content from cache.
    
    Args:
        name: Template name.
        
    Returns:
        Cached content if exists, None otherwise.
    """
    cache_path = get_cache_path(name)
    if cache_path.exists():
        try:
            return cache_path.read_text(encoding="utf-8")
        except OSError:
            return None
    return None


def save_to_cache(name: str, content: str) -> None:
    """
    Save template content to cache.
    
    Args:
        name: Template name.
        content: Template content to cache.
    """
    try:
        ensure_cache_dir()
        cache_path = get_cache_path(name)
        cache_path.write_text(content, encoding="utf-8")
    except OSError:
        # Silent fail - caching is optional
        pass


def get_registry() -> dict:
    """
    Fetch the template registry from remote source with offline fallback.
    
    Attempts to fetch the latest templates from the remote rules.json.
    If successful, merges with local templates (remote takes priority).
    If network fails (offline/timeout), returns local templates silently.
    
    Returns:
        Dictionary of all available templates (local + remote merged).
    """
    # Start with local templates as the base
    all_templates = TEMPLATES.copy()
    
    try:
        response = requests.get(REMOTE_REGISTRY_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        
        # Validate structure and merge remote templates
        if isinstance(data, dict) and "templates" in data:
            remote_templates = data["templates"]
            # Remote templates override local ones if keys conflict
            all_templates.update(remote_templates)
            
    except (requests.RequestException, ValueError, KeyError):
        # Silent fallback: network error, timeout, or invalid JSON
        # Just use local templates without any error message
        pass
    
    return all_templates


def download_from_url(url: str) -> str:
    """
    Download content from a URL.
    
    Args:
        url: The URL to download content from.
        
    Returns:
        The text content of the response.
        
    Raises:
        requests.RequestException: If download fails.
    """
    response = requests.get(url, timeout=10)  # Longer timeout for direct downloads
    response.raise_for_status()
    return response.text


def write_cursorrules(content: str, force: bool = False) -> Path:
    """
    Write content to .cursorrules file.
    
    Args:
        content: The content to write to the file.
        force: If True, overwrite without asking.
    
    Returns:
        The path to the created file.
        
    Raises:
        typer.Exit: If user cancels overwrite or write fails.
    """
    cursorrules_path = Path.cwd() / CURSORRULES_FILENAME
    
    # Check if .cursorrules already exists
    if cursorrules_path.exists() and not force:
        console.print(
            f"\n[yellow]⚠️  Warning:[/yellow] A [bold]{CURSORRULES_FILENAME}[/bold] "
            "file already exists in this directory.\n"
        )
        overwrite = typer.confirm("Do you want to overwrite it?", default=False)
        if not overwrite:
            console.print("\n[dim]Operation cancelled.[/dim]\n")
            raise typer.Exit(code=0)
    
    # Write the content
    try:
        cursorrules_path.write_text(content, encoding="utf-8")
    except OSError as e:
        console.print(f"\n[red]❌ Error writing file:[/red] {e}\n")
        raise typer.Exit(code=1)
    
    return cursorrules_path


@app.command()
def list() -> None:
    """List all available cursor rule templates."""
    # Fetch all templates (local + remote merged)
    all_templates = get_registry()
    
    table = Table(
        title="📚 Available Cursor Rule Templates",
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
    )

    table.add_column("Template", style="cyan", no_wrap=True)
    table.add_column("Name", style="green")
    table.add_column("Description", style="white")

    for key, template in sorted(all_templates.items()):
        table.add_row(key, template["name"], template["description"])

    console.print()
    console.print(table)
    console.print()
    console.print(
        "[dim]Usage: cursor-setup install <template>[/dim]",
        justify="center",
    )
    console.print(
        "[dim]Pro tip: cursor-setup install --url <link> for custom rules[/dim]",
        justify="center",
    )
    console.print()


@app.command()
def install(
    name: Optional[str] = typer.Argument(
        None,
        help="Template name to install (e.g., python, nextjs, flutter, laravel)",
    ),
    url: Optional[str] = typer.Option(
        None,
        "--url", "-u",
        help="Install directly from a raw URL (e.g., from GitHub)",
    ),
    force: bool = typer.Option(
        False,
        "--force", "-f",
        help="Overwrite existing .cursorrules without confirmation",
    ),
    no_cache: bool = typer.Option(
        False,
        "--no-cache",
        help="Force re-download and bypass cache",
    ),
) -> None:
    """
    Install a cursor rule template to the current directory.
    
    Examples:
        cursor-setup install python
        cursor-setup install --url https://raw.githubusercontent.com/.../rules.txt
        cursor-setup install python --no-cache
    """
    # Validate: either name or url must be provided, but not both
    if url and name:
        console.print(
            "\n[red]❌ Error:[/red] Please use either a template name OR --url, not both.\n"
        )
        raise typer.Exit(code=1)
    
    if not url and not name:
        console.print(
            "\n[red]❌ Error:[/red] Please provide a template name or use --url.\n"
        )
        console.print("Examples:", style="yellow")
        console.print("  cursor-setup install python", style="dim")
        console.print("  cursor-setup install --url https://example.com/rule.txt", style="dim")
        console.print()
        raise typer.Exit(code=1)
    
    # === URL Installation Mode ===
    if url:
        console.print(f"\n[cyan]🌐 Downloading from URL...[/cyan]\n")
        
        try:
            content = download_from_url(url)
        except requests.RequestException as e:
            console.print(f"\n[red]❌ Failed to download:[/red] {e}\n")
            console.print("[dim]Check the URL and your internet connection.[/dim]")
            raise typer.Exit(code=1)
        
        cursorrules_path = write_cursorrules(content, force)
        
        # Success message
        success_text = Text()
        success_text.append("✨ ", style="bold")
        success_text.append("Successfully installed cursor rules from URL!", style="green")
        
        console.print()
        console.print(Panel(success_text, border_style="green", padding=(0, 2)))
        console.print()
        console.print(f"[dim]Created:[/dim] [cyan]{cursorrules_path.absolute()}[/cyan]")
        console.print()
        return
    
    # === Template Name Installation Mode ===
    all_templates = get_registry()
    
    if name not in all_templates:
        console.print(
            f"\n[red]❌ Error:[/red] Template '[bold]{name}[/bold]' not found.\n"
        )
        console.print("Available templates:", style="yellow")
        for key in sorted(all_templates.keys()):
            console.print(f"  • {key}", style="dim")
        console.print()
        console.print("[dim]Tip: Use --url to install from any URL[/dim]")
        console.print()
        raise typer.Exit(code=1)

    template = all_templates[name]
    content: Optional[str] = None
    
    # Check if template has a URL (remote template) or content (local template)
    if "url" in template:
        # Try cache first (unless --no-cache is set)
        if not no_cache:
            cached_content = load_from_cache(name)
            if cached_content:
                console.print(f"\n[yellow]⚡ Loaded [bold]{template['name']}[/bold] from cache[/yellow]\n")
                content = cached_content
        
        # Cache miss or --no-cache: download from URL
        if content is None:
            console.print(f"\n[cyan]🌐 Fetching {template['name']} rules...[/cyan]\n")
            try:
                content = download_from_url(template["url"])
                # Save to cache for next time
                save_to_cache(name, content)
            except requests.RequestException as e:
                # Try fallback to cache even if --no-cache was set
                cached_content = load_from_cache(name)
                if cached_content:
                    console.print(f"[yellow]⚠️  Network error, using cached version[/yellow]\n")
                    content = cached_content
                else:
                    console.print(f"\n[red]❌ Failed to download template:[/red] {e}\n")
                    raise typer.Exit(code=1)
    else:
        # Local template: use embedded content
        content = template["content"]
    
    cursorrules_path = write_cursorrules(content, force)

    # Success message
    success_text = Text()
    success_text.append("✨ ", style="bold")
    success_text.append("Successfully initialized cursor rules for ", style="green")
    success_text.append(template["name"], style="bold green")
    success_text.append("!", style="green")

    console.print()
    console.print(Panel(success_text, border_style="green", padding=(0, 2)))
    console.print()
    console.print(f"[dim]Created:[/dim] [cyan]{cursorrules_path.absolute()}[/cyan]")
    console.print()


@app.command()
def show(
    name: str = typer.Argument(
        ...,
        help="Template name to preview (e.g., python, nextjs, flutter)",
    ),
) -> None:
    """Preview a cursor rule template without installing it."""
    all_templates = get_registry()
    
    if name not in all_templates:
        console.print(
            f"\n[red]❌ Error:[/red] Template '[bold]{name}[/bold]' not found.\n"
        )
        console.print("Available templates:", style="yellow")
        for key in sorted(all_templates.keys()):
            console.print(f"  • {key}", style="dim")
        console.print()
        raise typer.Exit(code=1)

    template = all_templates[name]
    
    # Check if template has a URL (remote) or content (local)
    if "url" in template:
        # Try cache first
        cached_content = load_from_cache(name)
        if cached_content:
            console.print(f"\n[yellow]⚡ Loaded from cache[/yellow]\n")
            content = cached_content
        else:
            console.print(f"\n[cyan]🌐 Fetching {template['name']} preview...[/cyan]\n")
            try:
                content = download_from_url(template["url"])
                save_to_cache(name, content)
            except requests.RequestException as e:
                console.print(f"\n[red]❌ Failed to fetch preview:[/red] {e}\n")
                raise typer.Exit(code=1)
    else:
        content = template["content"]

    console.print()
    console.print(
        Panel(
            content,
            title=f"📄 {template['name']} Template",
            border_style="cyan",
            padding=(1, 2),
        )
    )
    console.print()


@app.command()
def upgrade() -> None:
    """Upgrade cursor-setup to the latest version."""
    console.print()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        progress.add_task(description="[cyan]Checking for updates...[/cyan]", total=None)
        
        try:
            # Run pip install --upgrade
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--upgrade", "cursor-setup"],
                capture_output=True,
                text=True,
                timeout=60,
            )
            
            if result.returncode != 0:
                console.print(f"[red]❌ Upgrade failed:[/red]\n{result.stderr}")
                raise typer.Exit(code=1)
                
        except subprocess.TimeoutExpired:
            console.print("[red]❌ Upgrade timed out. Please try again.[/red]")
            raise typer.Exit(code=1)
        except FileNotFoundError:
            console.print("[red]❌ pip not found. Please ensure pip is installed.[/red]")
            raise typer.Exit(code=1)
    
    # Get new version
    try:
        from importlib.metadata import version
        new_version = version("cursor-setup")
    except Exception:
        new_version = "unknown"
    
    success_text = Text()
    success_text.append("✨ ", style="bold")
    success_text.append("Successfully upgraded to ", style="green")
    success_text.append(f"v{new_version}", style="bold green")
    success_text.append("!", style="green")
    
    console.print(Panel(success_text, border_style="green", padding=(0, 2)))
    console.print()


@app.command()
def cache(
    clear: bool = typer.Option(
        False,
        "--clear", "-c",
        help="Clear all cached templates",
    ),
) -> None:
    """Manage the template cache."""
    if clear:
        if CACHE_DIR.exists():
            import shutil
            try:
                shutil.rmtree(CACHE_DIR)
                console.print("\n[green]✨ Cache cleared successfully![/green]\n")
            except OSError as e:
                console.print(f"\n[red]❌ Failed to clear cache:[/red] {e}\n")
                raise typer.Exit(code=1)
        else:
            console.print("\n[dim]Cache is already empty.[/dim]\n")
        return
    
    # Show cache info
    console.print()
    if not CACHE_DIR.exists():
        console.print("[dim]No cache directory found.[/dim]")
        console.print(f"[dim]Cache location: {CACHE_DIR}[/dim]\n")
        return
    
    cached_files = list(CACHE_DIR.glob("*.cursorrules"))
    
    if not cached_files:
        console.print("[dim]Cache is empty.[/dim]")
        console.print(f"[dim]Cache location: {CACHE_DIR}[/dim]\n")
        return
    
    table = Table(
        title="📦 Cached Templates",
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
    )
    
    table.add_column("Template", style="cyan")
    table.add_column("Size", style="green")
    
    total_size = 0
    for cache_file in sorted(cached_files):
        size = cache_file.stat().st_size
        total_size += size
        size_str = f"{size / 1024:.1f} KB" if size >= 1024 else f"{size} B"
        table.add_row(cache_file.stem, size_str)
    
    console.print(table)
    total_str = f"{total_size / 1024:.1f} KB" if total_size >= 1024 else f"{total_size} B"
    console.print(f"\n[dim]Total size: {total_str}[/dim]")
    console.print(f"[dim]Location: {CACHE_DIR}[/dim]")
    console.print("\n[dim]Use --clear to remove all cached templates[/dim]\n")


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
