# Lesson: Testing And Delivery

## Start With The Problem
Code can appear correct while violating important behavior. Delivery also fails when setup depends on an individual machine.

## Core Model
Unit tests isolate rules, integration tests verify boundaries, contract tests protect agreements, and end-to-end tests verify workflows.

```text
many focused unit tests -> fewer integration tests -> few broad workflow tests
```

## Worked Example
A unit test proves an overdraft is rejected. An integration test proves the database constraint and transaction behavior.

## Think About It
- What behavior is worth protecting?
- Which test gives the best signal?
- What must a clean checkout be able to do?

## Common Mistakes
Testing implementation details, relying only on end-to-end tests, and merging without repeatable checks.

## Mastery Check
Design a test pyramid and delivery gate that catches a contract break, data error, and migration failure.