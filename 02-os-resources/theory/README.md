# 02. Operating Systems And Resource Boundaries

[Detailed lesson](lesson.md)

[Previous: Processes And State](../../01-processes-and-state/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Protocols](../../03-protocols/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

## Why This Exists

A backend shares finite CPU, memory, files, sockets, and process slots with other programs. Each resource has an owner, lifetime, limit, and failure mode.

## Model

```text
application process
  | operating-system boundary
  +-- CPU
  +-- memory
  +-- files
  +-- sockets
  +-- child processes
```

Configuration enters through an environment or deployment mechanism. Resources must be acquired, used, and released deliberately.

## Socratic Questions

- What happens if a file is never closed?
- Which limit fails first when work grows?
- What is the difference between blocked and slow?
- Who owns cleanup after an error?

## Exit Check

Draw the resource boundaries around a worker and name one failure at each boundary.