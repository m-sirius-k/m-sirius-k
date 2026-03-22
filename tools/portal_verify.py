import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_README_HEADINGS = [
    "# Architecture",
    "# Repositories",
    "# Research Workflow",
    "# Technical Backbone",
    "# Verification Architecture",
    "# Quick Demo",
]

REQUIRED_ARENA_HEADINGS = [
    "# MoCKA Demo Arena",
    "# Demo 1 Browser Demo",
    "# Demo 2 Break Test",
    "# Demo 3 Repair Test",
    "# Demo 4 Local Optional Reproduction",
    "# Verification Domains",
]

def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(str(path))
    return path.read_text(encoding="utf-8", errors="replace")

def check_headings(doc_name: str, text: str, required: list[str]) -> list[str]:
    missing = []
    for h in required:
        if h not in text:
            missing.append(h)
    if missing:
        print(f"FAIL: {doc_name} missing headings:")
        for m in missing:
            print(f"- {m}")
    else:
        print(f"PASS: {doc_name} required headings present")
    return missing

def main() -> int:
    readme_path = ROOT / "README.md"
    arena_path = ROOT / "DEMO_ARENA.md"

    try:
        readme = read_text(readme_path)
    except FileNotFoundError:
        print(f"FAIL: README not found: {readme_path}")
        return 1

    try:
        arena = read_text(arena_path)
    except FileNotFoundError:
        print(f"FAIL: DEMO_ARENA not found: {arena_path}")
        return 1

    missing_readme = check_headings("README.md", readme, REQUIRED_README_HEADINGS)
    missing_arena = check_headings("DEMO_ARENA.md", arena, REQUIRED_ARENA_HEADINGS)

    if missing_readme or missing_arena:
        print("RESULT: FAIL")
        return 1

    print("RESULT: PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())

