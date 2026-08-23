# 08. Queries, Indexes And Transactions

[Previous: Persistence Modeling](../../07-persistence-modeling/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Caches And Queues](../../09-caches-queues/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

Queries locate facts. Indexes trade write/storage cost for lookup speed. Transactions group changes so readers do not observe an unacceptable intermediate state.

```text
begin -> read -> change A -> change B -> commit
                         \-> failure -> rollback
```

Ask: Why can an index slow writes? Can two valid transactions create an invalid result? What isolation guarantee is actually needed?

## Exit Check

Describe a lost-update race as an interleaving of two transactions.

## Complete Lesson

Multiple changes can expose an invalid intermediate state, and concurrent readers or writers can lose updates. A transaction groups changes into an atomic unit. An index trades storage and write cost for lookup speed.

```text
begin -> read -> change A -> change B -> commit
                         \-> failure -> rollback
```

A transfer must subtract from one account and add to another in one transaction. If either update fails, neither should remain.

Ask yourself: Can two valid transactions create an invalid result? What does atomicity protect? Which query benefits from an index?

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
