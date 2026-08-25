# 01. Processes And State

[Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: OS Resources](../../02-os-resources/theory/README.md)

## Lesson Orientation

This lesson establishes the distinction between a running process, the state it holds, and effects that outlive the computation. Read the theory and inspect the starter code before running it.

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
 
## Complete Lesson

A backend handles many inputs over time. A single calculation is easy; remembering what happened and making the next decision correctly is the real problem. A program is instructions, a process is those instructions running, and state is information that changes future results.

```text
input + old state -> rules -> output + new state
                                      |
                                      +-> file, database, or network effect
```

For a ledger with balance `10`, `withdraw 4` produces output `6` and new state `6`. `withdraw 20` must produce an error and preserve state `10`. The invariant is the rule that must always remain true.

Ask yourself: What disappears when the process stops? Which operations are pure transformations? Why should invalid input leave state unchanged?

Common mistakes include confusing a variable with durable storage, allowing invalid transitions to mutate state, and testing only the happy path.

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Identify the state, the transition function, the input boundary, and the output boundary. Before executing the program, record your predictions and observations in the [experiment log](../exercises/experiment.md).

Run the experiment only after making your predictions. Then answer the Socratic questions below using both the code and the evidence you recorded.

## Dialogue Check

**You:** What should happen next?

**Guide:** Use the model above to predict the output and the state change before running the code.

**You:** How will I know if I am right?

**Guide:** Run the experiment, compare the result, and explain any difference in your notes.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- The process remembers the current `balance` between commands.
- The in-memory balance and transaction history disappear when the process restarts; the balance resets to `0`.
- `apply_command(balance, command)` is a pure transformation because it returns the next balance and output without external side effects.
- The balance must never become negative. Invalid commands and rejected withdrawals must leave it unchanged.

### Exit-check answer
