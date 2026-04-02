---
name: event-modeling
description: Use this skill to discover workflows, map events, commands, read models, automations, and Given/When/Then scenarios before implementation. It keeps discovery separate from architecture and implementation decisions.
---

# Event Modeling

Use this skill to understand a workflow before writing code.

## Core rule

Do not jump from vague product language straight to implementation. Map the workflow first.

The default standard for workflow documents is information completeness, not
just structural completeness.

## Two phases

1. **Domain discovery**
   - Identify actors, major workflows, external integrations, and the best starting workflow.
   - Capture the overview in `docs/event_model/domain/overview.md`.
2. **Workflow design**
   - Work through one workflow at a time.
   - Identify events, commands, views, automations, and translations.
   - Start from the shared workflow template at
     `plugins/codex-sdlc/templates/event_model_workflow.md` unless the user
     explicitly asks for a different artifact shape.
   - Produce pattern-specific Given/When/Then scenarios with concrete command
     and view examples.

## Modeling rules

- Events are past-tense business facts.
- Read models must trace back to source events.
- Commands depend on user input and prior events, not on read models.
- Automations need a trigger, a view or condition, a process, and a resulting command.
- Keep architecture selection and implementation details out of the event-modeling session.
- Remove unresolved either/or choices from event contracts before calling the
  workflow done.
- Separate operator-facing queries/views from internal inspection queries/views.
- If a workflow has no standalone automation or translation slice, say so
  explicitly instead of leaving the section implied.

## Information completeness

Run an information-completeness pass for every workflow and rerun it after
every substantive model change.

At minimum, verify:

- every event attribute has an explicit source from command input, generation,
  or a stated derivation rule
- every projection attribute traces back to source events or an explicit
  query-time derivation rule
- absence states are modeled explicitly rather than implied
- event contracts do not contain unresolved alternatives
- command preconditions trace back to prior events, not only to convenient
  read-model language

## Slice rules

- Each slice must include an application-boundary acceptance scenario.
- A slice that only changes internal code without an observable boundary is not a full vertical slice.
- Slices sharing the same event contract should stay independently testable.
- Classify every slice as one of the four patterns below. Do not mix pattern
  types inside one scenario.

## Pattern-specific scenarios

- `State Change`: `Given [EVENTS], When [COMMAND], Then [EVENTS | ERROR]`
- `State View`: `Given [EVENTS], Then [PROJECTION]`
- `Automation`: `Given [EVENTS | TIMER], When [AUTOMATION], Then [COMMAND -> EVENTS]`
- `Translation`: `Given [EXTERNAL EVENT], When [TRANSLATION], Then [INTERNAL COMMAND -> EVENTS]`

## Boundary examples

- Provide a concrete CLI or equivalent boundary example for every
  application-facing command.
- Provide a concrete CLI or equivalent boundary example for every
  operator-facing view/query.
- Internal inspection queries may exist, but they must be labeled as supporting
  surfaces rather than accidental public views.

## Codex-specific guidance

- Ask clarifying questions when domain knowledge is missing.
- Prefer explicit documents under `docs/event_model/` over transient chat-only analysis.
- Use this skill before major TDD work when the workflow is not yet well-shaped.
- After any model edit, revisit the `Information Completeness Check` section
  before claiming the workflow is done.

## Common failure modes

- stopping at structural completeness instead of information completeness
- mixing state-change and state-view scenarios in the same slice
- omitting CLI examples for commands or views
- inventing a fake automation slice for a synchronous flow narrative
- adding internal debug views without modeling the supporting queries

## Done when

- the workflow is mapped clearly enough to decompose into pattern-specific
  slices
- each slice has concrete GWT scenarios in the correct pattern form
- every application-boundary command and operator-facing view has a concrete
  example
- every event attribute has an explicit source
- every projection attribute has a traceable source path
- absent automation or translation patterns are explicitly stated when they do
  not exist
- no major workflow gap remains unaccounted for
