# 06. Application Structure And Request Lifecycle

[Previous: API Contracts](../../05-api-contracts/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Persistence Modeling](../../07-persistence-modeling/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

Structure isolates change. Transport translates protocol messages, the application layer coordinates a use case, domain code enforces decisions, and infrastructure persists or calls external systems.

```text
HTTP adapter -> use case -> domain rule -> repository interface
```

Ask: Which layer should know an HTTP status? Can a business rule be tested without a socket? Where does a transaction begin and end?

## Exit Check

Name one dependency that can be replaced without changing domain code.

## Complete Lesson

As features grow, one request handler can accumulate protocol parsing, business rules, storage, and external calls. Separate the adapter, use case, domain rules, and repository boundary.

```text
adapter -> use case -> domain rules -> repository interface
```

The adapter translates protocols, the use case coordinates work, domain code decides what is allowed, and infrastructure implements storage or network access. This lets rules be tested without a socket.

Ask yourself: Which layer should know an HTTP status? Where does a transaction begin? What can change independently? Avoid putting all logic in handlers.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
