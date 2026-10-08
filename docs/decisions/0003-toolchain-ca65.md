# 0003. Toolchain: ca65/ld65

- Status: Accepted
- Date: 2026-10-08

## Context

Options for assembling 65816: **ca65/ld65** (cc65 suite), **asar**, **WLA-DX**. A matching build needs exact control of bank layout and segment placement, scoped labels, assembler tracking of accumulator/index widths, and symbol output for the debugger.

## Decision

Use ca65 and ld65 with a memory-map config in `linker/snes.cfg`. Build with `make`. Tools in Python 3 standard library and POSIX shell.

## Consequences

- ld65 gives explicit memory areas and segments, map files, and `-Ln` label files that load into Mesen2.
- `.a8/.a16/.i8/.i16` make width mistakes assemble-time visible rather than silent.
- cc65 is widely packaged and maintained.
- Cost: DiztinGUIsh and many community disassemblies emit asar-style syntax, so an output converter is needed (tracked in `docs/WORKFLOW.md` §4).
- Reversible but expensive once much source exists; decide before real conversion starts (M5). Revisit at M3 if the converter proves painful.
- The SPC700 sound CPU needs a separate assembler decision (M9).
