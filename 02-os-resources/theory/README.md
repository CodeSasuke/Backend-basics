# 02. Operating Systems and Resource Boundaries

[Previous: Processes and State](../../01-processes-and-state/theory/README.md) | [Roadmap](../../ROADMAP.md) | [Exercises](../exercises/README.md) | [Experiment](../exercises/experiment.md) | [Starter code](../code/main.py) | [Next: Protocols](../../03-protocols/theory/README.md)

## Code Example

Run the [starter program](../code/main.py) after creating a small job file. The program reads one job per line, counts valid jobs, and records malformed input. It obtains the file name from the `JOB_FILE` environment variable; when that variable is absent, it uses `jobs.txt`.

Do not run the program yet. First follow the sequence below. The purpose of the experiment is not merely to make the program run. It is to observe how an ordinary application depends on resources controlled by the operating system.

## How to Study This Lesson

Complete the lesson in this order. The order matters because a prediction made before execution gives you something specific to test.

1. **Read the model.** Read this chapter through the section titled [The Resource Boundary](#the-resource-boundary). Focus on the ideas of ownership, lifetime, limit, and failure mode.
2. **Read the example.** Read [the starter program](../code/main.py) without modifying it. Identify where configuration enters, where the file is acquired, where each line is classified, and where cleanup is guaranteed.
3. **Make predictions.** Open the [experiment log](../exercises/experiment.md) and complete its `Prediction` section. Predict the result for a missing file, a valid job file, malformed lines, and a changed `JOB_FILE` value. Do this before running any command.
4. **Run the experiment.** Follow the steps in the experiment log. Record the exact output, the exit status, and any differences between your predictions and the observed behavior.
5. **Answer the Socratic questions.** Return to the questions in this chapter after recording the observations. Answer them using evidence from the code and the experiment, rather than giving only general definitions.
6. **Complete the exercises.** Work through the [module exercises](../exercises/README.md). They extend the example to temporary files, child processes, missing environment variables, interruption, and partial progress.
7. **Perform the exit check.** Draw the resource boundaries around the worker and identify the owner, cleanup action, limit, and failure behavior for each resource. Compare your response with [the expected observations](../exercises/expected.md) only after making your own attempt.

The theory explains the concepts, the experiment supplies evidence, the Socratic questions test your reasoning, and the exercises require you to apply the ideas. Keep those stages separate in your notes.

## Why This Matters

The process studied in the previous lesson does not execute in isolation. It runs on a machine whose CPU time, memory, file descriptors, sockets, and process slots are finite. The operating system mediates access to these resources and decides what the process is allowed to do.

This boundary is easy to overlook because successful programs make resource acquisition look instantaneous. Opening a file appears to produce a Python object; creating a child process appears to produce a process handle; sending a request appears to use a socket. In each case, however, the program has obtained a scarce operating-system resource with a lifetime, an owner, a limit, and a specific set of failure modes.

Backend reliability depends on making those facts explicit. A program that opens files without closing them may eventually be unable to open another file. A worker that creates an unbounded number of child processes may exhaust memory or process limits. A service that performs blocking I/O may appear slow even though its CPU is mostly idle. These are not abstract operating-system concerns: they become application failures at the boundary between the process and its environment.

## The Resource Boundary

```text
          operating system
   ---------------------------------------------------------
   CPU time | virtual memory | files | sockets | processes
   ---------------------------------------------------------
            ^
            | requests, uses, releases
            v
         application process
```

The application requests access; the operating system either grants the request or reports a failure. The application then uses the resource and remains responsible for releasing it when the resource is no longer needed. The operating system provides enforcement, but it cannot infer every application-level ownership decision.

For every resource, ask four questions:

1. **Who owns it?** Which component is responsible for deciding when it is needed and when it can be released?
2. **What is its lifetime?** Does it exist for one operation, one request, one worker, or the entire process?
3. **What limits it?** What finite quantity can be exhausted: bytes, descriptors, CPU time, connections, or process slots?
4. **How does failure appear?** Does the operation raise an exception, return an error, block, time out, or terminate the process?

This vocabulary turns vague statements such as “the server became slow” into questions that can be investigated.

## Files: Acquisition and Cleanup

The starter program uses a file as its job queue. `path.open()` asks the operating system to open the file and returns a file object that represents an operating-system file descriptor. The descriptor is a limited process resource; it is not just an incidental detail of the Python API.

```python
with path.open(encoding="utf-8") as job_file:
    for line in job_file:
     process(line)
```

The `with` statement establishes a resource-ownership boundary. The file is opened before the block and closed when control leaves the block, including when parsing raises an exception. This is the appropriate default for a resource with a definite lexical lifetime: acquire it, use it in the smallest necessary scope, and release it automatically.

Without deterministic cleanup, a long-running worker can accumulate open descriptors. The operating system eventually refuses new opens, sockets, or pipes, even though the application may still have plenty of memory. Garbage collection is not a substitute for explicit ownership: its timing is not the application’s resource policy, and a reference cycle or a delayed collection can keep a resource alive longer than intended.

The same principle applies beyond files. Socket connections, locks, temporary files, child processes, and database transactions all need a clearly defined owner and cleanup path. The mechanism differs, but the question is the same: what happens if the operation fails halfway through?

## Configuration Is an Input

The worker does not hard-code a particular deployment path. It reads `JOB_FILE` from the environment and falls back to `jobs.txt` for local use:

```text
environment: JOB_FILE=/var/lib/worker/jobs.txt
                |
                v
          application configuration
                |
                v
             file acquisition
```

Configuration is an input to the process, just like a command or a request. Keeping deployment-specific values in the environment makes the same program usable in development, testing, and production. It also makes missing configuration visible at startup instead of hiding an assumption inside business logic.

A missing job file is therefore a resource or configuration failure. It is different from a malformed job line. The first prevents the worker from acquiring its required input; the second occurs after acquisition and can be handled as bad data. Good error handling preserves this distinction because operators need to know whether to repair the deployment or inspect an individual job.

In the starter program, a missing file produces a diagnostic and exits with status `2`. A shell or supervisor can use that non-zero status to distinguish unsuccessful startup from a normal run.

## CPU and Memory

CPU time and memory are also resources, although their ownership is less visible in a short script. CPU is consumed when the process executes instructions. Memory is consumed by the interpreter, application objects, buffers, cached data, and every operation that temporarily holds input or output.

These resources fail differently:

- A CPU-bound task uses a processor continuously and may make other work wait.
- A blocked task is waiting for an external event, such as file or network I/O; it may consume little CPU while still delaying its caller.
- A slow task is a measurement about elapsed time. It may be CPU-bound, blocked, contending for a lock, or waiting behind another task.
- Unbounded input, queues, buffers, or caches increase memory usage until allocation fails or the operating system terminates the process.

“Blocked” describes why progress is not currently being made. “Slow” describes what an observer measures. A blocked operation can be slow, but the terms are not interchangeable. The distinction matters because the remedy differs: reducing computation helps a CPU bottleneck, while timeouts, concurrency limits, or a different I/O design may help a blocked operation.

## Sockets and Child Processes

Network sockets have lifetimes and limits just as files do. A service must decide who opens a connection, who may reuse it, when it expires, and what happens after a timeout. An application that keeps every connection open forever can exhaust file descriptors or hit a peer’s connection limit.

Child processes introduce another ownership relationship. The parent must know whether it is responsible for waiting for a child, collecting its exit status, terminating it on shutdown, and cleaning up its pipes. A child that has finished but whose status has not been collected can remain as a zombie process. A parent that starts workers without a bound can exhaust process slots and memory.

The general rule is simple but demanding: every acquisition must have a corresponding release, and every release must remain reachable on both the success and failure paths.

## A Failure-Oriented Reading of the Example

The worker’s execution can be described as a sequence of resource and data decisions:

```text
read JOB_FILE
  |
  +-- path unavailable -> report missing file, exit 2
  |
  v
open file
  |
  +-- open or read failure -> propagate/report resource failure
  |
  v
read each line
  |
  +-- empty line -> ignore
  +-- malformed line -> record an error, continue
  +-- valid line -> count as processed
  |
  v
close file and report totals
```

Notice the separation of concerns. The file must be available before a job can be interpreted. Once the file is open, malformed records are data-quality failures and do not necessarily require the entire worker to stop. The `with` block closes the file after either path. This is a small example of a larger backend design principle: classify failures at the boundary where they occur, and give each failure a response appropriate to its scope.

## Socratic Questions

### What happens if a file is never closed?

The process retains its file descriptor. Repeating the operation can exhaust the process’s descriptor limit, causing later file, socket, pipe, or process operations to fail. In a short-lived script the operating system eventually reclaims the descriptor when the process exits; in a backend worker, waiting for process exit is usually far too late.

### Which limit fails first when work grows?

There is no universal answer. It depends on the workload and the design. Unbounded records may exhaust memory; excessive parallel work may exhaust CPU or process slots; many simultaneous files or connections may exhaust descriptors; a slow dependency may exhaust request or connection capacity. Measure the resource that grows with the workload instead of guessing from the symptom alone.

### What is the difference between blocked and slow?

Blocked means that an operation is waiting for an event before it can continue. Slow means that an operation takes a long time from an observer’s perspective. A blocked network read may make a request slow, but a request can also be slow because it is performing expensive computation or waiting for a lock.

### Who owns cleanup after an error?

The component that acquired the resource should normally own its release. Ownership should be visible in the code and should cover exceptions, early returns, cancellation, and normal completion. In the example, `process_jobs` owns the opened file for the duration of the `with` block, so Python closes it regardless of how the block ends.

## Practical Rules

- Give every scarce resource an explicit owner.
- Keep the resource’s lifetime no longer than necessary.
- Use context managers or an equivalent structured cleanup mechanism.
- Bound concurrency, queue length, cache size, and buffering.
- Treat environment variables and deployment settings as validated inputs.
- Distinguish unavailable resources from invalid business data.
- Add timeouts to operations that can wait indefinitely.
- Test cleanup and partial failure, not only the successful path.

## Experiment

Use the [experiment log](../exercises/experiment.md) to make predictions before running the program. Try at least these cases:

1. Run with no job file and observe the message and exit status.
2. Run with a file containing valid, empty, and malformed lines.
3. Set `JOB_FILE` to a file in another location and confirm that configuration changes the input without changing the code.
4. Interrupt or alter the experiment and consider whether the file is still closed.

The important observations are the boundary between startup and processing, the difference between malformed input and an unavailable resource, and the fact that cleanup must occur even when normal processing does not finish.

## Exit Check

Draw the resource boundaries around a file-backed worker. For each resource, name its owner, its cleanup action, one limit, and one failure behavior. At minimum, include the job file, memory used for input and errors, CPU time, and the process itself.

## Dialogue Check

**You:** Should I run the code before reading the theory?

**Guide:** No. Read the model and the example first, then make explicit predictions in the experiment log. Running the program comes after the prediction so that the output can confirm or challenge your understanding.

**You:** When should I answer the Socratic questions?

**Guide:** Answer them after the experiment. The first reading gives you concepts to reason with; the experiment gives you concrete evidence; your final answers should connect both.

**You:** When should I read the expected answers?

**Guide:** Read them only after completing your predictions, experiment notes, exercises, and exit check. They are for comparison and correction, not a replacement for reasoning.

## Revision Summary

An operating system resource is finite, has a lifetime, and can fail independently of application logic. Reliable programs make ownership explicit, release resources deterministically, and distinguish blocked operations from merely expensive ones. In the example, the environment supplies the file path, the worker acquires the file, `with` guarantees cleanup, and the program reports missing configuration separately from malformed job data.

## My Notes

### Problem and explanation

Describe the resource boundary in your own words. Explain why a long-running worker cannot rely on process exit or garbage collection to clean up every resource.

### My visual

```text

```

### Socratic answers

- A file that is never closed retains a file descriptor and can eventually prevent later resource acquisitions.
- The first exhausted limit depends on the workload: memory, CPU, file descriptors, sockets, or process slots may fail first.
- Blocked describes waiting for an event; slow describes the elapsed time observed by a caller.
- The component that acquires a resource should own its cleanup, including cleanup after an error.

### Exit-check answer
