# references/

Local-only material used to understand the target game. Everything here except this file is git-ignored ([ADR-0005](../docs/decisions/0005-reference-roms.md)).

Suggested layout (all yours, none committed):

```
references/
  famicom/<name>.nes          related earlier games (6502), see docs/references.md
  traces/                     emulator trace logs, CDL files
  notes/                      scratch notes
```

Record *what* each reference is (title, region, SHA-1) in `docs/references.md`, never the files themselves.
