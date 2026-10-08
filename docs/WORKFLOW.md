# Workflow

How the project goes from an opaque ROM to labelled, matching source. Each stage ends with `make compare` passing (byte-identical) except stages 1–2, which come before a build exists.

## 1. Identify the ROM

`make header`, then fill in [ROM_INFO.md](ROM_INFO.md) and create `rom.sha1` containing the headerless SHA-1. Confirm title, region, revision, map mode (LoROM/HiROM), size, and that the internal checksum is valid (a bad one means a bad dump).

## 2. Memory map and linker config

Write `linker/snes.cfg` for the discovered mapping: bank layout, header segment, and the vectors at `$FFE0–$FFFF`. Include `include/snes_regs.inc` with standard hardware register names.

## 3. Matching build from splits ("M3")

Describe the ROM as ordered ranges in `data/splits.txt` (start, end, kind: `code` | `data` | `unknown`, name). Tooling (to be written) extracts each range from `baserom/baserom.sfc` into `build/` at build time; code ranges start as `.incbin` of those chunks. The first goal is a build that is byte-identical **before any real disassembly**. After that, every conversion is a small, always-verifiable step.

## 4. Find the code

Static disassembly of 65816 needs the M/X register-width state at every instruction, which cannot be derived without execution. So:

1. Run the game in Mesen2 with the debugger's code/data logger on; play broadly (menus, every character, stages, battles, game over, ending if possible).
2. Export the CDL. Load ROM + CDL in DiztinGUIsh to mark code, data, and M/X flags; iterate on gaps.
3. Convert its output to ca65 syntax (conversion tool: TBD, recorded as an ADR when chosen).

Coverage is never complete from play alone; unreached code is found by following jumps/tables from known code.

## 5. Convert and name

Per range, in order of usefulness: reset/NMI/IRQ handlers → main loop → DMA/VRAM upload → input → sprite/OAM → game state machine → battle logic → text engine → sound driver (SPC700 is a separate processor and needs its own toolchain decision).

For each routine: replace the `.incbin` with source, add labels and RAM names, `make compare`. Mark unverified naming `TODO(guess)`.

## 6. Data

Describe formats structurally (e.g. "pointer table of 24-bit addresses to compressed tiles") and have the build extract from the baserom. Compressed graphics/text: document the algorithm and write a decompressor in `tools/`; never commit the output.

## 7. Cross-reference related games

See [references.md](references.md). Use earlier titles to understand intent and data, not to copy bytes (different CPU, different code).

## Verification loop

```sh
make            # assemble
make compare    # must be identical to rom.sha1
```

On a mismatch: dump both ROMs, find the first differing offset (`cmp`), map it back to a source line through `build/dbz-ssj.map`/`.lbl`.
