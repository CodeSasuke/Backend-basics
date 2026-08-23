# Lesson: API Design And Contracts

## Start With The Problem
Clients and servers evolve independently. Without a contract, small internal changes become client failures.

## Core Model
An API contract defines input schemas, output schemas, errors, guarantees, and compatibility rules.

```text
contract = data shapes + behavior + errors + guarantees + versioning
```

## Worked Example
A create-note endpoint should define required fields, invalid-field errors, successful response shape, and whether repeating a request creates one note or two.

## Think About It
- What can a client safely rely on?
- Is idempotency a name or a behavior?
- Which detail should remain internal?

## Common Mistakes
Designing around tables, leaking database errors, and changing response shapes without compatibility planning.

## Mastery Check
Design a public notes API and defend its error, pagination, idempotency, and versioning choices.