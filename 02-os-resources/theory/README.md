# 02. Operating Systems And Resource Boundaries

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
 
## Complete Lesson

A backend shares a machine with other programs. CPU, memory, files, sockets, and child processes are finite resources and can fail independently. The operating system provides controlled boundaries: an application requests a resource, uses it, and releases it.

```text
process -> OS boundary -> CPU | memory | files | sockets
```

A worker opening a job file must close it even when parsing fails. A missing file is a startup or configuration failure, not a business-rule failure. Configuration should enter through the environment or deployment mechanism rather than being hidden in code.

Ask yourself: Who owns cleanup after an exception? What is the difference between blocked and slow? Which limit fails when input grows without bound?

Common mistakes include ignoring cleanup, treating configuration as optional, and creating unlimited workers or open files.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
