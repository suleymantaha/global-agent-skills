# Circuit Breaker & Automatic Rollback Protocol

Autonomous agents attempting to resolve recurring errors can fall into destructive feedback loops (hallucination cascades): failing tests trigger ad-hoc patches, introducing cascading breakage and wasting tokens.

The Circuit Breaker mechanism arrests repeated failures before state corruption occurs.

## 1. The 3-Strike Rule

Track consecutive failures per task assignment:

| Attempt | Status | Action |
| :--- | :--- | :--- |
| **Attempt 1** | Failure | Inspect error logs, formulate hypothesis, and retry. |
| **Attempt 2** | Failure | Warning: Current hypothesis is likely flawed; rethink approach. |
| **Attempt 3** | Failure | **CIRCUIT TRIPPED (Open)**: Immediately halt worker execution. |

## 2. Procedure When Tripped

1. **Immediate Halt (Kill Switch):** Terminate the active worker's execution thread or background process.
2. **Deterministic Rollback:** Discard unverified modifications to return the repository to the last clean, verified commit:
   ```bash
   git reset --hard HEAD
   git clean -fd
   ```
   *(If working within an isolated Git worktree, remove or reset the worktree branch).*
3. **Update Ledger:** Record the trip in the task tracking ledger:
   - Mark task status as `TRIPPED (3 Failures)`.
   - Log the root cause and the failing command output snippet.
4. **Architectural Escalation:**
   - Do not re-assign the exact same prompt to another worker.
   - The depth-0 orchestrator must reconsider the design, decompose the task into smaller sub-units, switch libraries/strategies, or ask the user for guidance.
