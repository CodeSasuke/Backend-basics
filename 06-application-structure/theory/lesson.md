# Lesson: Application Structure And Request Lifecycle

## Start With The Problem
As features grow, one request handler can accumulate protocol parsing, business rules, storage, and external calls. Every change then becomes risky.

## Core Model

```text
adapter -> use case -> domain rules -> repository interface
```

The adapter translates protocols. The use case coordinates work. Domain code decides what is allowed. Infrastructure implements storage or network access.

## Worked Example
A create-note request can be validated at the adapter, passed to a use case, checked for domain rules, and saved through a repository that tests can replace.

## Think About It
- Which layer should know an HTTP status?
- Where does a transaction begin?
- What can be tested without a socket?

## Common Mistakes
Putting all logic in handlers, abstracting without a reason, and allowing domain code to depend on a database library.

## Mastery Check
Choose boundaries for a new feature and explain what can change independently.