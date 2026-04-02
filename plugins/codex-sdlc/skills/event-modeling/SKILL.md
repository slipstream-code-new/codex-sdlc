---
name: event-modeling
description: Use this skill to discover workflows, map events, commands, read models, automations, and Given/When/Then scenarios before implementation. It keeps discovery separate from architecture and implementation decisions.
---

# Event Modeling

Use this skill to understand a workflow before writing code.

## Core rule

Do not jump from vague product language straight to implementation. Map the workflow first.

## Two phases

1. **Domain discovery**
   - Identify actors, major workflows, external integrations, and the best starting workflow.
   - Capture the overview in `docs/event_model/domain/overview.md`.
2. **Workflow design**
   - Work through one workflow at a time.
   - Identify events, commands, views, automations, and translations.
   - Produce slice-level Given/When/Then scenarios with concrete examples.

## Modeling rules

- Events are past-tense business facts.
- Read models must trace back to source events.
- Commands depend on user input and prior events, not on read models.
- Automations need a trigger, a view or condition, a process, and a resulting command.
- Keep architecture selection and implementation details out of the event-modeling session.

## Slice rules

- Each slice must include an application-boundary acceptance scenario.
- A slice that only changes internal code without an observable boundary is not a full vertical slice.
- Slices sharing the same event contract should stay independently testable.

## Codex-specific guidance

- Ask clarifying questions when domain knowledge is missing.
- Prefer explicit documents under `docs/event_model/` over transient chat-only analysis.
- Use this skill before major TDD work when the workflow is not yet well-shaped.

## Done when

- the workflow is mapped clearly enough to decompose into slices
- each slice has concrete GWT scenarios
- no major workflow gap remains unaccounted for
