---
name: self-healing-quality-gates
description: Use when requested changes need repository quality-gate selection or bounded diagnosis and repair of failing checks.
metadata:
  version: "1.1.0"
---

# Self-Healing Quality Gates

- Inspect repository instructions, versions, package scripts, CI, and tests. Use configured checks; Python tools are not universal and coverage targets must come from the project. Do not install unrelated tooling.
- Detect: run relevant checks and capture exit status and decisive output; identify pre-existing failures when practical.
- Diagnose: distinguish code defects from dependencies, permissions, and tool failures.
- Repair: make a minimal scoped change, format, and review the diff.
- Validate: rerun affected checks; broaden only for integration risk or unresolved concerns.
- After three attempts with the same unchanged failure, stop that path and report evidence and missing input; continue useful independent work. Respect stricter tool-specific limits. Never weaken tests or disable checks merely to pass.
- Retry transient read-only failures with bounded backoff and server guidance. Before retrying writes, reconcile outcome and use idempotency. Diagnose authentication/permission/invalid-input failures instead of repeating calls.
- Add meaningful tests for new behavior using the project framework. Report actual commands, outcomes, and unverified areas. Compilation does not prove behavior.
- Review final scope, data integrity, and secrets. Independent review may help when authorized and available; shadow agents are optional.
