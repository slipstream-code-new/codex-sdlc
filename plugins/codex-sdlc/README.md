# codex-sdlc plugin

Local Codex plugin for trunk-based software delivery without a PR-first workflow.

## Components

- `skills/`: Codex-native workflow skills
- `hooks.json`: lifecycle hook wiring
- `scripts/`: hook implementations and helper utilities
- `templates/agents/`: optional project-scoped custom-agent templates
- `templates/`: shared document and workflow templates used by plugin skills
- `assets/`: plugin card assets

## Design

The plugin keeps the portable strengths from `agent-skills` and the deterministic strengths from `claudez`, but adapts them to Codex:

- skills and AGENTS.md are the primary control plane
- hooks enforce only what Codex can mechanically observe well
- delegation is explicit and bounded, not ambient
- publish defaults are direct-to-trunk, not PR-centric

## Included Skills

- `bootstrap-codex-sdlc`
- `trunk-ship`
- `codex-review`
- `bounded-delegation`
- `session-retrospective`
- `repo-setup`
- `architecture-decisions`
- `domain-modeling`
- `event-modeling`
- `tdd`

## Shared templates

- `templates/event_model_workflow.md`: canonical workflow-doc scaffold for the
  `event-modeling` skill
