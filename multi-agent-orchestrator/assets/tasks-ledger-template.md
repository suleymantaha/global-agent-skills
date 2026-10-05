# Tasks Ledger Template

Use this template as `tasks/ledger.md` to coordinate and track multi-agent workflows atomically.

---

## 1. Plan Overview

- **Objective:** [High-level feature or refactoring goal]
- **Target Release / Milestone:** [vX.Y.Z or Milestone Name]
- **Execution Mode:** [Tier 1 Direct / Tier 2 Orchestrator]
- **Max Concurrency:** [e.g., 3]
- **Active Phase:** [Phase 1 / Phase 2]

---

## 2. Phase 1: Exploration & Contract Freeze

| ID | Task Description | Scope / Path | Assignee | Status | Checkpoint |
|:---|:---|:---|:---|:---|:---|
| T-101 | Read-only reconnaissance & API schema definition | `api/spec.json` | Explorer | DONE | Spec frozen |
| T-102 | Interface boundary review & test fixture setup | `tests/fixtures/` | Architect | DONE | Fixtures validated |

---

## 3. Phase 2: Implementation & Verification

| ID | Task Description | File Scope | Worker | Verifier | Status | Circuit Breaker |
|:---|:---|:---|:---|:---|:---|:---|
| T-201 | Implement data repository & models | `src/models/` | Worker-01 | Verifier-A | IN_PROGRESS | 0/3 (Normal) |
| T-202 | Implement service endpoints | `src/api/` | Worker-02 | Verifier-B | PENDING | 0/3 (Normal) |
| T-203 | Implement client integration | `src/client/` | Worker-03 | Verifier-C | PENDING | 0/3 (Normal) |

*Status Legend:* `PENDING`, `IN_PROGRESS`, `BLOCKED`, `DONE`, `TRIPPED`

---

## 4. Quality Gate Checklist

- [ ] Static analysis & linter pass with 0 errors and 0 warnings.
- [ ] Unit & integration test suites pass at 100%.
- [ ] Integration diff reviewed across all worker scopes.
- [ ] Evidence captured and verified before final merge.
