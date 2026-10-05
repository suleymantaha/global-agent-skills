# Tier Classification (Zero Time Loss Protocol)

To prevent orchestration overhead, token exhaustion, and unnecessary latency on simple tasks, classify incoming work into two operational tiers:

## Tier 1: Inline / Direct Execution

- **Scope:** Single-file modifications, localized bug fixes, lint/formatting adjustments, typo corrections, documentation updates, or status queries.
- **Protocol:**
  - Do not spawn subagents or initialize worktree sandboxes.
  - The primary agent executes the change directly in the existing workspace with minimal token footprint.
  - Run the relevant unit test or lint check locally and commit if required.

## Tier 2: Depth-0 Orchestrator Mode

- **Scope:** Multi-file features (2+ files), cross-layer changes (e.g. API + UI or schema + backend), architectural refactoring, migrations, or release verification.
- **Protocol:**
  - **Depth-0 Separation:** The primary orchestrator directs, scopes, and reviews tasks; it avoids inline code edits that pollute orchestrator context.
  - **Read-Only Parallel Reconnaissance:** Conduct file exploration, requirement discovery, and static research using lightweight, read-only analysis passes before generating implementation plans.
  - **Concurrency Limits:** Enforce a maximum concurrency of 3–4 active parallel workers. Decompose larger jobs into sequential phases (Phase 1 ➔ Phase 2).
  - **Worker + Verifier Pair:** Plan independent implementation workers paired with independent shadow verifiers.
  - **Isolated Storage:** Enforce disjoint file ownership or allocate isolated Git worktrees for tasks with potential file collision.
  - **Task Tracking:** Track progress atomically in a tasks ledger.
