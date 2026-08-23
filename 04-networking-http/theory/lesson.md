# Lesson: Networking And HTTP

## Start With The Problem
A network adds distance, latency, packet loss, independent failures, and uncertainty. The caller and server do not share memory or a clock.

## Core Model
HTTP gives request and response bytes shared meaning through method, target, headers, body, and status.

```text
client -- request --> server
client <-- response -- server
      connection can fail at any point
```

## Worked Example
A health request can return `200` with a small body. An unknown path can return `404`. A timeout means the caller has no answer; it does not prove the server did nothing.

## Think About It
- Why can a server receive a request but fail to respond?
- Which operations are safe to retry?
- What belongs in headers?

## Common Mistakes
Using status codes as the whole contract, retrying writes blindly, and forgetting timeouts.

## Mastery Check
Trace a request from intent to response and list every failure boundary.