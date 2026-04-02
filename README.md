# codex-sdlc

Codex-first SDLC plugin for solo-heavy, trunk-based development.

This repo packages a local Codex plugin that favors:

- direct work on trunk or a trunk branch
- linear history and no force-push
- skills as the main workflow contract
- AGENTS.md as the durable repo-level routing layer
- optional delegation only when explicitly useful

The plugin is in `plugins/codex-sdlc/` and is exposed through the repo marketplace in `.agents/plugins/marketplace.json`.

## Included

- Codex plugin manifest and marketplace entry
- ten workflow skills
- Bash-scoped lifecycle hooks for startup, guardrails, and publish checks
- helper scripts for hook state and AGENTS.md bootstrapping
- optional custom-agent templates

## Workflow defaults

- Solo-first
- Direct-to-trunk
- No PR flow by default
- No force-push
- Verify before commit or push

## Notes

Codex hooks can currently observe Bash lifecycle events. They do not provide the same always-on orchestration surface as Claude-specific subagent hooks, so this plugin keeps mechanical enforcement focused on:

- blocking destructive or out-of-policy git commands
- warning or blocking publish steps that skipped checks
- injecting concise startup and policy context into sessions

## Skill Inventory

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
