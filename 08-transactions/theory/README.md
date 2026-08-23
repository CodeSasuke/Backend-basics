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