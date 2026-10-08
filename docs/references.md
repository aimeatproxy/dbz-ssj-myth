# References

## Hardware and tools

- SNES Development wiki: <https://snes.nesdev.org/> and the Super Famicom Development Wiki: <https://wiki.superfamicom.org/> (65816 reference, registers, DMA, memory maps)
- cc65 / ca65 docs: <https://cc65.github.io/doc/ca65.html>
- Mesen2: <https://github.com/SourMesen/Mesen2>
- DiztinGUIsh: <https://github.com/IsoFrieze/DiztinGUIsh>

(Links were written from memory and not re-verified; fix any that moved.)

## Related games (user-supplied, local only)

The user states that the target game was based on two earlier titles: the Famicom games *Dragon Ball Z: Kyōshū! Saiyajin* (1990) and *Dragon Ball Z II: Gekishin Freeza!!* (1991). The owner has confirmed the first by filename; only that one is held.

Record each reference you hold here (title, region, SHA-1). Files stay in `references/` (git-ignored, [ADR-0005](decisions/0005-reference-roms.md)). All entries below are **owner-reported**; the cloud environment has no ROMs, so none were re-hashed or inspected here.

| Title | Region | SHA-1 | Notes |
| --- | --- | --- | --- |
| *Dragon Ball Z: Kyōshū! Saiyajin* (Famicom), file `references/Kyoushuu! Saiya Jin (J) [!].nes` | Japan | `375604EE5CC7CA7569FF4807C9ED5BA643002E87` (whole file, **including** the 16-byte iNES header; not the headerless convention used for the SNES target) | Owner reports 512 KiB of PRG+CHR after the 16-byte iNES header. Exact file size, mapper, and PRG/CHR split TBD (read from the iNES header locally). |
| *Dragon Ball Z II: Gekishin Freeza!!* (Famicom) | Japan | n/a | **Missing**: no ROM held. Anything attributed to this game is unavailable until the owner supplies it. |
| *Dragon Ball Z: Legend of the Super Saiyan (tr1)* (SNES fan translation), file `baserom/Dragon Ball Z - Legend of the Super Saiyan (tr1).sfc` | "USA" country byte (patched) | not recorded | **Not the target and not a matching reference.** Owner reports the title field is overwritten with "Vimm's Lair" and the internal checksum mismatches, i.e. modified. English text reference only ([ADR-0008](decisions/0008-translated-rom-text-reference-only.md)). Do not hash it into `rom.sha1`. Recommend moving it to `references/`. |

The Famicom games are 6502-based, so code does not byte-match anything in the SNES game; they are useful for game logic, data layout intent, and text.

## Prior art

Other SNES disassembly projects are worth reading for structure and tooling conventions. Add specific ones here after checking they are current; none are vendored or depended on.

## Considered tooling

- [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder): evaluated and not adopted, see [ADR-0007](decisions/0007-universal-modder-not-adopted.md).
