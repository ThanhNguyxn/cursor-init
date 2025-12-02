# Contributing to cursor-setup

First off, thanks for taking the time to contribute! 🎉

This guide will help you add new templates to cursor-setup. It's designed to be simple — even if you've never contributed to open source before.

---

## Table of Contents

- [The Easiest Way to Contribute](#the-easiest-way-to-contribute)
- [How to Add a New Template](#how-to-add-a-new-template)
- [Template Guidelines](#template-guidelines)
- [Other Ways to Contribute](#other-ways-to-contribute)
- [Development Setup](#development-setup)
- [Code Style](#code-style)

---

## The Easiest Way to Contribute

**Add a template to `rules.json`** — our community-driven registry!

This file contains URLs to cursor rules from around the internet. When users run `cursor-setup list`, they see templates from this file.

You don't need to write any Python code. Just add a URL and description!

---

## How to Add a New Template

### Step 1: Fork the Repository

Click the **Fork** button at the top of [this page](https://github.com/ThanhNguyxn/cursor-setup).

### Step 2: Edit `rules.json`

Open the `rules.json` file and add your template to the `"templates"` section:

```json
{
  "templates": {
    "existing-template": { ... },
    
    "your-template-name": {
      "name": "Display Name",
      "description": "Short description (under 60 characters)",
      "url": "https://raw.githubusercontent.com/user/repo/main/.cursorrules",
      "author": "your-github-username",
      "tags": ["tag1", "tag2", "tag3"]
    }
  }
}
```

### Step 3: Follow These Rules

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Human-readable name (e.g., "Django", "Ruby on Rails") |
| `description` | ✅ | Brief description, under 60 characters |
| `url` | ✅ | **Raw** URL to the cursorrules file (must start with `https://`) |
| `author` | ✅ | GitHub username or source attribution |
| `tags` | ✅ | Array of relevant tags (language, framework, etc.) |

### Step 4: Test Your URL

Make sure your URL works! Open it in a browser — it should show raw text, not a GitHub page.

✅ **Good URL:**
```
https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/laravel-tall-stack-best-practices/.cursorrules
```

❌ **Bad URL:**
```
https://github.com/PatrickJS/awesome-cursorrules/blob/main/rules/laravel-tall-stack-best-practices/.cursorrules
```

### Step 5: Submit a Pull Request

1. Commit your changes with a clear message:
   ```
   feat: add Django template
   ```

2. Push to your fork

3. Open a Pull Request to the `main` branch

4. Fill in the PR template describing your addition

---

## Template Guidelines

### ✅ DO:

- **Use reliable sources** — Link to well-maintained repositories
- **Include comprehensive rules** — Templates should cover coding style, best practices, and common patterns
- **Keep descriptions concise** — Under 60 characters works best in the CLI table
- **Use lowercase keys** — Template keys should be `kebab-case` (e.g., `ruby-rails`, not `Ruby_Rails`)
- **Test the URL** — Make sure it returns raw text content

### ❌ DON'T:

- Link to temporary or personal gists that might disappear
- Add duplicate templates (check existing ones first)
- Include placeholder or incomplete rules
- Use URLs that require authentication

---

## Other Ways to Contribute

### 🐛 Report Bugs

Found a bug? [Open an issue](https://github.com/ThanhNguyxn/cursor-setup/issues/new) with:
- What you expected to happen
- What actually happened
- Steps to reproduce
- Your environment (OS, Python version)

### 💡 Suggest Features

Have an idea? [Open an issue](https://github.com/ThanhNguyxn/cursor-setup/issues/new) and describe:
- The feature you want
- Why it would be useful
- Any implementation ideas

### 📝 Improve Documentation

- Fix typos
- Clarify confusing sections
- Add examples
- Translate to other languages

---

## Development Setup

Want to work on the Python code? Here's how:

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/cursor-setup.git
cd cursor-setup

# Create a virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Verify it works
cursor-setup --help
```

### Running Tests

```bash
pytest
```

### Code Quality Checks

```bash
# Format code
black src/

# Lint
ruff src/

# Type check
mypy src/
```

---

## Code Style

### Python

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://black.readthedocs.io/) for formatting
- Add type hints to all functions
- Write docstrings for public functions

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new template for X
fix: handle network timeout gracefully  
docs: update installation instructions
chore: bump dependencies
```

### Branch Naming

- `feat/description` — New features
- `fix/description` — Bug fixes
- `docs/description` — Documentation
- `chore/description` — Maintenance

---

## Questions?

- 💬 [Open a Discussion](https://github.com/ThanhNguyxn/cursor-setup/discussions)
- 🐛 [Open an Issue](https://github.com/ThanhNguyxn/cursor-setup/issues)

---

**Thank you for contributing!** 🚀

Every template you add helps developers around the world set up their projects faster.
