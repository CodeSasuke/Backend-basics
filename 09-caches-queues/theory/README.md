# 09. Caches, Queues And Derived State

[Previous: Transactions](../../08-transactions/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Failure And Retries](../../10-failure-retries/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

A cache improves speed but may be stale. A queue separates producers and consumers, introducing delay, duplication, ordering, acknowledgement, and retry questions.

```text
producer -> queue -> consumer -> source of truth
request -> cache hit | miss -> source -> cache fill
```

Ask: What is the cost of stale data? What if a consumer crashes after doing work but before acknowledging it? How can derived state be rebuilt?

## Exit Check

Identify the source of truth and the repair path for every derived value.

## Complete Lesson

A cache improves speed but may be stale. A queue separates producers and consumers, introducing delay, duplication, ordering, acknowledgement, and retry questions. Derived data needs a repair path.

A report job may be delivered twice. A durable job ID lets the consumer recognize completed work and avoid duplicate results. Ask when stale reads are acceptable and how derived data can be rebuilt. Never assume exactly-once delivery.

## Dialogue Check

**You:** Is this value the source of truth or a copy?

**Guide:** If it is a cache or derived result, define how stale data, duplicate work, and rebuilding are handled.

**You:** What should I try?

**Guide:** Deliver the same job twice and observe whether the durable result is duplicated.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
