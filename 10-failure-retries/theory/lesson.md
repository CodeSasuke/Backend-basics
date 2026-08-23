# Lesson: Errors, Timeouts And Retries

## Start With The Problem
Dependencies fail, become slow, or return unknown outcomes. A backend must fail predictably without multiplying load.

## Core Model

```text
caller -- deadline --> dependency
  | timeout -> bounded retry -> fallback or clear failure
```

A retry is safe only when the side effect and duplicate behavior are understood. Backoff and budgets bound damage.

## Worked Example
A payment request times out after the server may have accepted it. An idempotency key lets a retry ask for the same operation rather than create a second payment.

## Think About It
- Which failures are retryable?
- What does a timeout prove?
- What is the least harmful fallback?

## Common Mistakes
Unbounded retries, retrying permanent errors, and reporting unknown outcomes as definite failures.

## Mastery Check
Design deadlines, retry budgets, jitter, idempotency, fallback, and operator evidence.