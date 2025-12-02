# cursor-setup 🚀

> **The easiest way to set up Cursor AI for your project. One command. Done.**

[![PyPI version](https://badge.fury.io/py/cursor-setup.svg)](https://badge.fury.io/py/cursor-setup)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/cursor-setup)](https://pepy.tech/project/cursor-setup)

---

## What is this?

**cursor-setup** creates a `.cursorrules` file in your project folder. This file tells [Cursor AI](https://cursor.sh/) how to write code specifically for your tech stack (Python, React, Flutter, etc.).

**Before:** You Google for rules, copy-paste from random GitHub gists, hope they work...

**After:** Run one command and you're done! ✨

---

## 📦 Installation

```bash
pip install cursor-setup
```

That's it! Now you can use `cursor-setup` anywhere.

---

## 🚀 Usage

### ⚡ Quick Start (Fastest Way)

Already know what you want? Just run:

```bash
cursor-setup install python
```

Replace `python` with your stack: `nextjs`, `flutter`, `java-spring`, `laravel`, `vue`, `react`, `rust`, `golang`, `svelte`...

**Done!** A `.cursorrules` file is now in your project folder. 🎉

---

### 🔍 Interactive Mode (Browse Templates)

Not sure what's available? List all templates first:

```bash
cursor-setup list
```

You'll see a nice table like this:

```
📚 Available Cursor Rule Templates
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Template    ┃ Name               ┃ Description                             ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ python      │ Python             │ Modern Python with type hints...        │
│ nextjs      │ Next.js            │ Next.js 14+ with App Router...          │
│ flutter     │ Flutter            │ Flutter/Dart with clean architecture... │
│ laravel     │ Laravel            │ Laravel PHP framework with Eloquent...  │
│ vue         │ Vue.js             │ Vue 3 with Composition API...           │
│ react       │ React              │ React 18+ with hooks, TypeScript...     │
│ rust        │ Rust               │ Rust with memory safety patterns...     │
│ golang      │ Go                 │ Go with idiomatic patterns...           │
└─────────────┴────────────────────┴─────────────────────────────────────────┘
```

Pick one and install it:

```bash
cursor-setup install flutter
```

Want to see what's inside before installing?

```bash
cursor-setup show flutter
```

---

### 🔗 Pro Mode (Install from Any URL)

Found a custom `.cursorrules` file online? Install it directly:

```bash
cursor-setup install --url https://example.com/my-rules.txt
```

**Real-world example** — Install TypeScript rules from awesome-cursorrules:

```bash
cursor-setup install --url https://raw.githubusercontent.com/PatrickJS/awesome-cursorrules/main/rules/typescript-cursorrules-prompt-file/.cursorrules
```

This is perfect for:
- 🏢 **Teams**: Share a company-wide rules URL with your team
- 🧪 **Experiments**: Try community rules before they're officially added
- 🎯 **Custom setups**: Use your own private rules file

---

## 📋 All Available Templates

| Template | Best For |
|----------|----------|
| `python` | Python projects with type hints, docstrings, pytest |
| `nextjs` | Next.js 14+ with App Router, Server Components, Tailwind |
| `flutter` | Flutter/Dart mobile apps with clean architecture |
| `java-spring` | Spring Boot 3+ REST APIs with modern Java |
| `laravel` | Laravel PHP with Eloquent, Blade templates |
| `vue` | Vue 3 with Composition API, TypeScript, Pinia |
| `react` | React 18+ with hooks, TypeScript patterns |
| `rust` | Rust with ownership patterns, error handling |
| `golang` | Go with idiomatic patterns, concurrency |
| `svelte` | SvelteKit with TypeScript, stores, SSR |

> 💡 **More templates are added regularly!** Run `cursor-setup list` to see the latest.

---

## ⚙️ Options & Flags

| Flag | Short | Description |
|------|-------|-------------|
| `--url` | `-u` | Install from a direct URL |
| `--force` | `-f` | Overwrite existing file without asking |

**Examples:**

```bash
# Skip the "overwrite?" prompt
cursor-setup install python --force

# Short form
cursor-setup install python -f

# Combine flags
cursor-setup install -u https://example.com/rules.txt -f
```

---

## 🌐 How It Works

1. **Local templates** are bundled with the package (always available offline)
2. **Remote templates** are fetched from our [community registry](https://github.com/ThanhNguyxn/cursor-setup/blob/main/rules.json)
3. If you're offline, it silently falls back to local templates only

This means:
- ✅ Works offline with built-in templates
- ✅ Gets the latest community templates when online
- ✅ Never fails due to network issues

---

## 🤝 Contributing

We'd love your help! The easiest way to contribute:

**Add a new template to our registry:**

1. Fork the repository
2. Edit `rules.json`
3. Add your template URL + description
4. Submit a PR!

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions.

---

## 🛠️ Development

```bash
# Clone the repo
git clone https://github.com/ThanhNguyxn/cursor-setup.git
cd cursor-setup

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in dev mode
pip install -e ".[dev]"

# Test it
cursor-setup --help
```

---

## 📄 License

MIT License — use it however you want!

---

## 🙏 Credits

- Inspired by [Cursor](https://cursor.sh/) editor
- Built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/)
- Community templates from [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)
- Thanks to all contributors! ❤️

---

<p align="center">
  <b>Found this useful? ⭐ Star us on GitHub!</b>
</p>

<p align="center">
  <a href="https://github.com/ThanhNguyxn/cursor-setup">https://github.com/ThanhNguyxn/cursor-setup</a>
</p>
