#!/usr/bin/env python3
import json
import os
import re
import subprocess
import sys
from pathlib import Path


PLUGIN_ROOT = Path("/home/jwilger/projects/codex-sdlc/plugins/codex-sdlc")
STATE_ROOT = Path("/home/jwilger/projects/codex-sdlc/.codex-sdlc/runtime")

CHECK_COMMAND_PATTERNS = [
    r"\bcargo (test|nextest|clippy)\b",
    r"\bnpm (test|run test|run lint|run check)\b",
    r"\bpnpm (test|run test|run lint|run check)\b",
    r"\byarn (test|lint|check)\b",
    r"\bpytest\b",
    r"\bgo test\b",
    r"\bjust (test|check|lint)\b",
    r"\bmake (test|check|lint)\b",
    r"\bnix flake check\b",
    r"\buv run pytest\b",
]

PUBLISH_COMMAND_PATTERNS = [
    r"\bgit commit\b",
    r"\bgit push\b",
]

FORBIDDEN_COMMAND_PATTERNS = [
    (r"\bgit push\b.*\s--force(?:-with-lease)?\b", "Force-push is disabled by the Codex SDLC workflow. Rebase locally and push linear history instead."),
    (r"\bgit reset\s+--hard\b", "git reset --hard is blocked by the Codex SDLC workflow. Use targeted, reversible commands instead."),
    (r"\bgh pr create\b", "This workflow defaults to direct trunk integration. Do not open a PR unless the user explicitly overrides that policy."),
    (r"\bgh pr\b", "This workflow is not PR-first. Stay on the trunk-based path unless the user explicitly asks for GitHub PR operations."),
]


def load_payload() -> dict:
    return json.load(sys.stdin)


def hook_json(event_name: str, *, additional_context: str | None = None, system_message: str | None = None, decision: str | None = None, reason: str | None = None, continue_processing: bool = True, stop_reason: str | None = None) -> str:
    payload: dict = {}
    if not continue_processing:
        payload["continue"] = False
        if stop_reason:
            payload["stopReason"] = stop_reason
    if system_message:
        payload["systemMessage"] = system_message
    if decision:
        payload["decision"] = decision
    if reason:
        payload["reason"] = reason
    hook_specific = {"hookEventName": event_name}
    if additional_context:
        hook_specific["additionalContext"] = additional_context
    if hook_specific:
        payload["hookSpecificOutput"] = hook_specific
    return json.dumps(payload)


def command_text(payload: dict) -> str:
    return str(payload.get("tool_input", {}).get("command", "")).strip()


def turn_state_path(turn_id: str) -> Path:
    return STATE_ROOT / "turns" / f"{turn_id}.json"


def ensure_state_root() -> None:
    STATE_ROOT.mkdir(parents=True, exist_ok=True)
    (STATE_ROOT / "turns").mkdir(parents=True, exist_ok=True)


def load_turn_state(turn_id: str) -> dict:
    ensure_state_root()
    path = turn_state_path(turn_id)
    if not path.exists():
        return {
            "checks_ran": [],
            "publish_commands": [],
            "blocked_commands": [],
        }
    return json.loads(path.read_text(encoding="utf-8"))


def save_turn_state(turn_id: str, state: dict) -> None:
    ensure_state_root()
    turn_state_path(turn_id).write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


def repo_root(cwd: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    return result.stdout.strip() or None


def git_status_summary(cwd: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "status", "--short", "--branch"],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    return result.stdout.strip() or None


def branch_name(cwd: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    return result.stdout.strip() or None


def upstream_name(cwd: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    return result.stdout.strip() or None


def matches_any(patterns: list[str], command: str) -> bool:
    return any(re.search(pattern, command) for pattern in patterns)


def first_forbidden_reason(command: str) -> str | None:
    for pattern, reason in FORBIDDEN_COMMAND_PATTERNS:
        if re.search(pattern, command):
            return reason
    return None
