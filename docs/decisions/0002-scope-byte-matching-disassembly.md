# 0002. Scope: byte-matching disassembly

- Status: Accepted
- Date: 2026-10-08

## Context

"Decomp" usually means recovering C that compiles to the original bytes. That works for 32-bit-era games built with known compilers. A 1992 Super Famicom title is almost certainly hand-written 65816 assembly; there is no compiler output to match.

## Decision

The deliverable is an annotated, labelled assembly source that assembles to a ROM byte-identical to a specific original dump (SHA-1 in `rom.sha1`). Matching is the correctness criterion and is checked by `make compare`. Equivalent-but-different builds, rewrites in C, or ports are out of scope (they may be separate projects built on this one).

## Consequences

- Progress is measurable and regressions are caught instantly.
- Every change must preserve layout; refactors that move code need care (pointer tables via labels).
- Only the specific revision in `rom.sha1` is the target. Other revisions are later work.
- If it turns out parts of the game were compiled/generated, revisit via a new ADR.
