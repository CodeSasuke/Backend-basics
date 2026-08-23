# 04. Networking And HTTP

[Previous: Protocols](../../03-protocols/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: API Contracts](../../05-api-contracts/theory/README.md)

## Why This Exists

A network adds distance, latency, independent failures, and uncertainty. HTTP gives request and response messages shared meaning through methods, targets, headers, bodies, and status codes.

```text
client -- request bytes --> server
client <-- response bytes -- server
       connection may fail at any point
```

A timeout means the caller lacks an answer. It does not prove that the server did not perform the operation.

## Socratic Questions

- Why can a server receive a request but fail to respond?
- What makes retrying a write dangerous?
- What belongs in a header rather than a body?
- Which status communicates invalid input?

## Exit Check

Trace one request from client intent to server response and list every boundary.