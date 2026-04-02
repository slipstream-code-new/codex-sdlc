---
name: repo-setup
description: Set up repository policy and local Codex configuration for trunk-based development. Use when the user wants GitHub branch-protection guidance, `.codex/config.toml` direction, or a repo-local operating model aligned with direct trunk commits.
---

# Repo Setup

This skill sets the repository-level rules around Codex usage.

## Defaults

- Protect `main` or the chosen trunk branch.
- Require linear history.
- Disable force-push.
- Avoid a required-PR workflow unless the user explicitly wants one.

## GitHub guidance

Recommend:

- branch protection on trunk
- linear history required
- force-push blocked
- optional required status checks only for checks that are fast and reliable enough to stay on the main path

## Local Codex guidance

- Keep the repo trusted in `.codex/config.toml` when appropriate.
- Prefer repo-local `AGENTS.md` and repo-local plugin usage over home-global instruction sprawl.
- Keep custom agents optional and task-specific.

## Deliverables

- A short branch-protection checklist
- Any needed repo-local Codex config notes
- A clear statement of what is enforced by GitHub versus what is enforced by skills and hooks
