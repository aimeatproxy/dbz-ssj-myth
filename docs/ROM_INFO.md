# Target ROM

Fill from `make header` output on the owner's dump. Values below are **unknown** until then; do not guess.

| Field | Value |
| --- | --- |
| Title (assumed) | Dragon Ball Z: Super Saiya Densetsu (Super Famicom, 1992, Bandai) |
| Internal title | TBD |
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
