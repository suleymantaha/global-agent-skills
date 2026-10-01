---
name: context-optimization
description: Use when oversized tool outputs, long sessions, or handoffs require reducing context while preserving task state and decisive evidence.
metadata:
  version: "1.1.0"
---

# Context Optimization

- Preserve objective, latest user steering, constraints, permissions, completed changes, failures, unresolved questions, evidence paths, and next action. Separate observations from assumptions; never compress away a blocking error or required check.
- Filter before retrieval using targeted searches, relevant ranges, compact fields, and bounded output. Inspect truncation and retrieve missing decisive evidence.
- Summarize after inspecting output. Keep exact paths, identifiers, exit codes, and representative errors. Store raw evidence only when useful and authorized, with redaction and retention limits.
- Use host compaction and handoff mechanisms. Do not claim to remove turns, cap reasoning, change model settings, or enable caching without available controls and authorization.
- Application prompt caching and model routing require current API/pricing verification; never promise fixed discounts or savings.
- Introduce databases only for a demonstrated durable queryable-history need; small artifacts often suffice.
- Handoffs contain objective, constraints/permissions, changes, checks/results, unresolved issues, evidence pointers, and next step. Summaries do not override current instructions; verify current state before resuming.
