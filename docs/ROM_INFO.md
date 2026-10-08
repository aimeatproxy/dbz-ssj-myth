# Target ROM

Fill from `make header` output on the owner's **original Japanese** dump. Values below are **unknown** until then; do not guess. The owner is sourcing that dump from their own cartridge; it is not yet in `baserom/`.

| Field | Value |
| --- | --- |
| Title (assumed) | Dragon Ball Z: Super Saiya Densetsu (Super Famicom, 1992, Bandai) |
| Internal title | TBD (original dump only) |
| Region / country byte | TBD |
| Revision / version byte | TBD |
| Map mode | TBD (LoROM / HiROM), SlowROM / FastROM TBD |
| ROM size | TBD |
| SRAM size | TBD |
| Coprocessor / cart chips | TBD (ROM type byte) |
| Internal checksum | TBD (stored / computed / valid?) |
| SHA-1 (headerless) | TBD → also written to `/rom.sha1` |
| CRC32 (headerless) | TBD |
| Copier header present in dump | TBD |
| Dump source / method | TBD (owner's own cartridge) |

## Notes

- Compare the hash against a database of known-good dumps (e.g. No-Intro) to confirm it's an unmodified dump and to learn if revisions exist.
- If several revisions exist, one is the target; others become diffs later.

## What we know so far (owner-reported, unverified here)

- **Target:** the original Japanese release, from the owner's own cartridge. Not yet available; M1 is open.
- **Not the target:** a fan-translated ROM, `baserom/Dragon Ball Z - Legend of the Super Saiyan (tr1).sfc`. Per the owner: title field overwritten with "Vimm's Lair", checksum mismatch, USA country byte. It is a patched ROM, so nothing in the table above may be taken from it, `rom.sha1` must not be created from it, and its layout says nothing reliable about the original. English-text reference only ([ADR-0008](decisions/0008-translated-rom-text-reference-only.md)).
- **Related references:** one Famicom ROM held, the other missing. See [references.md](references.md).
- The cloud environment has no ROMs, so none of the above was inspected or hashed here.

## When the original dump arrives

1. Place it at `baserom/baserom.sfc` (strip a copier header first if `make header` reports one).
2. `make header`; fill the table above from its output; write the headerless SHA-1 to `rom.sha1`.
3. Tick M1 and start M2 in [PROGRESS.md](PROGRESS.md).
