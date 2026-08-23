# Lesson: Security Fundamentals

## Start With The Problem
Public inputs and external identities are untrusted. A backend must protect data, actions, and availability against intentional misuse.

## Core Model

```text
request -> validate -> authenticate identity -> authorize action
```

Authentication asks who. Authorization asks what that identity may do. Confidentiality, integrity, and availability are the core protection goals.

## Worked Example
A user may authenticate successfully but still be forbidden from reading another user's private note. Ownership is an authorization rule.

## Think About It
- What is the asset?
- Where can data become code or a query?
- What happens if a token is stolen?

## Common Mistakes
Confusing authentication with authorization, storing plaintext passwords, trusting client ownership fields, and logging secrets.

## Mastery Check
Create a threat model with assets, trust boundaries, abuse cases, controls, detection, and residual risk.