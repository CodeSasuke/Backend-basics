# Exercises: Concurrency

[Expected observations](expected.md) | [Levels](levels.md)

[Previous: Failure And Retries](../../10-failure-retries/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Observability](../../12-observability/exercises/README.md)

- Compare sequential and bounded concurrent I/O-like jobs.
- Demonstrate a shared-counter race, then protect the invariant.
- Make a producer faster than workers and observe backpressure.

## Task

Implement a bounded job runner with cancellation, timeout, result collection, and failure reporting. Measure throughput and latency at different limits.

## Exit Check

Name the shared state, owner, limit, and failure mode in your runner.