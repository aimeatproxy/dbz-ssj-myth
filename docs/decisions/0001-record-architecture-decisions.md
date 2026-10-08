# 0001. Record architecture decisions

- Status: Accepted
- Date: 2026-10-08

## Context

Reverse-engineering projects accumulate many judgement calls (tooling, naming, how data is described). Without a record, they get relitigated or silently reversed.

## Decision

Keep lightweight ADRs in `docs/decisions/`, one file per decision, numbered sequentially, indexed in `docs/decisions/README.md`.

## Consequences

Small overhead per decision. Superseding rather than editing keeps history honest. Agents are directed (AGENTS.md) to record non-trivial decisions.
