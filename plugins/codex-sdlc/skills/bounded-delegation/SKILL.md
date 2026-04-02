---
name: bounded-delegation
description: Keep Codex delegation explicit, sparse, and well-scoped. Use when the user asks for subagents, parallel work, or a multi-agent approach, or when a sidecar task is clearly parallelizable without changing the main workflow default.
---

# Bounded Delegation

Codex can delegate, but this workflow is not factory-first.

## Default

- Stay single-agent unless the user explicitly asks for delegation or a sidecar task is clearly parallel and bounded.

## When to delegate

- A read-only repository question can be answered independently.
- A non-overlapping implementation slice is well-defined.
- Verification can run in parallel with ongoing local work.

## When not to delegate

- The next local step is blocked on the answer.
- The task is tightly coupled to the current reasoning thread.
- The likely gain is small compared with coordination cost.

## Requirements

- Every delegated task must have one clear output.
- Avoid overlapping write scopes.
- Reintegrate results locally rather than turning delegation into an ambient team process.
