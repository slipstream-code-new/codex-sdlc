#!/usr/bin/env python3
from hook_lib import hook_json, load_payload


def main() -> None:
    payload = load_payload()
    prompt = payload.get("prompt", "").lower()

    if "pull request" in prompt or "pr " in prompt or "prs" in prompt:
        print(
            hook_json(
                "UserPromptSubmit",
                additional_context=(
                    "Repo policy reminder: this Codex SDLC plugin defaults to trunk-based development without PRs. Only shift to a PR workflow if the user is explicitly overriding that default for this task."
                ),
            )
        )
        return

    if "force push" in prompt or "--force" in prompt:
        print(
            hook_json(
                "UserPromptSubmit",
                additional_context=(
                    "Repo policy reminder: force-push is out of policy here. Prefer local rebase, linear history, and a normal push."
                ),
            )
        )
        return


if __name__ == "__main__":
    main()
