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

## Complete Lesson

Process memory disappears on restart. Persistence stores durable facts with relationships and rules that survive crashes. Start with facts and invariants, then choose entities, keys, constraints, indexes, and migrations.

```text
memory state --commit--> durable state
invariant: true before and after a valid change
```

An account balance can have a database constraint that it is never negative. Application validation is useful, but the database is a second defense.

Ask yourself: Which facts must survive restart? What is the source of truth? Where should uniqueness be enforced?

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
