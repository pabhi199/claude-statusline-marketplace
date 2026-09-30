#!/usr/bin/env python3
import sys
import json
import os
import subprocess

RESET = "\033[0m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
DIM = "\033[2m"


def get_git_branch(cwd):
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=2,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def format_duration(ms):
    seconds = ms / 1000
    if seconds < 60:
        return f"{seconds:.0f}s"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.1f}m"
    return f"{minutes / 60:.1f}h"


def main():
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        print("statusline: invalid input")
        return

    model = data.get("model", {}).get("display_name", "unknown")

    cwd = data.get("cwd") or data.get("workspace", {}).get("current_dir", "")
    short_cwd = cwd.replace(os.path.expanduser("~"), "~") if cwd else ""

    branch = get_git_branch(cwd) if cwd else None

    cost = data.get("cost", {})
    total_cost = cost.get("total_cost_usd")
    duration_ms = cost.get("total_duration_ms")

    parts = [f"{CYAN}{model}{RESET}"]

    if short_cwd:
        parts.append(f"{DIM}{short_cwd}{RESET}")

    if branch:
        parts.append(f"{GREEN}git:{branch}{RESET}")

    if total_cost is not None:
        parts.append(f"{YELLOW}${total_cost:.4f}{RESET}")

    if duration_ms is not None:
        parts.append(f"{MAGENTA}{format_duration(duration_ms)}{RESET}")

    print(" | ".join(parts))


if __name__ == "__main__":
    main()
