---
name: multi-agent-orchestrator
description: Use when explicitly requested or authorized multi-agent work requires coordinating independent tasks and integrating results.
metadata:
  version: "1.1.0"
---

# Multi-Agent Orchestrator

- Respect host delegation restrictions, available APIs, concurrency limits, and user scope. Do not invent tools, role parameters, or transcript paths. Fall back to sequential work when delegation is unavailable.
- Delegate independent tasks with objective, inputs, file ownership, permitted side effects, dependencies, acceptance checks, and expected evidence. A fixed three-level hierarchy is optional.
- Check whether agents share storage. Use isolated worktrees for overlapping changes or disjoint file ownership for safe shared-workspace work. Inspect Git state, preserve existing edits, and use returned workspace paths; spawning alone does not isolate files.
- Prefer native task tracking and messaging. If durable JSONL queues are needed, use unique IDs, single-writer or locking, atomic transitions, and restart reconciliation rather than three independently updated state files.
- Workers report artifacts, actual checks, and unresolved issues. Review the combined diff and run integration checks before completion.
- Incorporate user steering, stop obsolete tasks, and clean up only owned resources. Do not discard changes or delete branches without authorization.
