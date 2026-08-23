# 10. Errors, Timeouts And Retries

[Detailed lesson](lesson.md)

[Previous: Caches And Queues](../../09-caches-queues/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Concurrency](../../11-concurrency/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

A timeout means the caller lacks an answer; it does not prove an operation did not happen. Safe recovery needs deadlines, bounded retries, backoff, idempotency, and a clear fallback.

```text
caller -- deadline --> dependency
  | success | timeout -> bounded retry -> fallback or clear failure
```

Ask: Which failures are retryable? When does a retry duplicate a side effect? How do we prevent retries from multiplying load?

## Exit Check

Explain the difference between failed work and unknown outcome.