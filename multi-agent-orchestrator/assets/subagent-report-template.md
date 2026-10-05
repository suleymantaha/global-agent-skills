# Subagent Completion Report Template

Workers must submit this 5–10 line structured summary to the orchestrator upon task completion to preserve context hygiene:

```markdown
### Worker Completion Report: [Task ID / Component]

- **Task ID:** [e.g. T-201]
- **Worker Identity:** [e.g. Worker-01 (Backend API)]
- **Status:** [SUCCESS / BLOCKED / FAILED]
- **Modified Files:**
  - `path/to/modified_file_1.py`
  - `path/to/new_test_file.py`
- **Verification Command & Evidence:**
  - Command: `pytest tests/api/test_endpoints.py -v`
  - Output: `5 passed, 0 failed, exit code 0`
- **Remaining Issues / Notes for Verifier:**
  - [None / Specific edge cases noted]
```
