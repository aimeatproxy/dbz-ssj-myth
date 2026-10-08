# 0005. Reference ROMs stay local

- Status: Accepted
- Date: 2026-10-08

## Context

The owner plans to use ROMs of related earlier games (believed to be two Famicom titles, see `docs/references.md`) to understand the target. These add no matching value but help with logic, data layout, and text.

## Decision

- Reference ROMs and traces live in `references/` (git-ignored), supplied by the owner from copies they are entitled to use.
- The repo records only title/region/SHA-1 of each reference in `docs/references.md`.
- Agents and contributors do not obtain ROMs from the internet and do not commit or paste reference content.
- They are never build inputs. Only `baserom/` and `rom.sha1` define the build.

## Consequences

- Reference-driven findings must be restated as original documentation (what the format is), not copied data.
- The Famicom games are 6502; code will not match. Their value is comparative, not mechanical.
