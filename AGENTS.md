# AGENTS.md

Rules for AI coding agents working in this repo. Read [CONTRIBUTING.md](CONTRIBUTING.md) first; this file only adds agent-specific constraints.

## Project in one line

Byte-matching ca65 disassembly of a 1992 Super Famicom game. Target ROM details: `docs/ROM_INFO.md`. Decisions: `docs/decisions/`.

## Never

- Never commit, print, or paste ROM bytes, extracted assets, or long hex dumps of game data. Small excerpts (a few instructions) needed to explain a routine in a comment are fine.
- Never fetch, request, or help obtain ROMs from the internet. Only the user supplies dumps, locally, in `baserom/` and `references/` (git-ignored).
- Never mark something as "confirmed" from inference alone. Use `TODO(guess)`.
- Never "fix" a mismatch by editing the expected hash in `rom.sha1`.

## Always

- Run `make check` before committing, and `make compare` when a baserom is present.
- Treat `baserom/` as read-only.
- Check `docs/PROGRESS.md` and update it, plus `CHANGELOG.md`, when finishing a unit of work.
- Record non-trivial decisions as ADRs.
- If you can't run the ROM or emulator (e.g. no baserom in the environment), say so; don't invent addresses, labels, or behaviour.

## Environment notes

- Cloud/CI sessions normally have **no ROM**. Work there is limited to tooling, docs, and source that is already verified against a ROM elsewhere.
