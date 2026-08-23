# Exercises: Processes And State

[Expected observations](expected.md) | [Levels](levels.md)

[Theory](../theory/README.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: OS Resources](../../02-os-resources/exercises/README.md)

## Experiment 1: Predict The Transition

Before running the program, write the balance after these commands: `deposit 10`, `withdraw 4`, `withdraw 9`.

## Experiment 2: Break Restartability

Run the starter, create state, stop it, and run it again. Record what was lost. Decide which facts should be durable later.

## Task

Extend the ledger with `balance`, `deposit`, `withdraw`, and `reset`. Reject negative amounts and overdrafts. Write at least five tests for valid and invalid transitions.

## Evidence

Record one input, old state, output, and new state for each operation.

## Exit Check

Draw a state-transition table and describe the invariant without using Python terms.