# References

## Hardware and tools

- SNES Development wiki: <https://snes.nesdev.org/> and the Super Famicom Development Wiki: <https://wiki.superfamicom.org/> (65816 reference, registers, DMA, memory maps)
- cc65 / ca65 docs: <https://cc65.github.io/doc/ca65.html>
- Mesen2: <https://github.com/SourMesen/Mesen2>
- DiztinGUIsh: <https://github.com/IsoFrieze/DiztinGUIsh>

(Links were written from memory and not re-verified; fix any that moved.)

## Related games (user-supplied, local only)

The user states that the target game was based on two earlier titles. These are likely the Famicom games *Dragon Ball Z: Kyōshū! Saiyajin* (1990) and *Dragon Ball Z II: Gekishin Freeza!!* (1991), to be confirmed by the user. They are 6502-based, so code does not byte-match anything in the SNES game; they are useful for game logic, data layout intent, and text.

Record each reference you hold here (title, region, SHA-1 of headerless dump). Files stay in `references/` (git-ignored, [ADR-0005](decisions/0005-reference-roms.md)).

| Title | Region | SHA-1 | Notes |
| --- | --- | --- | --- |
| _(none recorded yet)_ | | | |

## Prior art

Other SNES disassembly projects are worth reading for structure and tooling conventions. Add specific ones here after checking they are current; none are vendored or depended on.

## Considered tooling

- [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder): evaluated and not adopted, see [ADR-0007](decisions/0007-universal-modder-not-adopted.md).
