# 07. Persistence And Data Modeling

[Previous: Application Structure](../../06-application-structure/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Transactions](../../08-transactions/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

Persistent state outlives a process. Start with facts and invariants, then choose tables, keys, constraints, indexes, and migrations.

```text
application state --commit--> durable state
invariant: true before and after a transaction
```

Ask: Which facts must never contradict? What survives a crash? Why enforce a rule in the database as well as application code?

## Exit Check

List the ledger invariants and the layer responsible for enforcing each one.