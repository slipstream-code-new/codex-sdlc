---
name: bootstrap-codex-sdlc
description: Bootstrap a repository for Codex-first, trunk-based development. Use when the user asks to set up AGENTS.md, Codex workflow guidance, or repo-local SDLC defaults without centering Claude-specific conventions.
---

# Bootstrap Codex SDLC

Use this skill to establish a Codex-native workflow baseline for a repository.

## Goals

- Keep `AGENTS.md` concise and current.
- Make the repo's build, test, and ship commands obvious.
- Encode the workflow defaults: solo-first, direct-to-trunk, no force-push, no PR-first flow.

## Workflow

1. Inspect the repo before asking questions. Detect the primary language, build command, test command, and lint or check command.
2. Read any existing `AGENTS.md` before writing new guidance.
3. Prefer a single managed block rather than spreading instructions across many files.
4. Use `plugins/codex-sdlc/scripts/render_agents_md.py` for a starter block when useful, then tailor it to the repo.
5. Keep deep process detail in this plugin's skills, not in `AGENTS.md`.

## Required defaults

- Default to one main Codex agent unless the user explicitly wants delegation.
- Prefer direct work toward trunk.
- Run relevant checks before commit or push.
- Do not normalize around PRs, review queues, or force-push.

## Done when

- The repo has a concise `AGENTS.md` routing block.
- Build, test, lint, and workflow rules are easy to find.
- The instructions match Codex rather than Claude-specific setup.
