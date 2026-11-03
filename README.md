<!--
Profile: github.com/tonydzi. Editorial owner: the existing weekly maintenance routine.
Keep profile-specific content; generic repository footers and kit catalogs do not belong here.
PROFILE-ACTIVITY is maintained by tools/refresh_profile.py.
BLOG-POST-LIST is maintained by .github/workflows/blog-post-workflow.yml.
Public repository inventory: docs/REPOSITORIES.md. Maintenance: tools/README.md.
-->

# Anton Dziatkovskii

**Persistent agent memory, deterministic verification and operations across machines.**

The work here asks a practical question: **what evidence shows that an AI agent did what it claimed?** The repositories include small tools, fault-injection experiments, operating patterns and experience reports. Each project documents its own tests and limits.

[Portfolio and resume](https://tonydzi.github.io/) · [All upstream contributions](https://tonydzi.github.io/contributions/) · [Research and publications](https://tonydzi.github.io/scholar/) · [ORCID](https://orcid.org/0000-0001-7408-3054)

## Selected engineering work

| Project | What it does | Where to inspect the evidence |
|---|---|---|
| [sqlite-graph-memory](https://github.com/tonydzi/sqlite-graph-memory) | Persistent memory over Markdown and wikilinks, using SQLite, with MCP access for coding agents. | The repository's evaluation, tests and documented pilot limitations. |
| [verbatim-citation-gate](https://github.com/tonydzi/verbatim-citation-gate) | Checks whether a quoted passage occurs in its claimed source before a RAG answer reaches the reader. | Runnable checks and failure examples. Source matching is not a proof that the claim itself is true. |
| [agent-runtime-integrity-bench](https://github.com/tonydzi/agent-runtime-integrity-bench) | Fault-injection checks for runtime behavior, drawn from replay, idempotency and control-plane incidents. | Dated reports, SDK versions and reproducible scenarios. |
| [verdict-contract](https://github.com/tonydzi/verdict-contract) | Connects a model review's structured verdict to a parser and an actual process exit status. | A small stdlib module, tests and counterexamples. |
| [claw-consensus](https://github.com/tonydzi/claw-consensus) | A propose/counter/accept/commit protocol and operating patterns for agents on multiple machines. | Protocol, examples and tests. A working example does not establish the health of every deployed node. |
| [second-brain-starter-kit](https://github.com/tonydzi/second-brain-starter-kit) | Reusable skills, memory integration and templates for a coding agent used as a second brain. | The current skill index, setup instructions and repository checks. |

**Practical connectors:** [WhatsApp MCP kit](https://github.com/tonydzi/whatsapp-mcp-kit) · [Telegram MCP kit](https://github.com/tonydzi/telegram-mcp-kit).

**Governance and operations:** [claude-bible](https://github.com/tonydzi/claude-bible) · [agent-leash](https://github.com/tonydzi/agent-leash) · [fleet-deploy](https://github.com/tonydzi/fleet-deploy) · [secondop-panel](https://github.com/tonydzi/secondop-panel).

[Complete public repository catalog](docs/REPOSITORIES.md) · [How the pieces fit: SYSTEM.md](SYSTEM.md)

## Selected upstream fixes

- [Microsoft Semantic Kernel #14371](https://github.com/microsoft/semantic-kernel/pull/14371): pin the validated address for Python OpenAPI-plugin requests, closing a check/use gap. Merged 5 October 2026.
- [UK AISI Inspect #4769](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4769): decide a grader panel by strict majority rather than mode. Merged 1 September 2026.
- [Obsidian Second Brain #377](https://github.com/eugeniughelbur/obsidian-second-brain/pull/377): flag a source that calls itself unverified but has no source-quality field. Merged 28 October 2026.

## Recently updated merged contributions

These are contributions to other owners' public repositories. Merged work, open proposals and closed submissions remain distinct in the [full contribution ledger](https://tonydzi.github.io/contributions/).

<!-- PROFILE-ACTIVITY:START -->
Public upstream PRs, sorted by last activity. Merged status verified 2026-11-03 UTC; this is a sample, not a lifetime total.

- **ebertti/awesome-telegram**: [Add telegram-mcp-kit to Tools](https://github.com/ebertti/awesome-telegram/pull/394), merged 2026-11-02.
- **hashgraph-online/awesome-ai-plugins**: [Add second-brain-starter-kit to Development &amp; Workflow](https://github.com/hashgraph-online/awesome-ai-plugins/pull/1006), merged 2026-10-27.
- **hashgraph-online/awesome-ai-plugins**: [Add sqlite-graph-memory to Development &amp; Workflow](https://github.com/hashgraph-online/awesome-ai-plugins/pull/881), merged 2026-10-20.
- **eugeniughelbur/obsidian-second-brain**: [health: flag a source that calls itself unverified but has no source\_quality \(\#258\)](https://github.com/eugeniughelbur/obsidian-second-brain/pull/377), merged 2026-10-28.
- **Sagargupta16/awesome-mcp-servers**: [Add SQLite Graph Memory to Knowledge Management](https://github.com/Sagargupta16/awesome-mcp-servers/pull/227), merged 2026-10-28.
<!-- PROFILE-ACTIVITY:END -->

## Current research and experiments

- [Persona portability benchmark](https://github.com/tonydzi/persona-portability-benchmark): a frozen persona and memory, tested across models with blind judging and contamination checks. Read the dated results and limitations before comparing scores.
- [Python vulnerability-patching probe](https://github.com/tonydzi/pyvulnpatch-probe): an audit of advisory leakage, fix dates, hint ablations and self-reported success in patching benchmarks.
- [Brain Lite](https://github.com/tonydzi/brain-lite): a small receive-only library for another person's coding agent, with checksummed updates and rollback.
- [Control-plane casebook](https://github.com/tonydzi/agent-control-plane-casebook): reproducible incidents involving schedulers, registries and watchdogs.
- [Deep research collection](https://github.com/tonydzi/deep-research): published research summaries with their questions, findings and source links.

[Preprints, PDFs and DOIs](https://tonydzi.github.io/papers/) · [Full publication list](https://tonydzi.github.io/scholar/publications/)

## Latest writing

[Clawrush](https://github.com/tonydzi/clawrush) records what was built, what broke and what was learned. The feed below updates automatically. [The Journey](https://github.com/tonydzi/the-journey) is the longer build-in-public book, with human-readable chapters and a machine-readable edition.

<!-- BLOG-POST-LIST:START -->
- [2 November 2026: The Answer Was Already on the Desk](https://github.com/tonydzi/clawrush/blob/main/longreads/20261102.md) &nbsp;<sub>Nov 3, 2026</sub>
- [1 November 2026: The Experiment We Already Ran and Stopped Measuring](https://github.com/tonydzi/clawrush/blob/main/longreads/20261101.md) &nbsp;<sub>Nov 2, 2026</sub>
- [30 October 2026: Claims That Nothing Verifies](https://github.com/tonydzi/clawrush/blob/main/longreads/20261030.md) &nbsp;<sub>Nov 2, 2026</sub>
- [29 October 2026: Five Things to Build, Five Things Already Standing](https://github.com/tonydzi/clawrush/blob/main/longreads/20261029.md) &nbsp;<sub>Oct 29, 2026</sub>
- [28 October 2026: Somebody Else&#39;s Database, and Somebody Else&#39;s Gate](https://github.com/tonydzi/clawrush/blob/main/longreads/20261028.md) &nbsp;<sub>Oct 29, 2026</sub><!-- BLOG-POST-LIST:END -->

## Working approach

Small tools with inspectable outputs. SQL and files for durable facts; models for judgment and language; tests and independent review for checking the result. A successful command, a delivered file and a verified outcome are different things.

This profile and the repositories are maintained with AI collaboration, including Claude, Codex, Grok and Gemini. Anton owns the work's direction and decisions. Tool roles vary by task; commit credits reflect actual contributions. [AI collaboration policy](https://github.com/tonydzi/.github/blob/main/AI-CONTRIBUTORS.md).

<details>
<summary>GitHub activity</summary>

![GitHub activity and community metrics](metrics.svg)

Generated by this repository's existing metrics workflow. Activity is distinct from verified deployments and project maturity.

</details>

## Contact and testing

Engineers are invited to try a project on a real task and report what broke, with a reproducer or a test result.

- [WhatsApp: +1 341 222 9178](https://wa.me/13412229178)
- [Telegram: @tonydzi](https://t.me/tonydzi) · [English updates: @ClawEng](https://t.me/ClawEng) · [Russian updates: @ClawRus](https://t.me/ClawRus)
- [X: @Tony_Stef_](https://x.com/Tony_Stef_)

[github.com/tonydzi](https://github.com/tonydzi)
