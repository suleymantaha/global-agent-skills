# Results: seven skills, independent contexts, matched control

## Main finding

Both arms handled the tasks well. The no-target-body control met 34 of 35 criteria fully and one partially; the skill-body arm met all 35 fully. No criterion was rated fail. The single partial was a sandbox review that specified denial tests but did not explicitly call for successful permitted-access tests. The skill arm included both.

This is a narrow completeness difference in one run, not evidence of a general quality advantage. Strong host guidance and already-capable agents likely contribute to good control results; this evaluation cannot quantify their causal role.

| Scenario | Control (arm A) | Skill bodies (arm B) | Control report tokens | Skill report tokens |
| --- | --- | --- | ---: | ---: |
| context-optimization | 5/5 | 5/5 | 297 | 330 |
| code-sandbox-security | 4/5 + 1 partial | 5/5 | 508 | 464 |
| agent-memory-systems | 5/5 | 5/5 | 531 | 529 |
| mcp-tool-integration | 5/5 | 5/5 | 346 | 381 |
| multi-agent-orchestrator | 5/5 | 5/5 | 429 | 459 |
| second-brain-vault | 5/5 | 5/5 | 202 | 218 |
| self-healing-quality-gates | 5/5 | 5/5 | 270 | 368 |

## Time and output length

| Descriptive metric | Control | Skill bodies |
| --- | ---: | ---: |
| Entire seven-task suite elapsed wall time | 77 seconds | 85 seconds |
| Saved report tokens, cl100k_base | 2,583 | 2,749 |

The skill arm was longer and slower in this sample. **No measured speed or token savings is established.** The two suites overlapped in time and are single observations, with no randomized order, repeated trials, or latency controls. Output-length differences include wording choices; they exclude skill input overhead, prompts, tools, and hidden reasoning. The tokenizer was tiktoken 0.14.0 with cl100k_base; this is a fixed text measure, not necessarily the host model's tokenizer or actual billing.

## Executed artifact checks

Both agents observed the configured unittest failure, repaired the disposable pricing function, preserved the three-item test, and added a zero-item regression. The maintainer and independent reviewer re-ran the resulting suites: **2 tests passed in each arm**. The original fixture still fails with `28 != 21`, confirming that a real failing fixture existed.

Both vault edits preserved the frontmatter and unrelated note, kept one session entry, and added the confirmed outcome once. Neither inserted the unmeasured speed claim into the journal. These are actual fixture mutations, not statements about live services.

Five remaining scenarios are review/planning/handoff evaluations. They test decisions and scope preservation, not operational backend isolation, retrieval enforcement, MCP connectivity, or actual parallel orchestration.

## What this adds to the previous demo

- Two independent contexts with no parent conversation history.
- A matched no-target-body control for every module.
- A blinded third-agent criterion review and maintainer artifact checks.
- Recorded suite wall time and explicit output-token counts.
- A documented test scenario for all seven modules.

It does **not** establish a fresh desktop chat, a different host/model, statistical significance, comprehensive efficacy, or outside adoption. The control still had normal system instructions and skill discovery metadata. The two task workers handled all seven cases sequentially in their own contexts; there was not a separate agent per case. The reviewer is model-based, not a calibrated human panel. No target skill was modified to improve these scores.

## Evidence and reproduction

Read [protocol](README.md), [cases](cases.json), [rubric](rubric.json), [manifest](manifest.json), [blind review](blind-review.json), [metrics](metrics.json), [artifact verification](verification.json), and [summary](summary.json). The `runs/arm-a` and `runs/arm-b` directories contain all saved outputs and resulting code/vault artifacts. The `fixtures/` directory retains the original inputs; its pricing test is intentionally failing.

To re-run the repaired code, from this repository use:

```sh
cd evaluations/2026-10-01/runs/arm-a/quality
python -m unittest discover -v
```

Repeat from `runs/arm-b/quality`. To repeat the agent comparison, copy `fixtures/` into two new isolated workspaces, provide cases to two agents without the parent history, withhold the rubric, give the matching skill bodies only to one arm, and retain actual reports and timing. Run several repetitions and alternate arm order before drawing performance conclusions.

To recount saved reports, use tiktoken 0.14.0 and `get_encoding("cl100k_base").encode(text)` on each UTF-8 report's text, without counting timing JSON or test sources. Installed module text counts are also recorded in metrics.json, separately from report totals. No exact billed-usage inference is supported.
