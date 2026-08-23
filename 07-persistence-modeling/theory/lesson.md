# Lesson: Persistence And Data Modeling

## Start With The Problem
Process memory disappears on restart. A backend needs durable facts with relationships and rules that survive crashes.

## Core Model
Start with facts and invariants, then choose entities, keys, constraints, indexes, and migrations.

```text
memory state --commit--> durable state
invariant: true before and after a valid change
```

## Worked Example
An account balance can have a database constraint that it is never negative. Application validation is useful, but the database is a second defense.

## Think About It
- Which facts must survive restart?
- What is the source of truth?
- Where should uniqueness be enforced?

## Common Mistakes
Treating storage as a dump of objects, omitting constraints, and changing schemas without migrations.

## Mastery Check
Model users, notes, and ownership with invariants, constraints, indexes, and a migration plan.