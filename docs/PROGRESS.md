# Progress

Milestones in order. Update when work lands.

- [x] **M0** Repository scaffolding, tooling, docs, ADRs
- [ ] **M1** ROM identified; `docs/ROM_INFO.md` and `rom.sha1` filled
- [ ] **M2** `linker/snes.cfg` and header/vectors reproduce the ROM layout
- [ ] **M3** Matching build from splits + `.incbin` (entire ROM, zero real disassembly)
- [ ] **M4** Mesen2 CDL coverage collected; code/data boundaries and M/X flags marked
- [ ] **M5** Reset/NMI/IRQ, main loop, DMA/VRAM, input converted to named source
- [ ] **M6** RAM map (`include/ram.inc`) covers all accessed WRAM/SRAM
- [ ] **M7** Core game systems documented (state machine, sprites, battle, text)
- [ ] **M8** Data formats documented with extractors (graphics, maps, text, tables)
- [ ] **M9** Sound (SPC700 driver) plan and tooling decided
- [ ] **M10** All code converted; all remaining `Code_/Data_` labels are intentional

Percentages of ROM converted will be tracked here once M3 gives a denominator.
