# Lesson: Programs, Processes, And State

## Start With The Problem
A backend must handle many inputs over time. A single calculation is easy; remembering what happened and making the next decision correctly is the real problem.

## Core Model
A program is instructions. A process is those instructions running with memory and a lifecycle. State is information that changes future results. A side effect changes something outside the current calculation.

```text
input + old state -> rules -> output + new state
                                      |
                                      +-> file, database, or network effect
```

## Worked Example
For a ledger with balance `10`, `withdraw 4` produces output `6` and new state `6`. `withdraw 20` must produce an error and preserve state `10`.

## Think About It
- What disappears when the process stops?
- Which rule must never be broken?
- How can a pure state-transition function make debugging easier?

## Common Mistakes
Confusing a variable with durable storage, allowing invalid transitions to mutate state, and testing only the happy path.

## Mastery Check
Describe the same state machine without using Python terms. Then identify its inputs, outputs, invariant, and side effects.