# 0004. No copyrighted material in the repo

- Status: Accepted
- Date: 2026-10-08

## Context

The game is copyrighted by its owners. Disassembly projects survive by distributing only original work (source, tools, documentation) and requiring users to supply their own dump. Source that is a line-for-line rendering of the program is itself a derivative work; that risk is real and accepted by the owner of the repo, but shipping the data (graphics, audio, text, the ROM) is a separate, avoidable one.

## Decision

- The repo never contains the ROM, graphics, audio, music, extracted text, save states, or long hex dumps of game data.
- Data is described structurally in `data/` and extracted from the user's `baserom/` at build time.
- `baserom/`, `references/`, and ROM file extensions are git-ignored; `tools/check_no_roms.sh` runs in a pre-commit hook and CI.
- The repo may contain SHA-1/CRC32 hashes of dumps (they identify, not reproduce).

## Consequences

- Nobody can build without their own dump. That is intended.
- Contributors must not paste ROM bytes into issues, PRs, or docs beyond tiny illustrative snippets.
- This reduces, but does not eliminate, legal risk; it is not legal advice. Takedown requests are honoured.
