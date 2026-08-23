# Exercises: Errors And Retries

[Previous: Caches And Queues](../../09-caches-queues/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Concurrency](../../11-concurrency/exercises/README.md)

- Measure total latency as retry delay changes.
- Add a retry budget and prove it stops.
- Classify failures as retryable, permanent, or unknown.

## Task

Create a flaky dependency. Add a deadline, bounded exponential backoff, idempotency key, and fallback. Test that dependency load stays bounded.

## Exit Check

State what the client may safely tell a user after a timeout.