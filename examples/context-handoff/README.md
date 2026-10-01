# Real usage: evidence-preserving context handoff

The `context-optimization` skill was read and applied during this repository's GitHub launch preparation. Instead of replaying all installation and documentation history, the agent produced a continuation handoff from actual repository inspection.

1. [Request](request.md): the task and authorized scope.
2. [Captured evidence](evidence.json): actual commands, outputs, baseline commit, and skill hash.
3. [Agent output](handoff.md): objective, scope, verified artifacts, checks, limits, and next action.

## What was checked

The source snapshot has seven skill entry points. Validation and diff checks actually exited 0. The handoff retains the exact baseline commit and check result, the GitHub-only scope, and unfinished release/list work. It distinguishes structural validation from behavioral evaluation and does not assert a deployment or token-saving percentage.

The baseline is immutable in Git history; compare `git show <snapshot_commit>:README.md` and `git ls-tree -r --name-only <snapshot_commit>` with the evidence. Re-run `python scripts/validate_skills.py` against the current checkout for current validation.

## Try it on your own task

```text
Use $context-optimization to prepare a continuation handoff from this repository.
Preserve the current objective, permissions, changed files, actual test outcomes,
uncertainties, evidence pointers, and next step. Verify the current state first.
```

Review whether another person can resume without asking for facts already available. Check facts against command output, not just the handoff's wording.

## Limits

This is a maintainer-run example within the same conversation, not an independent subagent or fresh-session evaluation. No unskilled control run, timing test, token-count measurement, cross-host trial, or external community adoption has been established. It demonstrates one concrete use and does not prove the other six modules work in every scenario.

## Subsequent independent-context evaluation

The paragraph above describes the original example only. A later [seven-skill matched-control evaluation](../../evaluations/2026-10-01/RESULTS.md) now adds independent subagent contexts, a no-target-body control, blinded review, wall-time recording, and output-token counts. Cross-host testing and outside adoption remain unestablished.
