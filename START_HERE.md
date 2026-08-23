# Start Here

This course teaches backend engineering from first principles. You will use Python to run experiments, but the ideas are about systems, not Python syntax.

## Before Module 1

You should be able to:

- create and call a Python function
- use a terminal to run a file
- read a basic error message
- edit a text file

You do not need a web framework or database experience.

## Setup

From this repository root:

```text
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python3 scripts/validate_course.py
python3 -m unittest discover -s tests
```

## Your First Study Session

1. Open [Module 1 theory](01-processes-and-state/theory/README.md).
2. Answer the Socratic questions in the notes section at the end of [Module 1 theory](01-processes-and-state/theory/README.md).
3. Read [Module 1 exercises](01-processes-and-state/exercises/README.md).
4. Write a prediction in the [experiment log](01-processes-and-state/exercises/experiment.md).
5. Run the reference program:

   ```text
   printf "deposit 10\nbalance\nquit\n" | python3 01-processes-and-state/code/main.py
   ```

6. Implement the task in [exercise.py](01-processes-and-state/code/exercise.py).
7. Run the learner checks:

   ```text
   python3 -m unittest 01-processes-and-state/code/test_exercise.py
   ```

8. Record evidence and the exit-check answer in [answers](01-processes-and-state/exercises/answers.md).
9. Update [PROGRESS.md](PROGRESS.md).

## The Rule

Predict first, run second, explain third. When your prediction is wrong, that is the lesson.

## Continue

Return to the [ROADMAP.md](ROADMAP.md) after Module 1 and open the next theory page.
