# Backend Engineering Basics Roadmap

This file is the course index. Use it to choose the next module and open its materials. The explanations, visuals, Socratic questions, exercises, and code belong inside the module folders.

[Progress dashboard](PROGRESS.md) | [Template guide](TEMPLATE_GUIDE.md) | [Shared notes-service project](projects/notes-service/README.md)

## Learning Flow

For each module:

1. Open **Theory** and read the lesson.
2. Write your thinking in **Notes**.
3. Open **Exercises** and make a prediction.
4. Record the experiment in **Experiment log**.
5. Implement in **Solution** while comparing with **Starter code**.
6. Record your answers and complete the **Exit check**.
7. Move to the next module only when you can explain the idea without relying on Python vocabulary.

## Module Workspace

Every module follows this structure:

```text
module/
  theory/README.md       lesson content
  theory/notes.md        your theory notes
  exercises/README.md    exercises and task
  exercises/experiment.md prediction and evidence
  exercises/answers.md   your answers and review
  code/main.py           reference starter
  code/solution.py       your implementation
```

## Phase 1: Foundations

Learn what a backend process is, how it holds state, and how systems communicate.

### 01. Processes And State

[Theory](01-processes-and-state/theory/README.md) | [Exercises](01-processes-and-state/exercises/README.md) | [Notes](01-processes-and-state/theory/notes.md) | [Experiment](01-processes-and-state/exercises/experiment.md) | [Answers](01-processes-and-state/exercises/answers.md) | [Code](01-processes-and-state/code/main.py) | [Solution](01-processes-and-state/code/solution.py)

### 02. Operating Systems And Resources

[Theory](02-os-resources/theory/README.md) | [Exercises](02-os-resources/exercises/README.md) | [Notes](02-os-resources/theory/notes.md) | [Experiment](02-os-resources/exercises/experiment.md) | [Answers](02-os-resources/exercises/answers.md) | [Code](02-os-resources/code/main.py) | [Solution](02-os-resources/code/solution.py)

### 03. Protocols

[Theory](03-protocols/theory/README.md) | [Exercises](03-protocols/exercises/README.md) | [Notes](03-protocols/theory/notes.md) | [Experiment](03-protocols/exercises/experiment.md) | [Answers](03-protocols/exercises/answers.md) | [Code](03-protocols/code/main.py) | [Solution](03-protocols/code/solution.py)

## Phase 2: Web And APIs

Build an HTTP service and learn to design contracts that independent clients can rely on.

### 04. Networking And HTTP

[Theory](04-networking-http/theory/README.md) | [Exercises](04-networking-http/exercises/README.md) | [Notes](04-networking-http/theory/notes.md) | [Experiment](04-networking-http/exercises/experiment.md) | [Answers](04-networking-http/exercises/answers.md) | [Code](04-networking-http/code/main.py) | [Solution](04-networking-http/code/solution.py)

### 05. API Design And Contracts

[Theory](05-api-contracts/theory/README.md) | [Exercises](05-api-contracts/exercises/README.md) | [Notes](05-api-contracts/theory/notes.md) | [Experiment](05-api-contracts/exercises/experiment.md) | [Answers](05-api-contracts/exercises/answers.md) | [Code](05-api-contracts/code/main.py) | [Solution](05-api-contracts/code/solution.py)

### 06. Application Structure

[Theory](06-application-structure/theory/README.md) | [Exercises](06-application-structure/exercises/README.md) | [Notes](06-application-structure/theory/notes.md) | [Experiment](06-application-structure/exercises/experiment.md) | [Answers](06-application-structure/exercises/answers.md) | [Code](06-application-structure/code/main.py) | [Solution](06-application-structure/code/solution.py)

## Phase 3: Data

Model durable state, query it efficiently, and protect it with transactions.

### 07. Persistence And Data Modeling

[Theory](07-persistence-modeling/theory/README.md) | [Exercises](07-persistence-modeling/exercises/README.md) | [Notes](07-persistence-modeling/theory/notes.md) | [Experiment](07-persistence-modeling/exercises/experiment.md) | [Answers](07-persistence-modeling/exercises/answers.md) | [Code](07-persistence-modeling/code/main.py) | [Solution](07-persistence-modeling/code/solution.py)

### 08. Queries, Indexes And Transactions

[Theory](08-transactions/theory/README.md) | [Exercises](08-transactions/exercises/README.md) | [Notes](08-transactions/theory/notes.md) | [Experiment](08-transactions/exercises/experiment.md) | [Answers](08-transactions/exercises/answers.md) | [Code](08-transactions/code/main.py) | [Solution](08-transactions/code/solution.py)

### 09. Caches, Queues And Derived State

[Theory](09-caches-queues/theory/README.md) | [Exercises](09-caches-queues/exercises/README.md) | [Notes](09-caches-queues/theory/notes.md) | [Experiment](09-caches-queues/exercises/experiment.md) | [Answers](09-caches-queues/exercises/answers.md) | [Code](09-caches-queues/code/main.py) | [Solution](09-caches-queues/code/solution.py)

## Phase 4: Reliability

Design for failure, bounded work, concurrency, and useful evidence.

### 10. Errors, Timeouts And Retries

[Theory](10-failure-retries/theory/README.md) | [Exercises](10-failure-retries/exercises/README.md) | [Notes](10-failure-retries/theory/notes.md) | [Experiment](10-failure-retries/exercises/experiment.md) | [Answers](10-failure-retries/exercises/answers.md) | [Code](10-failure-retries/code/main.py) | [Solution](10-failure-retries/code/solution.py)

### 11. Concurrency And Parallelism

[Theory](11-concurrency/theory/README.md) | [Exercises](11-concurrency/exercises/README.md) | [Notes](11-concurrency/theory/notes.md) | [Experiment](11-concurrency/exercises/experiment.md) | [Answers](11-concurrency/exercises/answers.md) | [Code](11-concurrency/code/main.py) | [Solution](11-concurrency/code/solution.py)

### 12. Observability And Debugging

[Theory](12-observability/theory/README.md) | [Exercises](12-observability/exercises/README.md) | [Notes](12-observability/theory/notes.md) | [Experiment](12-observability/exercises/experiment.md) | [Answers](12-observability/exercises/answers.md) | [Code](12-observability/code/main.py) | [Solution](12-observability/code/solution.py)

## Phase 5: Production Thinking

Apply security, testing, delivery, deployment, and scaling decisions.

### 13. Security Fundamentals

[Theory](13-security/theory/README.md) | [Exercises](13-security/exercises/README.md) | [Notes](13-security/theory/notes.md) | [Experiment](13-security/exercises/experiment.md) | [Answers](13-security/exercises/answers.md) | [Code](13-security/code/main.py) | [Solution](13-security/code/solution.py)

### 14. Testing And Delivery

[Theory](14-testing-delivery/theory/README.md) | [Exercises](14-testing-delivery/exercises/README.md) | [Notes](14-testing-delivery/theory/notes.md) | [Experiment](14-testing-delivery/exercises/experiment.md) | [Answers](14-testing-delivery/exercises/answers.md) | [Code](14-testing-delivery/code/main.py) | [Solution](14-testing-delivery/code/solution.py)

### 15. Deployment, Scaling And System Design

[Theory](15-deployment-scaling/theory/README.md) | [Exercises](15-deployment-scaling/exercises/README.md) | [Notes](15-deployment-scaling/theory/notes.md) | [Experiment](15-deployment-scaling/exercises/experiment.md) | [Answers](15-deployment-scaling/exercises/answers.md) | [Code](15-deployment-scaling/code/main.py) | [Solution](15-deployment-scaling/code/solution.py)

## Phase 6: Capstone

Integrate the complete system into a reliable notes and jobs platform.

### 16. Reliable Notes And Jobs Platform

[Theory](16-capstone/theory/README.md) | [Exercises](16-capstone/exercises/README.md) | [Notes](16-capstone/theory/notes.md) | [Build log](16-capstone/exercises/experiment.md) | [Review](16-capstone/exercises/answers.md) | [Code](16-capstone/code/main.py) | [Solution](16-capstone/code/solution.py)

## Start Here

[Open Module 01: Processes And State](01-processes-and-state/theory/README.md)
