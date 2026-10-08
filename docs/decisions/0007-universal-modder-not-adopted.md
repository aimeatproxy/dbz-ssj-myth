# 0007. universal-modder not adopted

- Status: Accepted
- Date: 2026-10-08

## Context

[rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) was suggested as useful. From its README (the only part reviewed): it is a set of agent skills plus a `um` CLI for **modding PC games**, centred on Windows, game-engine playbooks (Unity, Unreal, Godot, etc.), fal.ai asset generation, and in-game screenshot/input automation. Its list of engine playbooks mentions "retro decomps", but SNES is not named. It ships per-agent config copies, and its MCP setup targets fal.

## Decision

Do not vendor, depend on, or configure it. Its automation targets running PC games and generating new assets; this project's work is static/dynamic analysis of 65816 code in an emulator and matching a build. If its "retro decomps" playbook proves relevant, read it as prose and borrow ideas through an ADR or docs, not code.

## Consequences

- No extra dependencies, API keys, or agent config in the repo.
- Revisit if the maintainers add SNES/65816 tooling that is actually exercised (emulator tracing, CDL handling).
