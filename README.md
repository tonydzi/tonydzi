<!--
Profile: github.com/tonydzi. Editorial owner: the existing weekly maintenance routine.
Keep profile-specific content; generic repository footers and kit catalogs do not belong here.
PROFILE-ACTIVITY is maintained by tools/refresh_profile.py.
BLOG-POST-LIST is maintained by .github/workflows/blog-post-workflow.yml.
Public repository inventory: docs/REPOSITORIES.md. Maintenance: tools/README.md.
-->

# Anton Dziatkovskii

**I have a brain tumor. I found it ten years ago, and that is why I started building a second brain long before LLMs became a hype: my own notes, indexed and searchable, retrieval over a personal archive. Today that archive feeds my agents. Agent memory is my personal pain, not a product idea.**

PhD, Python/C++ engineer, technical lead at Palo Alto AI Research Lab. **Seeking Research Engineer roles.**

**Persistent agent memory, deterministic verification and operations across machines.**

The work here asks a practical question: **what evidence shows that an AI agent did what it claimed?** The repositories include small tools, fault-injection experiments, operating patterns and experience reports. Each project documents its own tests and limits.

[Portfolio and resume](https://tonydzi.github.io/) · [All upstream contributions](https://tonydzi.github.io/contributions/) · [Research and publications](https://tonydzi.github.io/scholar/) · [ORCID](https://orcid.org/0000-0001-7408-3054)

## START HERE

Lost among the repositories? Of the 200+ public ones, about 150 are working forks used to send fixes to other projects. Our own work is a short list. Read in this order:

1. [second-brain-starter-kit](https://github.com/tonydzi/second-brain-starter-kit): the entry point, a second brain for a coding agent that keeps receipts.
2. [sqlite-graph-memory](https://github.com/tonydzi/sqlite-graph-memory): the memory it runs on.
3. [claude-bible](https://github.com/tonydzi/claude-bible): the rules that keep the agent consistent.
4. [claw-consensus](https://github.com/tonydzi/claw-consensus) and [charm-os](https://github.com/tonydzi/charm-os): several agents and people working together.
5. [verbatim-citation-gate](https://github.com/tonydzi/verbatim-citation-gate): checking that an agent's quotes are real.
6. Connectors: [WhatsApp](https://github.com/tonydzi/whatsapp-mcp-kit) and [Telegram](https://github.com/tonydzi/telegram-mcp-kit).

Everything else is a smaller tool or an experiment, listed in the [catalog](docs/REPOSITORIES.md).

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

**November 2026 so far:** 17 pull requests merged into 12 upstream projects, and [sqlite-graph-memory](https://github.com/tonydzi/sqlite-graph-memory) shipped four releases (v0.3.5 to v0.3.8) on PyPI and became installable as a Claude Code plugin.

- [Google ADK for Go #1299](https://github.com/google/adk-go/pull/1299): workflow node references now go through the same `config_path` containment check as agent references, so a workflow config can no longer load and instantiate a node from anywhere on the filesystem. Merged 10 November 2026.
- [Qwen Code #13312](https://github.com/QwenLM/qwen-code/pull/13312) and [#14855](https://github.com/QwenLM/qwen-code/pull/14855): name the capped MCP server timeout in read-timeout warnings; characterize leader delivery and terminal state per host class in tests. Merged 8 and 16 November 2026.
- [MCP Memory Service #1913](https://github.com/doobidoo/mcp-memory-service/pull/1913), [#1924](https://github.com/doobidoo/mcp-memory-service/pull/1924), [#1923](https://github.com/doobidoo/mcp-memory-service/pull/1923): a three-part series that keeps each memory in its own store on the Cloudflare and hybrid backends, so a per-store credential cannot read another store. Plan agreed with the maintainer first; merged 8 to 10 November 2026.
- [MTEB #5898](https://github.com/embeddings-benchmark/mteb/pull/5898): documentation fix for the random-encoder baseline model name in the dataset guide. Merged 16 November 2026.
- [Microsoft Semantic Kernel #14371](https://github.com/microsoft/semantic-kernel/pull/14371): pin the validated address for Python OpenAPI-plugin requests, closing a check/use gap. Merged 5 October 2026.
- [Google ADK for Go #1543](https://github.com/google/adk-go/pull/1543): images and PDFs (`InlineData`/`FileData` parts) now reach both OpenAI endpoints instead of failing as an unsupported payload; closes #1333, design agreed in the review thread. Merged 16 October 2026.
- [Google Chrome DevTools MCP #2852](https://github.com/ChromeDevTools/chrome-devtools-mcp/pull/2852): documentation fix for which extension tools are available from the CLI. Merged 20 October 2026.
- [NVIDIA SkillSpector #807](https://github.com/NVIDIA/SkillSpector/pull/807): documentation fix for broken source links in the LLM analyzer docs. Merged 14 October 2026.
- [UK AISI Inspect #4769](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4769): decide a grader panel by strict majority rather than mode. Merged 1 September 2026.
- [Obsidian Second Brain #377](https://github.com/eugeniughelbur/obsidian-second-brain/pull/377): flag a source that calls itself unverified but has no source-quality field. Merged 28 October 2026.

## Upstream pull requests, merged and in review

These are contributions to other owners' public repositories. Merged work, open proposals and closed submissions remain distinct in the [full contribution ledger](https://tonydzi.github.io/contributions/).

<!-- PROFILE-ACTIVITY:START -->
Live from the GitHub API, verified 2026-11-19 UTC. Own repositories and awesome-/registry-list entries are not counted.

**87 pull requests merged into 50 upstream projects** (8 of them at large tech companies and labs) · **49 more open in review** across 46 projects · [full list with live status](https://tonydzi.github.io/contributions/)

Merged, large vendors first:

- **microsoft/semantic-kernel**: [1 merged](https://github.com/microsoft/semantic-kernel/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-10-05.
- **google/adk-go**: [2 merged](https://github.com/google/adk-go/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-11-10.
- **ChromeDevTools/chrome-devtools-mcp**: [1 merged](https://github.com/ChromeDevTools/chrome-devtools-mcp/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-10-20.
- **google-gemini/cookbook**: [1 merged](https://github.com/google-gemini/cookbook/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-08-17.
- **NVIDIA/SkillSpector**: [1 merged](https://github.com/NVIDIA/SkillSpector/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-10-14.
- **QwenLM/qwen-code**: [4 merged](https://github.com/QwenLM/qwen-code/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-11-16.
- **bytedance/deer-flow**: [1 merged](https://github.com/bytedance/deer-flow/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-09-30.
- **UKGovernmentBEIS/inspect\_ai**: [1 merged](https://github.com/UKGovernmentBEIS/inspect_ai/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-09-01.
- **doobidoo/mcp-memory-service**: [5 merged](https://github.com/doobidoo/mcp-memory-service/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-11-18.
- **embeddings-benchmark/mteb**: [1 merged](https://github.com/embeddings-benchmark/mteb/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-11-16.
- **osaurus-ai/osaurus**: [1 merged](https://github.com/osaurus-ai/osaurus/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-11-14.
- **zhayujie/CowAgent**: [1 merged](https://github.com/zhayujie/CowAgent/pulls?q=is%3Apr+is%3Amerged+author%3Atonydzi), last 2026-11-09.

In review now:

- **microsoft/semantic-kernel**: [Python: document connector extras and optional dependency compatibility](https://github.com/microsoft/semantic-kernel/pull/14355), opened 2026-09-01.
- **anthropics/claude-cookbooks**: [fix: convert remaining broken sre\_bot\_slack.py links in SRE cookbook](https://github.com/anthropics/claude-cookbooks/pull/799), opened 2026-07-25.
- **openai/openai-cookbook**: [Add cookbook: check citation faithfulness in RAG with a zero-token gate](https://github.com/openai/openai-cookbook/pull/2880), opened 2026-07-24.
- **huggingface/cookbook**: [Add self-verifying search agent recipe](https://github.com/huggingface/cookbook/pull/366), opened 2026-07-24.
- **TencentCloud/TencentDB-Agent-Memory**: [fix\(l2\): cap the agent read tool output to avoid context\_length\_exceeded](https://github.com/TencentCloud/TencentDB-Agent-Memory/pull/1999), opened 2026-11-17.
- **lancedb/vectordb-recipes**: [Add agent memory over a markdown vault example](https://github.com/lancedb/vectordb-recipes/pull/363), opened 2026-11-16.
<!-- PROFILE-ACTIVITY:END -->

## Current research and experiments

- [Persona portability benchmark](https://github.com/tonydzi/persona-portability-benchmark): a frozen persona and memory, tested across models with blind judging and contamination checks. Read the dated results and limitations before comparing scores.
- [Python vulnerability-patching probe](https://github.com/tonydzi/pyvulnpatch-probe): an audit of advisory leakage, fix dates, hint ablations and self-reported success in patching benchmarks.
- [Brain Lite](https://github.com/tonydzi/brain-lite): a small receive-only library for another person's coding agent, with checksummed updates and rollback.
- [Control-plane casebook](https://github.com/tonydzi/agent-control-plane-casebook): reproducible incidents involving schedulers, registries and watchdogs.
- [Deep research collection](https://github.com/tonydzi/deep-research): published research summaries with their questions, findings and source links.

[Preprints, PDFs and DOIs](https://tonydzi.github.io/papers/) · [Full publication list](https://tonydzi.github.io/scholar/publications/)

<details>
<summary>Preprints and versioned research records</summary>

| Research record | DOI |
|---|---|
| One Persona, Eighteen Models | [10.5281/zenodo.23915113](https://doi.org/10.5281/zenodo.23915113) |
| Recovery on Signal or on Schedule? | [10.5281/zenodo.23268660](https://doi.org/10.5281/zenodo.23268660) |
| When Does Graph Expansion Help Personal-Corpus Retrieval? (v0.3) | [10.5281/zenodo.23113066](https://doi.org/10.5281/zenodo.23113066) |
| Instructions That Never Arrive | [10.5281/zenodo.22684968](https://doi.org/10.5281/zenodo.22684968) |
| Silent by Construction | [10.5281/zenodo.22688465](https://doi.org/10.5281/zenodo.22688465) |
| Keeping Agents on a Leash (LEASH-8) | [10.5281/zenodo.22691782](https://doi.org/10.5281/zenodo.22691782) |
| Rules as Files | [10.5281/zenodo.22694070](https://doi.org/10.5281/zenodo.22694070) |
| Facts Before Explanation | [10.5281/zenodo.22696755](https://doi.org/10.5281/zenodo.22696755) |
| Operating a Human-Governed Multi-Machine LLM Agent Fleet | [10.5281/zenodo.22639714](https://doi.org/10.5281/zenodo.22639714) |
| Homeostatic Governance | [10.5281/zenodo.22639712](https://doi.org/10.5281/zenodo.22639712) |
| Le Chatelier Tokenomics | [10.5281/zenodo.22639710](https://doi.org/10.5281/zenodo.22639710) |

Earlier graph-retrieval protocol and pilot: [10.5281/zenodo.22639718](https://doi.org/10.5281/zenodo.22639718). The v0.3 record, *When Does Graph Expansion Help Personal-Corpus Retrieval?*, reports the subsequent execution and its limitations.

The DOI links identify the individual research records; earlier versions remain separately citable.

</details>

## Latest writing

[Clawrush](https://github.com/tonydzi/clawrush) records what was built, what broke and what was learned. The feed below updates automatically. [The Journey](https://github.com/tonydzi/the-journey) is the longer build-in-public book, with human-readable chapters and a machine-readable edition.

<!-- BLOG-POST-LIST:START -->
- [I asked an AI to shrink my CLAUDE.md. I got an 854-row table and an eval that lied to me first](https://github.com/tonydzi/clawrush/blob/main/longreads/canon-as-table-2026-11-18.md) &nbsp;<sub>Nov 18, 2026</sub>
- [Daily longread, 17 November 2026](https://github.com/tonydzi/clawrush/blob/main/longreads/20261117.md) &nbsp;<sub>Nov 18, 2026</sub>
- [How we grow our GitHub: 87 merged PRs in 51 projects, 33 agent lanes, and what four merges in one repo had in common](https://github.com/tonydzi/clawrush/blob/main/longreads/how-we-grow-our-github-2026-11-17.md) &nbsp;<sub>Nov 17, 2026</sub>
- [Daily longread, 16 November 2026](https://github.com/tonydzi/clawrush/blob/main/longreads/20261116.md) &nbsp;<sub>Nov 17, 2026</sub>
- [Daily longread, 13 November 2026](https://github.com/tonydzi/clawrush/blob/main/longreads/20261113.md) &nbsp;<sub>Nov 16, 2026</sub><!-- BLOG-POST-LIST:END -->

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
