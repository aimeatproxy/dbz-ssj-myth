# Contributing

## Hard rules

1. **Never commit game data**: ROMs, graphics, audio, music, text dumps, save states, large hex blobs. `make hooks` installs a pre-commit guard; CI enforces it too. Describe data structurally and extract at build time from the user's own `baserom/`.
2. **The build must stay byte-identical.** Run `make compare` before every commit that touches `src/`, `include/`, `linker/`, or `data/`. A change that breaks matching does not merge.
3. **Don't claim what you haven't verified.** Label guesses (`; TODO(guess):`) and distinguish them from confirmed behaviour. Confirmed means observed in an emulator trace/debugger or proven by a caller.

## Workflow

- Branch per task; small PRs (one routine, table, or subsystem).
- Commit messages: imperative, scoped, e.g. `bank01: name sprite OAM builder`.
- Add a line to `CHANGELOG.md` under `[Unreleased]` for notable changes and tick off [docs/PROGRESS.md](docs/PROGRESS.md) items.
- Non-obvious tooling, format, or structure choices get an ADR: copy [docs/decisions/0000-template.md](docs/decisions/0000-template.md), take the next number, add it to the index.

## Source conventions (ca65)

- Files: `src/bankNN_<topic>.s`; one logical subsystem per file once split out of raw bank dumps.
- Labels: routines `PascalCase` (`UpdateSprites`), local labels `@lowercase`, data `PascalCase` with a type suffix where useful (`PaletteTable`, `TextPtrs`). Unknown code/data: `Code_BBAAAA` / `Data_BBAAAA` (bank, address). Rename as understood.
- RAM: `include/ram.inc`, named `wFoo` (WRAM), `sFoo` (SRAM); unknowns `wUnk_7E1234`.
- Hardware registers: `include/snes_regs.inc`, using the standard register names.
- Always state register widths where they change: use `.a8/.a16/.i8/.i16` and `rep/sep` so ca65 tracks them.
- Use named constants over magic numbers when meaning is known. Comments explain *why*, not the opcode.
- Pointer tables and jump tables: emit with `.word`/`.addr`/`.faraddr` of labels, not literals, so layout changes don't silently break.
- Indent: tabs (see `.editorconfig`). LF line endings.

## Tools

Python 3.10+ standard library only, unit-tested under `tests/` (`make test`). Shell scripts must be POSIX `sh`.
