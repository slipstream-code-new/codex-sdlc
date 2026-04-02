#!/usr/bin/env python3
from hook_lib import load_payload, load_turn_state


def main() -> None:
    payload = load_payload()
    turn_id = payload["turn_id"]
    state = load_turn_state(turn_id)

    if state["publish_commands"] and not state["checks_ran"]:
        print('{"decision":"block","reason":"Before finishing, run the most relevant tests or checks for the changes you committed or pushed in this turn, then continue with the results."}')


if __name__ == "__main__":
    main()
