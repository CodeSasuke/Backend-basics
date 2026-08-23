# Lesson: Operating Systems And Resource Boundaries

## Start With The Problem
A backend shares a machine with other programs. CPU, memory, files, sockets, and child processes are finite resources and can fail independently.

## Core Model
The operating system provides controlled boundaries. An application requests a resource, uses it, and must release it. Configuration should enter at the boundary instead of being hidden in code.

```text
process -> OS boundary -> CPU | memory | files | sockets
```

## Worked Example
A worker opens a job file. If parsing fails, the file still needs to close. A missing file is a startup/configuration failure, not a mysterious business-rule failure.

## Think About It
- Who owns cleanup after an exception?
- What is the difference between blocked and slow?
- Which limit fails when input grows without bound?

## Common Mistakes
Ignoring cleanup, treating environment configuration as optional, and creating unlimited workers or open files.

## Mastery Check
Design a worker with explicit resource ownership, limits, interruption behavior, and exit codes.