# Lesson: Queries, Indexes, And Transactions

## Start With The Problem
Multiple changes can expose an invalid intermediate state. Concurrent readers and writers can also lose updates.

## Core Model
A transaction groups changes into an atomic unit. An index accelerates lookup by adding storage and write cost.

```text
begin -> read -> change A -> change B -> commit
                         \-> failure -> rollback
```

## Worked Example
A transfer must subtract from one account and add to another in one transaction. If either update fails, neither should remain.

## Think About It
- Can two valid transactions create an invalid combined result?
- What does atomicity protect?
- Which query benefits from an index?

## Common Mistakes
Checking then updating outside a transaction, indexing every column, and assuming atomicity solves every race.

## Mastery Check
Show a lost-update interleaving, then choose a transaction and isolation strategy that prevents it.