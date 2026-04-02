---
name: tdd
description: Use this skill whenever the user wants test-first implementation. It runs a Codex-native RED -> DOMAIN -> GREEN -> DOMAIN -> COMMIT loop, with optional subagent delegation when explicitly useful.
---

# TDD

Use this skill for disciplined test-first implementation in Codex.

## The cycle

Every feature moves through:

1. **RED**
   - Write one failing test for the next behavior.
   - Prefer an acceptance boundary first, then drill inward if needed.
   - Run the test and capture the real failure.
2. **DOMAIN**
   - Review the test and the emerging shape for primitive obsession or invalid-state risks.
   - Introduce type stubs or semantic types if they are required for the test to compile meaningfully.
3. **GREEN**
   - Fix the next actual failure with the smallest useful implementation step.
   - Do not rewrite the test to match the code.
   - If the change is too large, drill down into a smaller inner cycle.
4. **DOMAIN**
   - Review the implementation for domain integrity after the test passes.
5. **COMMIT**
   - Run the relevant broader checks.
   - Commit the completed cycle before starting a new RED phase.
   - In this workflow, commit means a local git commit on the trunk path, not opening a PR.

## Phase boundaries

- RED edits tests.
- DOMAIN edits or proposes types and domain structure.
- GREEN edits implementation.
- COMMIT performs git and verification steps, not new feature work.

These boundaries are partly advisory in Codex because the strongest hook surface today is around Bash, not every file edit. Follow them anyway.

## Outside-in bias

- Start from an application boundary when possible.
- A test that only calls an internal helper is not the acceptance test for the slice.
- Keep the outer behavior in view while drilling into smaller unit-level cycles.

## Delegation

- Default to a single-agent TDD loop.
- Use subagents only when explicitly requested or when a bounded sidecar review or implementation slice is clearly worth it.
- Do not hide the orchestration in a generic manager agent.

## Evidence

- Run the test after RED.
- Run the changed test path during GREEN.
- Run the broader relevant check set before COMMIT.
- Do not claim success without actual command output.

## Codex-specific guidance

- Keep the cycle compatible with direct-to-trunk work.
- Do not assume PR review or branch-based gating.
- Use the `domain-modeling` skill for the domain checkpoints.
- Use `codex-review` after the TDD cycle if an additional review pass is warranted.

## Done when

- the intended test was written before the implementation
- the test passes with minimal code
- domain issues were reviewed on both sides of implementation
- the cycle ends in a real commit before the next RED phase
