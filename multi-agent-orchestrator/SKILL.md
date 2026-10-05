---
name: multi-agent-orchestrator
description: Use when explicitly requested or authorized multi-agent work requires coordinating independent tasks and integrating results.
metadata:
  version: "1.2.0"
---

# Multi-Agent Orchestrator

- Respect host delegation restrictions, available APIs, concurrency limits, and user scope. Do not invent tools, role parameters, or transcript paths. Fall back to sequential work when delegation is unavailable.
- Apply [Tier Classification](references/tier-classification.md): use inline execution for small/bounded changes (Tier 1); engage depth-0 orchestration mode with max 3–4 concurrent workers for cross-layer systems (Tier 2).
- Follow the [Worker & Verifier Protocol](references/worker-verifier-protocol.md): freeze contracts first, assign disjoint file ownership, use independent shadow verifiers, and enforce 5–10 line structured worker reports.
- Track progress atomically using the [Tasks Ledger Template](assets/tasks-ledger-template.md) and standardize worker summaries with the [Subagent Report Template](assets/subagent-report-template.md).
- Enforce the [Circuit Breaker](references/circuit-breaker.md): trip and halt execution on 3 consecutive failures, execute deterministic rollback (`git reset --hard HEAD`), and escalate to architecture redesign.
- Check whether agents share storage. Use isolated worktrees for overlapping changes or disjoint file ownership for safe shared-workspace work. Inspect Git state, preserve existing edits, and use returned workspace paths; spawning alone does not isolate files.
- Review the combined diff across all worker scopes and run integration checks before declaring completion. Do not discard changes or delete branches without authorization.
