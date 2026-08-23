# Lesson: Concurrency And Parallelism

## Start With The Problem
A backend often waits for many independent operations. Doing everything sequentially wastes time, but simultaneous work can race and exhaust resources.

## Core Model
Concurrency interleaves in-progress tasks. Parallelism executes work simultaneously. Shared state needs ownership or synchronization.

```text
concurrency: tasks interleave during waits
parallelism: tasks run at the same time
```

## Worked Example
A bounded worker pool can process several I/O jobs while refusing new work after its queue limit, creating backpressure instead of exhaustion.

## Think About It
- Is the workload CPU-bound or I/O-bound?
- What state is shared?
- What happens when producers are faster?

## Common Mistakes
Unbounded workers, assuming concurrency automatically improves CPU work, and ignoring cancellation.

## Mastery Check
Choose a model, limit, ownership rule, and failure behavior for three workloads.