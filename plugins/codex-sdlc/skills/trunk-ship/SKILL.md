---
name: trunk-ship
description: Ship changes directly through trunk-based development. Use when the user wants to review scope, commit intentionally, rebase or fast-forward if needed, and push without opening a pull request.
---

# Trunk Ship

This skill handles the publish path for a trunk-based repo.

## Rules

- Do not open a PR unless the user explicitly asks for one.
- Never force-push.
- Never stage unrelated work silently.
- Prefer a clean linear history over merge commits.

## Workflow

1. Inspect `git status -sb` and the diff before staging.
2. If the worktree is mixed, stage only explicit files.
3. Run the most relevant checks for the scope.
4. Commit intentionally with a terse, accurate message.
5. Rebase or fast-forward onto the latest trunk when needed.
6. Push normally.
7. Summarize what shipped, what checks ran, and any remaining risk.

## When blocked

- If checks fail, stop and fix the issue or ask the user how to proceed.
- If the branch diverged, rebase locally. Do not resolve divergence with force-push.
