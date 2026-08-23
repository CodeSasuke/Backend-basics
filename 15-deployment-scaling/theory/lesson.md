# Lesson: Deployment, Scaling And System Design

## Start With The Problem
A service changes when placed in production: traffic varies, resources are finite, dependencies fail, and someone must recover it.

## Core Model
Scaling relieves bottlenecks while managing state, consistency, coordination, and cost.

```text
clients -> load balancer -> service instances -> database
                              +-> cache / queue / workers
```

A stateless instance keeps durable or shared state outside its process. Health means the process can serve; readiness means dependencies are usable.

## Worked Example
Adding service instances does not fix a saturated database. Capacity estimates begin with assumptions about concurrency, latency, and resource limits.

## Think About It
- What saturates first?
- What can be eventually consistent?
- How does rollback work?

## Common Mistakes
Scaling every component equally, storing session state locally, and deploying without migration or rollback plans.

## Mastery Check
Write assumptions, capacity estimates, bottlenecks, failure modes, rollout, rollback, backup, and cost decisions.