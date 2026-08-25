# 03. Bytes, Messages, And Protocols

[Previous: OS Resources](../../02-os-resources/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Networking And HTTP](../../04-networking-http/theory/README.md)

## Lesson Orientation

This lesson explains how independent systems agree on the meaning of bytes. Read the theory and inspect the starter code before running it.

## Why This Exists

Independent systems only share meaning when they share rules for bytes: encoding, framing, fields, message types, and errors.

```text
bytes -> decode -> shape -> validate -> meaning
meaning -> encode -> bytes
```

Serialization changes representation. Validation checks whether the representation is acceptable. Business rules decide whether an accepted action is allowed.

## Socratic Questions

- How does the receiver know where a message ends?
- What happens to an unknown field?
- Is malformed input a client error or a server failure?
- Which compatibility rule permits an old client to keep working?

## Exit Check

Describe parsing, validation, and business rules as three separate responsibilities.
 
## Complete Lesson

Two systems cannot share meaning just because both can send bytes. They need rules for encoding, message boundaries, fields, versions, and errors. Serialization changes representation; validation checks shape; business rules decide whether an accepted action is allowed.

```text
bytes -> decode -> frame -> validate shape -> apply meaning
meaning -> encode -> bytes
```

`CREATE|title|body` is a protocol message. A delimiter inside the body requires escaping or a different format. A truncated message should be rejected clearly rather than silently interpreted.

Ask yourself: How does the receiver know where a message ends? What happens to an unknown field? Which compatibility rule lets old clients continue working?

Common mistakes include combining parsing and business rules in one opaque function and changing a format without a compatibility plan.

## Code Example

Read the [starter program](../code/main.py) from top to bottom without modifying or running it. Identify the byte-to-message boundary, the parser, the validator, and the encoder. Before executing the program, record your predictions and observations in the [experiment log](../exercises/experiment.md).

Run the experiment only after making your predictions. Then answer the Socratic questions below using both the code and the evidence you recorded.

## Dialogue Check

**You:** Do these bytes form a valid message?

**Guide:** Decode them, find the boundary, validate the shape, and only then assign meaning.

**You:** What should I test next?

**Guide:** Try one valid message, one malformed message, and one future-compatible message.

## My Notes

### Problem and explanation


### My visual

```text

```

### Socratic answers

- 

### Exit-check answer
