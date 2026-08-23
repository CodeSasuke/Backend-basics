"""Validate the expected course structure and Markdown links."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
MODULES = sorted(path for path in ROOT.iterdir() if path.is_dir() and re.match(r"^\d{2}-", path.name))
REQUIRED = (
    "theory/README.md",
    "exercises/README.md",
    "exercises/experiment.md",
    "exercises/answers.md",
    "exercises/hints.md",
    "exercises/levels.md",
    "exercises/expected.md",
    "code/main.py",
    "code/exercise.py",
    "code/solution.py",
)


def main() -> int:
    missing = []
    for module in MODULES:
        for relative_path in REQUIRED:
            if not (module / relative_path).exists():
                missing.append(f"{module.name}/{relative_path}")

        theory = (module / "theory/README.md").read_text()
        if "## Dialogue Check" not in theory:
            missing.append(f"{module.name}/theory/README.md: dialogue check")
        if "## My Notes" not in theory:
            missing.append(f"{module.name}/theory/README.md: learner notes")

    links = re.findall(r"\]\(([^)#]+)\)", (ROOT / "ROADMAP.md").read_text())
    broken_links = [link for link in links if not (ROOT / link).exists()]
    if missing or broken_links:
        for item in missing:
            print(f"missing file: {item}")
        for item in broken_links:
            print(f"broken roadmap link: {item}")
        return 1

    print(f"validated {len(MODULES)} modules and {len(links)} roadmap links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
