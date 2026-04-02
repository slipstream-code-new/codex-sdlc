#!/usr/bin/env python3
from hook_lib import hook_json, load_payload


def main() -> None:
    payload = load_payload()
    prompt = payload.get("prompt", "").lower()
    event_model_terms = (
        "event model",
        "event modeling",
        "workflow model",
        "workflow modeling",
        "commands",
        "events",
        "views",
        "cqrs",
    )

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

    if any(term in prompt for term in event_model_terms):
        print(
            hook_json(
                "UserPromptSubmit",
                additional_context=(
                    "Event-modeling reminder: use the `event-modeling` skill, "
                    "start from the shared workflow template, classify slices by "
                    "pattern, include concrete command and view CLI examples, "
                    "and run an information-completeness check before claiming the workflow is done."
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
