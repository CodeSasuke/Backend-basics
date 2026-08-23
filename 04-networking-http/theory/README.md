# 04. Networking And HTTP

[Previous: Protocols](../../03-protocols/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: API Contracts](../../05-api-contracts/theory/README.md)

## Code Example

Run [the starter code](../code/main.py), then record your prediction and observations in the [experiment log](../exercises/experiment.md).

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
 
## Complete Lesson

A network adds distance, latency, packet loss, independent failures, and uncertainty. The caller and server do not share memory or a clock. HTTP gives request and response bytes shared meaning through method, target, headers, body, and status.

```text
client -- request --> server
client <-- response -- server
       connection can fail at any point
```

A health request can return `200`; an unknown path can return `404`. A timeout means the caller has no answer, not that the server did nothing.

Ask yourself: Why can a server receive a request but fail to respond? Which operations are safe to retry? What belongs in headers?

Common mistakes include retrying writes blindly, forgetting timeouts, and treating status codes as the entire API contract.

## Dialogue Check

**You:** What does the client know after this response or timeout?

**Guide:** Separate confirmed facts from unknown outcomes, then choose whether retrying is safe.

**You:** How can I test that idea?

**Guide:** Make a prediction, use the client, and record the request and response evidence.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
