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
   - Create one ADR per decision in the repository's ADR location. Default to
     `docs/adrs/NNNN-<slug>.md` unless the repo documents a different layout.
   - Keep claims concrete and traceable to the research summary.
   - After the first draft, immediately surface any remaining open questions.
   - If you ask any multiple-choice question, or any batch of multiple
     questions, use the `request_user_input` tool instead of writing them
     directly in chat.
   - Update `docs/ARCHITECTURE.md` only when the decision is actually accepted.
4. **Hold**
   - Treat the ADR as pending until the user explicitly approves it.
   - Do not treat silence as approval.
5. **Merge**
   - After approval, integrate the decision into `docs/ARCHITECTURE.md`.
   - In this workflow, merge means accepted into trunk or accepted in-place. It does not imply a PR.
   - In repos where `docs/ARCHITECTURE.md` is the active architecture
     authority, do not treat the accepted ADR as implementation-active until
     that document has been updated.

## Codex-specific guidance

- Use local repo inspection first.
- Use web research when the decision depends on drift-prone external facts.
- Do not assume a PR-based ADR flow. Use branches only when the user wants them.
- If the user says "draft the ADR," draft it, but still separate verified findings from open questions.
- If the user asks a direct architecture question, answer it directly before
  proposing adjacent next steps.

## Deliverables

- ADR entry in the repository's documented ADR location
- updated `docs/ARCHITECTURE.md` after approval
- short research summary or citations backing the draft

## Done when

- the decision record is atomic
- the rationale reflects verified reality
- the user has explicitly accepted the decision before it is treated as active
- any accepted decision that changes current architecture has been projected
  into `docs/ARCHITECTURE.md` before implementation relies on it
