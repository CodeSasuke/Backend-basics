# 11. Concurrency And Parallelism

[Previous: Failure And Retries](../../10-failure-retries/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Observability](../../12-observability/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

Concurrency manages multiple in-progress tasks; parallelism executes work simultaneously. Both can improve throughput and can create races, contention, starvation, and exhaustion.

```text
concurrency: tasks interleave while waiting
parallelism: tasks run at the same time
```

Ask: Is the workload CPU-bound or I/O-bound? What state is shared? What happens when producers outpace consumers? Why must concurrency be bounded?

## Exit Check

Choose a concurrency model for an I/O workload and a CPU workload, with reasons.

## Complete Lesson

Concurrency manages multiple in-progress tasks; parallelism executes work simultaneously. Simultaneous work can improve throughput but can create races and exhaust resources.

A bounded worker pool processes independent I/O jobs while refusing unlimited work, creating backpressure. Ask whether work is CPU-bound or I/O-bound, what state is shared, and who owns it.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
