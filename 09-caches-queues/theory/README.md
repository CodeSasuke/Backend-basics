# 09. Caches, Queues And Derived State

[Previous: Transactions](../../08-transactions/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Failure And Retries](../../10-failure-retries/theory/README.md)

A cache improves speed but may be stale. A queue separates producers and consumers, introducing delay, duplication, ordering, acknowledgement, and retry questions.

```text
producer -> queue -> consumer -> source of truth
request -> cache hit | miss -> source -> cache fill
```

Ask: What is the cost of stale data? What if a consumer crashes after doing work but before acknowledging it? How can derived state be rebuilt?

## Exit Check

Identify the source of truth and the repair path for every derived value.