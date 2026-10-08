# 0008. Fan-translated ROM is a text reference only

- Status: Accepted
- Date: 2026-10-08

## Context

The owner holds a fan-translated SNES ROM of the target game (file `baserom/Dragon Ball Z - Legend of the Super Saiyan (tr1).sfc`). Per the owner it has the title field overwritten with "Vimm's Lair", a failing internal checksum, and a USA country byte. These symptoms indicate a modified ROM rather than an original dump (not inspected in this repo's cloud environment, which has no ROMs). The owner is sourcing the original Japanese ROM from their own cartridge.

## Decision

- The translated ROM is **not** the matching target. `rom.sha1` is never created from it, and `make header` / `make verify` / `make compare` are not run against it as if it were the target.
- It is used only to read English text while understanding the game. Findings are restated as original documentation, never copied data ([ADR-0004](0004-no-copyrighted-material.md), [ADR-0005](0005-reference-roms.md)).
- Because it is patched, even its text and pointers may differ from the original (relocated strings, changed tables, expanded ROM). Do not treat any offset or layout seen in it as evidence about the original.
- M1 (ROM identified) stays open until the original dump is in `baserom/baserom.sfc` and has been inspected.

## Consequences

- Nothing about the target (map mode, size, checksum, hashes) is recorded in `docs/ROM_INFO.md` until the original dump is inspected.
- Keeping it in `baserom/` risks confusing the build's expected input. It belongs in `references/`; moving it there is recommended.
