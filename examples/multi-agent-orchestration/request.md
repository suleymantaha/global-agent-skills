# Example Request: Multi-Agent Orchestrated Feature

```text
Use $multi-agent-orchestrator to coordinate implementing our user export feature:
1. Backend: Build a paginated CSV export endpoint in src/api/export.py with unit tests.
2. Client: Add the export button and progress state in src/client/export_button.ts with tests.
3. Keep file ownership disjoint, freeze the API contract first, use independent verifiers, and track state in tasks/ledger.md.
```
