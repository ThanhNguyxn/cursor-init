# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2024-12-02

### Changed

- **BREAKING**: Renamed package from `cursor-init` to `cursor-setup` (PyPI name conflict)
- CLI command is now `cursor-setup` instead of `cursor-init`

### Added

- Dynamic template registry from remote `rules.json`
- `--url` flag to install from any URL directly
- `--force` flag to skip overwrite confirmation
- Silent fallback to local templates when network fails
- GitHub Actions workflow for auto-publishing to PyPI
- Remote templates for: Laravel, Go, Rust, React, Vue, SvelteKit

### Technical

- Built with Typer for CLI framework
- Rich for beautiful terminal output
- Requests for HTTP fetching
- Supports Python 3.9 - 3.13

## [0.1.0] - 2024-12-02

### Added

- Initial release of CLI tool
- `cursor-setup list` command to display available templates
- `cursor-setup install <template>` command to install cursor rules
- `cursor-setup show <template>` command to preview templates
- Built-in templates for:
  - Python (type hints, docstrings, PEP 8)
  - Next.js (App Router, Server Components, Tailwind)
  - Flutter (clean architecture, Riverpod)
  - Java Spring Boot (Spring Boot 3+, modern Java)

[Unreleased]: https://github.com/ThanhNguyxn/cursor-setup/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/ThanhNguyxn/cursor-setup/releases/tag/v2.0.0
[0.1.0]: https://github.com/ThanhNguyxn/cursor-setup/releases/tag/v0.1.0
