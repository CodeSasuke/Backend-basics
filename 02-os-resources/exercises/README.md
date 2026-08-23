# Exercises: Operating Systems And Resources

[Previous: Processes And State](../../01-processes-and-state/exercises/README.md) | [Theory](../theory/README.md) | [Notes](../theory/notes.md) | [Roadmap](../../ROADMAP.md) | [Experiment log](experiment.md) | [Answers](answers.md) | [Starter code](../code/main.py) | [Next: Protocols](../../03-protocols/exercises/README.md)

- Create temporary files, measure their lifetime, and clean them up on success and failure.
- Start a child process and record its output and exit code.
- Remove a required environment variable and design a useful startup error.

## Task

Build a file-backed worker that processes one job per line, skips malformed jobs with an error record, and returns a meaningful exit code. Test interruption and partial progress.

## Exit Check

For each resource, state its owner, cleanup action, and behavior when unavailable.