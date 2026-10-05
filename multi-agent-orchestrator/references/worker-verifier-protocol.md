# Worker & Verifier Protocol

Safe multi-agent collaboration requires strict isolation boundaries, independent verification, and disciplined context hygiene.

## 1. Scope Boundaries & Disjoint Ownership

- Partition each objective into disjoint file boundaries before assigning workers.
  - *Example Worker A:* Owns `src/api/` and `tests/api/`.
  - *Example Worker B:* Owns `src/ui/` and `tests/ui/`.
- No worker may edit files outside its designated scope.
- Overlapping changes to shared files must be scheduled sequentially or developed in separate Git worktrees and merged by the orchestrator.

## 2. Contract-First Design

When multiple workers collaborate on interdependent systems:
1. **Freeze Specifications First:** Explicitly define and freeze API contracts, JSON schemas, routes, DTOs, or database schemas before workers begin code generation.
2. **Mock Boundaries:** Client/consumer workers mock against the agreed contract until the producer's implementation is verified.

## 3. Worker + Independent Shadow Verifier Pattern

Self-review is prone to confirmation bias. Verification must be decoupled from authoring:
- **Worker Agent:** Implements the scoped changes and writes unit/integration tests within its boundary.
- **Verifier (Shadow) Agent:** An independent, read-only evaluator that:
  - Validates code against the agreed contract and invariants.
  - Executes static analysis, linter checks, and test suites.
  - Confirms zero regressions and demands actual execution evidence before sign-off.
- The authoring worker cannot approve its own completion.

## 4. Context Hygiene

- Workers must never return raw logs, massive terminal outputs, or whole-file dumps to the depth-0 orchestrator.
- Return a compact 5–10 line structured summary:
  1. Objectives completed.
  2. Files modified or created.
  3. Exact verification command executed and actual exit code / test result.
  4. Unresolved issues, assumptions, or notes for the next worker.
