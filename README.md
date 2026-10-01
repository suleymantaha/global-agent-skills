# Global Agent Skills

Seven focused, portable skills for AI coding agents, following the [Agent Skills specification](https://agentskills.io/specification).

These are on-demand instructions, not running services. They do not install sandboxes, memory backends, MCP servers, hooks, or background agents. Host capabilities, user authorization, and repository instructions remain authoritative.

## Skills

| Skill | When to use |
| --- | --- |
| [multi-agent-orchestrator](multi-agent-orchestrator/SKILL.md) | Authorized delegation, worker ownership, integration checks |
| [code-sandbox-security](code-sandbox-security/SKILL.md) | Untrusted-code isolation, egress, credential delivery |
| [context-optimization](context-optimization/SKILL.md) | Large outputs, long sessions, evidence-preserving handoffs |
| [agent-memory-systems](agent-memory-systems/SKILL.md) | Persistent memory, scoped retrieval, retention and provenance |
| [self-healing-quality-gates](self-healing-quality-gates/SKILL.md) | Project-specific checks, bounded repair, safe retries |
| [mcp-tool-integration](mcp-tool-integration/SKILL.md) | MCP discovery, configuration, permissions and verification |
| [second-brain-vault](second-brain-vault/SKILL.md) | Markdown/Obsidian knowledge capture and reusable workflows |

## Install in Codex

Clone this repository, review the selected SKILL.md files, then copy each desired skill folder directly into `$CODEX_HOME/skills` (default: `~/.codex/skills`). Do not copy the whole repository as a single skill or overwrite existing skills without reviewing differences.

```sh
git clone https://github.com/suleymantaha/global-agent-skills.git
```

For example, copy `global-agent-skills/context-optimization` to `~/.codex/skills/context-optimization`. Installed skills become available on the next turn. Explicit invocation examples:

```text
Use $context-optimization to prepare an evidence-preserving handoff.
Use $self-healing-quality-gates to select and run this project's checks.
```

Other Agent Skills-compatible hosts may use different discovery paths and invocation syntax; follow their documentation. Runtime-specific tools are discovered rather than assumed.

## Validate

Python 3.10+ is required only for the repository validator, not for reading skills.

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

CI checks the skill structure and local Markdown links. These checks do not prove agent behavior, sandbox isolation, or backend access. The initial collection has passed format checks; behavioral evaluation in real tasks is still pending.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Reports with realistic requests and observed outcomes are especially useful.

## License

[Apache License 2.0](LICENSE).
