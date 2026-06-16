#!/usr/bin/env python3
"""HyperFocus Z0ne - Starting Code Env Guard.

Starting code template repo -- no required env vars.
Confirms we are in the correct repo root and passes.
Always exits 0.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    print("\n[ENV GUARD] HyperFocus Z0ne -- Starting Code")
    print("-" * 40)
    print("   Template/starter repo -- no required env vars.")
    print()

    marker = ROOT / "requirements.txt"
    if not marker.exists():
        print("WARN  requirements.txt not found -- may be wrong directory")
    else:
        print("   PASS  repo root confirmed (requirements.txt present)")

    print()
    print("PASS  Env guard passed (template repo -- no secrets required).\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
