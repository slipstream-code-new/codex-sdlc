#!/usr/bin/env python3
import argparse
from pathlib import Path


LANGUAGE_MARKERS = {
    "Cargo.toml": ("Rust", "`cargo build`", "`cargo test`", "`cargo clippy --all-targets --all-features`"),
    "package.json": ("JavaScript/TypeScript", "`npm run build`", "`npm test`", "`npm run lint`"),
    "pyproject.toml": ("Python", "`python -m build`", "`pytest`", "`ruff check .`"),
    "go.mod": ("Go", "`go build ./...`", "`go test ./...`", "`go vet ./...`"),
}


def detect_repo_shape(root: Path) -> tuple[str, str, str, str]:
    for marker, result in LANGUAGE_MARKERS.items():
        if (root / marker).exists():
            return result
    return (
        "Unknown",
        "[fill in build command]",
        "[fill in test command]",
        "[fill in lint/check command]",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a starter AGENTS.md block for Codex SDLC.")
    parser.add_argument("repo", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    language, build_cmd, test_cmd, lint_cmd = detect_repo_shape(root)
    print(
        f"""<!-- BEGIN MANAGED: codex-sdlc -->
## Build And Test

- Language: {language}
- Build: {build_cmd}
- Test: {test_cmd}
- Lint/check: {lint_cmd}

## Workflow

- Default to solo-first execution. Only delegate when the user explicitly asks for subagents or when a bounded sidecar task is clearly worthwhile.
- Work directly toward trunk. Keep history linear and never use force-push.
- Run the most relevant checks before commit or push.
- Keep AGENTS.md concise. Put deep process detail in skills or referenced docs.
<!-- END MANAGED: codex-sdlc -->"""
    )


if __name__ == "__main__":
    main()
