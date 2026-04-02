#!/usr/bin/env python3
from hook_lib import branch_name, git_status_summary, hook_json, load_payload, repo_root, upstream_name


def main() -> None:
    payload = load_payload()
    cwd = payload["cwd"]
    repo = repo_root(cwd)
    if repo is None:
        print(
            hook_json(
                "SessionStart",
                additional_context=(
                    "Codex SDLC defaults: solo-first, direct-to-trunk, no force-push, and no PR flow unless the user explicitly asks for it."
                ),
            )
        )
        return

    branch = branch_name(cwd) or "(detached)"
    upstream = upstream_name(cwd) or "(no upstream)"
    status = git_status_summary(cwd) or "(clean)"
    print(
        hook_json(
            "SessionStart",
            additional_context=(
                "Codex SDLC workflow active. Default to solo-first execution, direct trunk integration, linear history, and no force-push. "
                f"Repo root: {repo}. Branch: {branch}. Upstream: {upstream}. Git status:\n{status}"
            ),
        )
    )


if __name__ == "__main__":
    main()
