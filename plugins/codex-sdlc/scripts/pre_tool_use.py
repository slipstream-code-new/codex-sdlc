#!/usr/bin/env python3
import sys
from hook_lib import command_text, first_forbidden_reason, load_payload, load_turn_state, save_turn_state


def main() -> None:
    payload = load_payload()
    command = command_text(payload)
    turn_id = payload["turn_id"]
    reason = first_forbidden_reason(command)
    if reason:
        state = load_turn_state(turn_id)
        state["blocked_commands"].append(command)
        save_turn_state(turn_id, state)
        sys.stderr.write(reason + "\n")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
