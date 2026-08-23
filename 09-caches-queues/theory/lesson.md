# Lesson: Caches, Queues And Derived State

## Start With The Problem
Some work is expensive or slow. Caches reduce repeated work; queues separate producers and consumers. Both introduce consistency questions.

## Core Model

```text
producer -> queue -> consumer -> source of truth
request -> cache hit | miss -> source -> cache fill
```

A cache can be stale. A queue can redeliver. A consumer must be safe to repeat when delivery is at-least-once.

## Worked Example
A report job may be delivered twice. A durable job ID lets the consumer recognize a completed job and avoid producing duplicate results.

## Think About It
- How is derived data rebuilt?
- What happens after a consumer crash?
- When is stale data acceptable?

## Common Mistakes
Treating a cache as the source of truth, assuming exactly-once delivery, and having no failed-job path.

## Mastery Check
Design retry, acknowledgement, ordering, deduplication, and rebuild behavior for a report queue.