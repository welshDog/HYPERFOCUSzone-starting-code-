#!/usr/bin/env python3
"""HyperFocus Z0ne - Starting Code Session Start Hook.

Writes a .focus_session_start marker and checks core repo files exist.
Exits 0 on pass, 1 on hard failure.
"""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSION_FILE = ROOT / ".focus_session_start"


def main() -> int:
    now = datetime.now()
    print("\n[SESSION START] HyperFocus Z0ne -- Starting Code")
    print("-" * 40)
    print("   Time    : " + now.strftime("%Y-%m-%d %H:%M:%S"))

    SESSION_FILE.write_text(now.isoformat())

    readme_ok = (ROOT / "README.md").exists()
    reqs_ok = (ROOT / "requirements.txt").exists()
    core_ok = (ROOT / "core").is_dir()
    public_ok = (ROOT / "public").is_dir()

    print("   README.md      : " + ("PASS found" if readme_ok else "FAIL missing"))
    print("   requirements.txt: " + ("PASS found" if reqs_ok else "WARN missing"))
    print("   core/           : " + ("PASS found" if core_ok else "WARN missing"))
    print("   public/         : " + ("PASS found" if public_ok else "WARN missing"))
    print()

    if not readme_ok:
        print("FAIL  Session start FAILED -- README.md not found.\n")
        return 1

    print("PASS  Starting Code session started. BROski forever! Let's build!\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
