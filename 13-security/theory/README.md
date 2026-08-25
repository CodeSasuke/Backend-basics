# 13. Security Fundamentals

[Previous: Observability](../../12-observability/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Testing And Delivery](../../14-testing-delivery/theory/README.md)

## Lesson Orientation

This lesson treats every external input and identity as untrusted until the appropriate controls have been applied. Read the theory and inspect the starter code before running it.

Security protects confidentiality, integrity, and availability under adversarial input. Every boundary is untrusted; every privilege should be minimized.

```text
request -> validate -> authenticate identity -> authorize action
```

Authentication asks who. Authorization asks what that identity may do. Hash passwords with a reviewed library, protect secrets, prevent injection, and audit sensitive actions.

## Exit Check

For every endpoint, identify the asset, attacker capability, trust boundary, and control.

## Complete Lesson

Public inputs and external identities are untrusted. Security protects confidentiality, integrity, and availability. Authentication asks who; authorization asks what that identity may do.

A user may authenticate successfully but still be forbidden from reading another user's private note. Ask what the asset is, where data can become code or a query, and what happens if a token is stolen. Never store plaintext passwords or log secrets.

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Identify every untrusted input, authentication decision, authorization decision, sensitive asset, and security-relevant failure. Before executing the program, record your predictions and observations in the [experiment log](../exercises/experiment.md).

Run the experiment only after making your predictions. Then answer the Socratic questions below using both the code and the evidence you recorded.

## Dialogue Check

**You:** Who is this caller, and what may they do?

**Guide:** Keep authentication and authorization separate, then check the resource owner at the server boundary.

**You:** What should I challenge?

**Guide:** Try another identity, malformed input, and a request containing data that must never become a command.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
