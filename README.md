# Backend Basics Lab

This repository is a hands-on companion to [ROADMAP.md](ROADMAP.md). Python is used for experiments; the explanations, models, contracts, and trade-offs are language-independent.

Use [PROGRESS.md](PROGRESS.md) to track completion, [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md) to understand the learner files, and [ROADMAP.md](ROADMAP.md) as the navigation hub.

## Learning Loop

For each module, work in this order:

1. Read `theory/README.md` and answer its questions on paper.
2. Open `exercises/README.md` and make a prediction before running code.
3. Run and modify `code/main.py`.
4. Write tests for the invariant or contract you discovered.
5. Record evidence and explain the idea without Python-specific vocabulary.

Every module has:

```text
module/
  theory/README.md       concepts, visuals, Socratic prompts
  exercises/README.md   experiments, tasks, exit checks
  code/main.py           Python starting point
```

## Setup

```text
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pytest
```

Run a starter:

```text
python 01-processes-and-state/code/main.py
```

Validate the course structure and links:

```text
python scripts/validate_course.py
```

## Progress Rule

Do not mark a module complete because the starter runs. Mark it complete when you can state the invariant, predict a failure, produce evidence, and explain the design trade-off.

## Project Thread

The modules gradually build one notes and jobs platform. Preserve the earlier behavior as later modules add persistence, HTTP, security, background work, observability, and deployment thinking.
