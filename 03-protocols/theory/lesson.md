# Lesson: Bytes, Messages, And Protocols

## Start With The Problem
Two systems cannot share meaning just because both can send bytes. They need rules for encoding, message boundaries, fields, versions, and errors.

## Core Model

```text
bytes -> decode -> frame -> validate shape -> apply meaning
meaning -> encode -> bytes
```

Serialization changes representation. Validation checks whether data is acceptable. Business rules decide whether an accepted action is allowed.

## Worked Example
`CREATE|title|body` is a protocol message. A newline can frame messages, but a delimiter inside the body requires escaping or a different format.

## Think About It
- How does the receiver know where a message ends?
- What does a truncated message mean?
- Can an unknown field be ignored safely?

## Common Mistakes
Parsing and validation in one opaque function, accepting ambiguous input, and changing a format without a compatibility rule.

## Mastery Check
Specify a versioned protocol including framing, limits, malformed-input behavior, and an evolution rule.