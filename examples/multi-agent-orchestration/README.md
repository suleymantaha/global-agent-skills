# Example: Multi-Agent Orchestration Walkthrough

This example demonstrates how an AI orchestrator handles a cross-layer feature using `multi-agent-orchestrator`:

1. **Request:** The user prompts the orchestrator with an objective spanning both backend and frontend components ([request.md](request.md)).
2. **Tier 2 Classification:** Because 2+ files and multiple architectural layers are involved, the orchestrator initiates Tier 2 mode:
   - Freezes the API contract before authoring code.
   - Decomposes work into disjoint file ownership scopes.
   - Allocates parallel workers with a concurrency cap of 2.
3. **Atomic Tracking:** The orchestrator maintains task status in [tasks-ledger.md](tasks-ledger.md).
4. **Context Hygiene:** Workers return concise 5–10 line structured summaries with real test evidence rather than flooding the orchestrator transcript ([worker-report.md](worker-report.md)).
5. **Quality Gate:** Independent verifiers confirm linter and unit tests pass before final sign-off.
