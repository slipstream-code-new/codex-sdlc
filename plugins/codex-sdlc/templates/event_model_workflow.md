# Workflow Title

## Summary

Describe the workflow boundary, actor intent, and what this workflow covers.

## Working Definitions

- Define key business terms used in commands, events, and views.

## Commands

### `CommandName`

- Actor:
- Purpose:
- Inputs:
- Preconditions:
- Errors:

## Events

### `EventName`

- Meaning:
- Attributes:
- Attribute sources:

## Queries

### `OperatorFacingQuery`

- Purpose:
- Inputs:
- Returns:

### `InternalInspectionQuery`

- Purpose:
- Inputs:
- Returns:
- Surface: internal/supporting only

## Views / Projections

### `OperatorFacingView`

- Purpose:
- Attributes:
- Source:

### `SupportingProjection`

- Purpose:
- Attributes:
- Source:
- Surface: internal/supporting only

## Flow Narratives

### Flow name

Describe the happy path and relevant negative-path checkpoints in plain language.

## Information Completeness Check

### Event attribute sources

- `EventName.AttributeName`: source

### Read-model attribute sources

- `ViewName.AttributeName`: source

### Absence and derivation rules

- State any explicit absence cases.
- State any query-time derivations.

## Command-to-Event Mapping

- `CommandName` -> `EventName`

## Query-to-View Mapping

- `QueryName` -> `ViewName`

## CLI Examples

### Command CLI examples

```text
$ app command-name --example
```

### View CLI examples

```text
$ app show-view --example
```

## Pattern Slices

### State Change slices

#### Slice name

Intent:

CLI example:

```text
$ app command-name --example
```

Gherkin:

```gherkin
Given [EVENTS]
When [COMMAND]
Then [EVENTS | ERROR]
```

Completeness focus:

- List the specific attribute sources or preconditions this slice proves.

### State View slices

#### Slice name

Intent:

CLI example:

```text
$ app show-view --example
```

Gherkin:

```gherkin
Given [EVENTS]
Then [PROJECTION]
```

Completeness focus:

- List the specific projection fields and source traces this slice proves.

### Automation slices

If this workflow has no standalone automation pattern, say so explicitly here.

#### Slice name

Intent:

CLI example:

```text
$ app automation-example
```

Gherkin:

```gherkin
Given [EVENTS | TIMER]
When [AUTOMATION]
Then [COMMAND -> EVENTS]
```

Completeness focus:

- List the trigger, view/condition source, and resulting command/event chain.

### Translation slices

If this workflow has no translation pattern, say so explicitly here.

#### Slice name

Intent:

CLI example:

```text
$ app translation-example
```

Gherkin:

```gherkin
Given [EXTERNAL EVENT]
When [TRANSLATION]
Then [INTERNAL COMMAND -> EVENTS]
```

Completeness focus:

- List the external input, translation rule, and resulting internal command/event chain.

## Notes

- Record scope boundaries, deferred workflows, or explicit out-of-scope items.
