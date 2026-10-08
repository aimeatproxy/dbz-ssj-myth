# Setup

## Required

| Tool | Why | Install |
| --- | --- | --- |
| `make`, `sh` | build driver | system package manager |
| Python 3.10+ | tools (stdlib only) | system package manager |
| cc65 (`ca65`, `ld65`) | assemble and link 65816 ([ADR-0003](decisions/0003-toolchain-ca65.md)) | `apt install cc65`, `brew install cc65`, or build from <https://cc65.github.io/> |
| Your own ROM dump | the reference being matched | see `baserom/README.md` |

## Strongly recommended

| Tool | Why |
| --- | --- |
| [Mesen2](https://github.com/SourMesen/Mesen2) | debugger, trace logger, code/data log (CDL), memory viewers, label import |
| [DiztinGUIsh](https://github.com/IsoFrieze/DiztinGUIsh) | SNES-aware disassembler that tracks M/X flags and consumes CDL |
| A hex editor with a diff view (ImHex, HxD, `cmp -l`) | locating the first mismatching byte |

## First run

```sh
make hooks                      # one-time per clone
cp <your dump> baserom/baserom.sfc
make header                     # prints map mode, checksum, hashes
make check                      # tool tests + no-ROM guard
```

Then follow [WORKFLOW.md](WORKFLOW.md). If `make header` reports a copier header, strip it first (see `baserom/README.md`).

## Environment notes

- **Cloud / CI sessions have no ROM.** They can run `make check` only. Anything needing the dump, emulator, or `make compare` happens on a machine that has them.
- Windows: use WSL2; keep the repo in the WSL filesystem so line endings and the `make` build behave.
