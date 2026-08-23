# 01. Processes And State

[Detailed lesson](lesson.md)

[Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: OS Resources](../../02-os-resources/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

## Why This Exists

A backend is a running process that transforms input into output while state influences future behavior. If state is unclear, restart behavior, correctness, and bugs become mysterious.

## Model

```text
input + current state -> rules -> output + next state
                                      |
                                      +-> side effect
```

A value is data for one computation. State is data that changes what happens next. A side effect changes something outside the computation, such as a file or database.

## Socratic Questions

- What state does the process remember between two commands?
- What disappears when the process restarts?
- Which operations are pure transformations?
- Which invariant must always remain true?

## Python Lens

Use a function for a state transition and keep input/output at the boundary. This makes the rule testable without running a server.

## Exit Check

Explain the difference between value, state, and side effect using a bank ledger.