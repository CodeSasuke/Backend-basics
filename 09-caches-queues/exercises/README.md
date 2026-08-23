# Exercises: Caches And Queues

[Expected observations](expected.md) | [Levels](levels.md)

[Previous: Transactions](../../08-transactions/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Levels](levels.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Failure And Retries](../../10-failure-retries/exercises/README.md)

- Add expiration to a cache and observe stale reads.
- Deliver one job twice and make the result durable only once.
- Stop a consumer midway, restart it, and inspect repeated work.

## Task

Build an asynchronous report job with states, retries, duplicate protection, and failed-job inspection. Start with an in-process queue and document the external-queue changes.

## Exit Check

Explain at-least-once delivery and why consumers need idempotency.