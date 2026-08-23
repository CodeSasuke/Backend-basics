# 05. API Design And Contracts

[Previous: Networking And HTTP](../../04-networking-http/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Application Structure](../../06-application-structure/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

An API is a promise between independent programs. A useful contract defines inputs, outputs, errors, guarantees, and how change remains compatible.

```text
contract = schema + errors + guarantees + compatibility rules
```

Ask: What can a client rely on after success? Which errors are retryable? Is this operation idempotent by behavior? What happens to old clients after a server change?

## Exit Check

Change internal storage without changing the API contract and explain why clients continue working.

## Complete Lesson

Clients and servers evolve independently. An API contract defines input schemas, output schemas, errors, guarantees, and compatibility rules. A create-note operation should define required fields, invalid-field errors, its success shape, and whether repeating a request creates one note or two.

Ask yourself: What can a client safely rely on? Is idempotency a name or a behavior? Which changes are backwards-compatible? Keep storage details private and never leak database errors as the public contract.

## Dialogue Check

**You:** What promise does this API make to its client?

**Guide:** State its inputs, outputs, errors, and guarantees without mentioning its private implementation.

**You:** How can I challenge the contract?

**Guide:** Send valid, invalid, repeated, and old-client requests, then record what remains predictable.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
