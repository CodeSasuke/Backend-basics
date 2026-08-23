# Socratic Method

## What This Is

The repository uses a Socratic teaching method. Instead of only giving definitions, each module asks questions that make you predict, investigate, and explain backend behavior.

The current Guide is a **static teaching format**, not an AI agent. The dialogue is written into the theory files for you to follow while learning.

```text
question -> prediction -> experiment -> observation -> explanation
```

## How The Guide Works

Each theory file contains a `Dialogue Check` section with two voices:

```text
You: What should happen next?
Guide: Use the model above to make a prediction.
You: How do I know if I am right?
Guide: Run the experiment and compare the result.
```

The Guide is a thinking prompt. It does not automatically read your answers, execute your code, inspect your tests, or adapt the lesson.

## Learner Workflow

For every module:

1. Read the theory and visual model.
2. Read the question from the Guide.
3. Answer it before looking at the expected observation.
4. Write your prediction in `exercises/experiment.md`.
5. Run `code/main.py`.
6. Compare the result with your prediction.
7. Record evidence and changed assumptions.
8. Implement the task in `code/exercise.py`.
9. Run the learner tests when available.
10. Use the exit check to explain the idea without relying on Python vocabulary.

## The Five Questions

Use these questions whenever you study a backend concept:

### 1. What problem exists?

What becomes difficult, incorrect, slow, or unsafe without this concept?

### 2. What is the model?

What are the inputs, state, rules, outputs, boundaries, and side effects?

### 3. What do I predict?

Before running code, what do you expect to happen and why?

### 4. What failed?

Break the code deliberately. What failure occurred, and what evidence shows its cause?

### 5. What guarantee exists?

What can a caller, operator, or future developer rely on? What guarantee is intentionally not provided?

## Example: State

```text
You: What happens if I withdraw more than the balance?
Guide: State the invariant before running the command.
You: The balance must never become negative.
Guide: Now run the command and inspect both the output and the state.
You: The command should fail and preserve the previous balance.
```

The important result is not memorizing a Python `if` statement. It is learning the language-independent rule:

> An invalid state transition must not change the existing valid state.

## What The Guide Is Not

The current repository does not provide a dynamic tutor. It does not:

- generate follow-up questions from your answers
- grade your explanations automatically
- inspect your implementation and suggest targeted hints
- decide whether you have mastered a module
- track understanding beyond the files you update

Use the exercise levels, tests, expected observations, and `PROGRESS.md` to create that feedback loop manually.

## What A Future AI Guide Could Do

An actual AI guide could read your learner files and:

- ask adaptive follow-up questions
- give a smaller hint when you are stuck
- review code against the stated invariant
- inspect failing tests and explain the evidence
- recommend repeating or advancing a level
- update progress after reviewing your work

That would require an AI integration such as a VS Code workflow, command-line tutor, or local application. It is separate from the current Markdown course materials.

## Rule Of Practice

Predict first. Run second. Explain third. When your prediction is wrong, do not hide the result; use it to improve the model.

## Navigation

[Roadmap](ROADMAP.md) | [Start Here](START_HERE.md) | [Progress](PROGRESS.md) | [Template Guide](TEMPLATE_GUIDE.md)
