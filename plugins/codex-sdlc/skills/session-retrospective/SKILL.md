---
name: session-retrospective
description: Capture repeated mistakes and workflow friction after meaningful work. Use when a task exposed recurring failures, confusing prompts, missing guardrails, or instructions that should be tightened for future Codex sessions.
---

# Session Retrospective

Use this skill to tighten the workflow without turning every task into process work.

## Trigger conditions

- The same correction happened more than once.
- A risky command path needed a manual catch.
- AGENTS.md or a skill was missing an important routing rule.
- A hook should warn earlier or more clearly.

## Workflow

1. Summarize the friction in one sentence.
2. Identify whether the fix belongs in:
   - `AGENTS.md`
   - a plugin skill
   - a hook script
   - a helper script
3. Prefer the smallest durable fix.
4. Do not mutate this plugin automatically unless the user asked for it or the current task is explicitly about plugin maintenance.

## Output

- A concise proposed change
- Why it prevents the repeat failure
- Whether it is local to one repo or belongs in the shared plugin
