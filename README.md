# dbz-ssj-myth

A byte-matching disassembly ("decomp") of the Super Famicom game **Dragon Ball Z: Super Saiya Densetsu** (1992, Bandai).

> The exact title, region, and revision are **unconfirmed** until the owner's dump has been inspected with `make header` and recorded in [docs/ROM_INFO.md](docs/ROM_INFO.md).

**Status:** project scaffolding only. No code disassembled yet. See [docs/PROGRESS.md](docs/PROGRESS.md).

## What this is (and isn't)

- The goal is source that assembles to a ROM **byte-identical** to a known original dump ([ADR-0002](docs/decisions/0002-scope-byte-matching-disassembly.md)). A game of this era is hand-written 65816 assembly, so "decomp" here means an annotated, labelled, reassemblable disassembly, not C.
- **This repository contains no game data.** No ROM, no graphics, no audio, no text dumps, no large hex blobs ([ADR-0004](docs/decisions/0004-no-copyrighted-material.md)). You must supply your own legally obtained dump. The build extracts what it needs from it locally.
- Not affiliated with or endorsed by Bandai, Toei, Shueisha, or Akira Toriyama. Dragon Ball is their property.

## Quick start

Requirements: `make`, Python 3.10+, the [cc65](https://cc65.github.io/) suite (`ca65`, `ld65`). Details in [docs/SETUP.md](docs/SETUP.md).

```sh
git clone https://github.com/aimeatproxy/dbz-ssj-myth && cd dbz-ssj-myth
make hooks                                  # block accidental ROM commits
cp /path/to/your/dump.sfc baserom/baserom.sfc
make header                                 # map mode, checksum, SHA-1 of your dump
make verify                                 # once rom.sha1 exists: is it the right dump?
make compare                                # build and require a byte-identical ROM
```

`make` targets: `header`, `verify`, `all`, `compare`, `test`, `check`, `hooks`, `clean`.

## Layout

| Path | Purpose |
| --- | --- |
| `src/` | Assembly source (`.s`, ca65) |
| `include/` | Shared includes: hardware registers, RAM map, macros |
| `linker/` | ld65 memory-map configs |
| `data/` | Hand-authored data descriptions (never raw dumps) |
| `tools/` | Helper scripts (`rom_header.py`, `check_no_roms.sh`) |
| `tests/` | Unit tests for tools |
| `docs/` | Setup, workflow, ROM info, progress, ADRs |
| `baserom/` | Your dump goes here (git-ignored) |
| `references/` | Other reference ROMs / traces (git-ignored) |

## Documentation

- [docs/SETUP.md](docs/SETUP.md): install toolchain and emulator
- [docs/WORKFLOW.md](docs/WORKFLOW.md): how code gets from ROM to labelled source
- [docs/ROM_INFO.md](docs/ROM_INFO.md): identified facts about the target ROM
- [docs/PROGRESS.md](docs/PROGRESS.md): milestones
- [docs/references.md](docs/references.md): prior art, hardware docs, related games
- [docs/decisions/](docs/decisions/README.md): architecture decision records
- [CONTRIBUTING.md](CONTRIBUTING.md), [CHANGELOG.md](CHANGELOG.md), [AGENTS.md](AGENTS.md) (rules for AI agents)

## License

GPL-3.0 for the original work in this repository (see [LICENSE](LICENSE) and [ADR-0006](docs/decisions/0006-license.md)). This does not and cannot license the game itself.
