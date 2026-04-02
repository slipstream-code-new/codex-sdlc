---
name: codex-review
description: Review local changes before a trunk commit or push. Use when the user asks for review, a final preflight pass, or a regression check focused on correctness, risks, and missing tests.
---

# Codex Review

Use a code-review mindset. Findings come first.

## Focus

- Behavioral regressions
- Incorrect assumptions in changed code
- Missing or weak verification
- Risky git or release steps

## Workflow

1. Inspect the diff, not just final files.
2. Trace the changed behavior to the user-facing or system-facing boundary.
3. Check that the relevant tests or validation steps exist and were run.
4. Classify each accepted finding as `event-model gap`, `domain/core gap`, or
   `shell/CLI gap`.
5. If a finding is an `event-model gap`, patch the event model first, rerun the
   model completeness pass, and only then implement the fix.
6. For stateful CLIs or operator tooling, explicitly inspect open-vs-create
   behavior, bootstrap/init safety, wrong-path or wrong-store behavior, and
   lifecycle-state interactions.
7. Report findings ordered by severity with file references when possible.
8. If no findings exist, say so explicitly and mention residual risk or test gaps.

## Biases

- Prefer concrete evidence over hypothetical style commentary.
- Do not center PR review conventions. This is local preflight review for trunk shipping.
