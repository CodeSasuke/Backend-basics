# 11. Concurrency And Parallelism

[Previous: Failure And Retries](../../10-failure-retries/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Observability](../../12-observability/theory/README.md)

## Lesson Orientation

This lesson distinguishes concurrency from parallelism and examines the races and resource exhaustion that simultaneous work can create. Read the theory and inspect the starter code before running it.

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

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Identify the shared state, the worker limit, the scheduling model, and the point where backpressure should occur. Before executing the program, record your predictions and observations in the [experiment log](../exercises/experiment.md).

Run the experiment only after making your predictions. Then answer the Socratic questions below using both the code and the evidence you recorded.

## Dialogue Check

**You:** Why run these tasks together?

**Guide:** Independent work can overlap, but shared state and finite resources need ownership and limits.

**You:** What should I measure?

**Guide:** Compare throughput, latency, failures, and queued work as the worker limit changes.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
