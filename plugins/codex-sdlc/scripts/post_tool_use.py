#!/usr/bin/env python3
from hook_lib import CHECK_COMMAND_PATTERNS, PUBLISH_COMMAND_PATTERNS, command_text, hook_json, load_payload, load_turn_state, matches_any, save_turn_state


def main() -> None:
    payload = load_payload()
    turn_id = payload["turn_id"]
    command = command_text(payload)
    state = load_turn_state(turn_id)

    if matches_any(CHECK_COMMAND_PATTERNS, command):
        state["checks_ran"].append(command)

    if matches_any(PUBLISH_COMMAND_PATTERNS, command):
        state["publish_commands"].append(command)

    save_turn_state(turn_id, state)

    if command.startswith("git commit") and not state["checks_ran"]:
        print(
            hook_json(
                "PostToolUse",
                additional_context=(
                    "A commit was attempted before any tracked verification command in this turn. Run the most relevant tests or checks before considering the work ready to ship."
                ),
            )
        )
        return

    if command.startswith("git push") and not state["checks_ran"]:
        print(
            hook_json(
                "PostToolUse",
                additional_context=(
                    "A push was attempted before any tracked verification command in this turn. The Codex SDLC workflow expects checks before publishing to trunk."
                ),
            )
        )
        return


if __name__ == "__main__":
    main()
