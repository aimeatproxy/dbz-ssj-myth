# Changelog

All notable changes are recorded here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project does not use semantic versioning; entries are grouped by date until a first matching build exists, after which milestones will be tagged.

## [Unreleased]

### Added
- Repository scaffolding: README, CONTRIBUTING, AGENTS.md, ADRs 0001–0007, setup/workflow/ROM-info/progress/reference docs.
- `tools/rom_header.py`: SNES header, copier-header, checksum and hash inspector with unit tests.
- `tools/check_no_roms.sh` and `.githooks/pre-commit` guard against committing game data.
- `Makefile` (header, verify, build, compare, test, check) targeting ca65/ld65.
- CI workflow (tool tests + no-ROM check), PR and issue templates, `.editorconfig`, `.gitattributes`.
