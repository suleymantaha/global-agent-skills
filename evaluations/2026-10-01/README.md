# Independent-context skill evaluation — 2026-10-01

**[Read measured results](RESULTS.md)** — 34 fully met criteria plus one partial for the control; 35 fully met for the skill arm. No speed or output-token savings was shown.

## Question

Can the seven modules handle concrete tasks, and do their instruction bodies improve results over a no-target-body control?

## Protocol

Two independent Codex subagents were launched with `fork_turns=none`, without the maintainer conversation. Each received identical raw fixtures and seven task requests. Arm A was instructed not to read or invoke the seven target skill bodies; arm B read and applied each matching module. Workers had isolated writable fixture directories and were not shown the rubric or expected answers.

Both workers retained the normal host instructions and exposed skill catalog. This is a **no-target-body control**, not a pristine model without system guidance. Target-body isolation is instructed, not enforced by a filesystem sandbox. It is independent context within the same host, not a separate Codex desktop chat or different server/model.

The tasks include a real execution bug in a disposable Python fixture and an actual vault edit. The other five are scenario-based review/planning/handoff tasks. No live sandbox, MCP server, memory backend, deployment, paid service, or social account was used.

There is one run per case per arm: 14 task outputs, produced in two sequential suites running concurrently. Suite wall time includes reading, tool calls, reasoning and writing. Run order and host load are not controlled, so it is descriptive, not a speed benchmark. Output token counts use the named tokenizer in metrics.json; they exclude prompts, tool transcripts, hidden reasoning, skill-loading overhead and billing. Shorter output does not by itself imply better performance.

## Evidence

- [Cases](cases.json) and fixtures specify the raw tasks.
- [Rubric](rubric.json) defines five observable criteria per case and was withheld from task workers.
- [Manifest](manifest.json) identifies source commit, skill hashes, environment and run count.

An independent third agent reviews anonymized arms against the rubric; it is another model-based reviewer, not a human or statistically calibrated judge. The maintainer separately re-runs executable checks and inspects edited artifacts. Read results with these limitations rather than as proof of universal effectiveness.

## Not established

Cross-host/cross-model behavior, repeated-run variance, total billed tokens, production isolation, service integration, and outside community adoption remain untested. A public listing PR, stars, or a release is not evidence of real usage by others. Existing qualitative examples should not be represented as savings or maturity guarantees.

Saved report prose is unchanged; line endings and trailing blank lines are normalized for publication. Metrics count the published report text.
