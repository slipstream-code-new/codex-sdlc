---
name: architecture-decisions
description: Use this skill for ADRs, architecture choices, technology selection, boundaries, and updates to `docs/ARCHITECTURE.md`. It keeps research ahead of prose and requires explicit approval before a decision is treated as merged.
---

# Architecture Decisions

Use this skill to turn architecture choices into durable, reviewable records.

## Core rule

Research first. Do not write ADR prose from memory or assumptions when the decision depends on external tools, frameworks, protocols, or services.

## Lifecycle

1. **Research**
   - Identify the dependencies or constraints the decision touches.
   - Inspect the real code, documentation, or repository context.
   - Summarize what you verified and what remains uncertain.
2. **Critique**
   - List unverified assumptions.
   - List missing dependency checks.
   - List conflicts with existing architecture or repo constraints.
   - Resolve these before drafting.
3. **Draft**
   - Create one ADR per decision in `docs/decisions/YYYYMMDD-<slug>.md`.
   - Keep claims concrete and traceable to the research summary.
   - Update `docs/ARCHITECTURE.md` only when the decision is actually accepted.
4. **Hold**
   - Treat the ADR as pending until the user explicitly approves it.
   - Do not treat silence as approval.
5. **Merge**
   - After approval, integrate the decision into `docs/ARCHITECTURE.md`.
   - In this workflow, merge means accepted into trunk or accepted in-place. It does not imply a PR.

## Codex-specific guidance

- Use local repo inspection first.
- Use web research when the decision depends on drift-prone external facts.
- Do not assume a PR-based ADR flow. Use branches only when the user wants them.
- If the user says "draft the ADR," draft it, but still separate verified findings from open questions.

## Deliverables

- `docs/decisions/` entry for the decision
- updated `docs/ARCHITECTURE.md` after approval
- short research summary or citations backing the draft

## Done when

- the decision record is atomic
- the rationale reflects verified reality
- the user has explicitly accepted the decision before it is treated as active
