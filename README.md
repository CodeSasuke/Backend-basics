# Backend Basics Lab

This repository is a hands-on companion to [ROADMAP.md](ROADMAP.md). Python is used for experiments; the explanations, models, contracts, and trade-offs are language-independent.

New here? Start with [START_HERE.md](START_HERE.md).

Use [PROGRESS.md](PROGRESS.md) to track completion, [TEMPLATE_GUIDE.md](TEMPLATE_GUIDE.md) to understand the learner files, and [ROADMAP.md](ROADMAP.md) as the navigation hub.

Read [SOCRATIC_METHOD.md](SOCRATIC_METHOD.md) to understand the dialogue-based teaching approach.

## Learning Loop

For each module, work in this order:

1. Read `theory/README.md` and understand its model and vocabulary.
2. Read `code/main.py` without modifying or running it; identify the important behavior.
3. Open `exercises/README.md` and make a prediction before running code.
4. Record and run the experiment in `exercises/experiment.md`.
5. Answer the Socratic questions in the theory notes using the code and observed evidence.
6. Implement the task in `code/exercise.py`.
7. Run the learner test file when the module provides one.
8. Record the final evidence and explain the idea without Python-specific vocabulary.

Every module has:

```text
module/
  theory/README.md       complete lesson followed by your notes
  exercises/README.md   experiments, tasks, exit checks
  exercises/hints.md    optional hints
  exercises/levels.md   four levels of practice
  exercises/experiment.md prediction and evidence
  exercises/answers.md   your answers and review
  code/main.py           Python starting point
  code/exercise.py       your exercise implementation
  code/test_exercise.py  learner checks when provided
  code/solution.py       optional solution workspace
```

## Setup

```text
python3 -m venv .venv
source .venv/bin/activate
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
