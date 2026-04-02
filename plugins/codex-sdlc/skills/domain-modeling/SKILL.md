---
name: domain-modeling
description: Use this skill for semantic types, primitive obsession, parse-don't-validate, invalid-state prevention, and domain-focused review. It is also the domain review lens for the TDD cycle.
---

# Domain Modeling

Use this skill when the code should express the business domain more precisely.

## Core principles

- Replace domain-significant primitives with semantic types.
- Parse at the boundary, then trust the type inside the system.
- Make invalid states unrepresentable where the type system can do the work.
- Treat stateful booleans as a smell when an enum is the real model.

## What to look for

- `String`, `int`, `number`, or `bool` carrying domain meaning
- identifiers without newtype wrappers
- contradictory field combinations that should be encoded as variants
- validation logic buried inside business logic instead of constructors or parsers
- swappable parameters that should be distinct semantic types

## Review workflow

1. Identify the domain concepts hidden inside primitives.
2. Propose the smallest semantic type that captures the business meaning.
3. Move validation to the type construction boundary.
4. Re-check the model for impossible combinations and leaked validation.

## Codex-specific guidance

- Use this skill during review and during TDD domain checkpoints.
- Push back on weak domain types even if the code "works."
- If the user deliberately accepts a weaker model for speed, say so explicitly and record the tradeoff.

## Done when

- domain concepts are named in the type system
- invalid combinations are harder or impossible to construct
- business logic stops repeating low-level validation
