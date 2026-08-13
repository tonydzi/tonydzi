<!--
  This is the profile README of github.com/tonydzi.
  Heads-up for whoever renames the account: every badge, widget and raw URL below
  hard-codes the login "tonydzi". A rename silently breaks them
  (shields.io and the stats widgets just render an error card). Grep for the login
  and rewrite it in the same commit as the rename.
  The "Latest writing" block is generated — see .github/workflows/blog-post-workflow.yml.
-->

<h1 align="center">Anton Dziatkovskii</h1>

<p align="center">
  <b>AI Research Builder</b> — building a multi-agent lab, publishing the artifacts from running it daily.<br>
  <sub>One non-technical founder + an AI cofounder + a fleet of Claude machines that reach consensus without me.</sub>
</p>

<p align="center">
  <a href="https://github.com/tonydzi?tab=followers"><img alt="Followers" src="https://img.shields.io/github/followers/tonydzi?style=flat-square&logo=github&label=followers&color=1f6feb"></a>
  <a href="https://orcid.org/0000-0001-7408-3054"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-0000--0001--7408--3054-a6ce39?style=flat-square&logo=orcid&logoColor=white"></a>
  <a href="https://x.com/Tony_Stef_"><img alt="X" src="https://img.shields.io/badge/X-@Tony__Stef__-000000?style=flat-square&logo=x&logoColor=white"></a>
  <a href="https://t.me/ClawEng"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-@ClawEng-229ED9?style=flat-square&logo=telegram&logoColor=white"></a>
  <img alt="License" src="https://img.shields.io/badge/everything%20here-MIT-3da639?style=flat-square&logo=opensourceinitiative&logoColor=white">
</p>

> 👤 **Hiring manager or engineer? [START HERE — one page of proof →](https://palo-alto-ai-research-lab.github.io/)**
>
> 🧩 **Everything we built, part by part → [SYSTEM.md](https://github.com/tonydzi/tonydzi/blob/main/SYSTEM.md)** — 20 repos, what each one does, how they fit together.
>
> 📄 Resume: **[PDF](https://palo-alto-ai-research-lab.github.io/resume.pdf)** · [JSON Resume](https://palo-alto-ai-research-lab.github.io/resume.json) — 🎓 Research: **[academic profile](https://palo-alto-ai-research-lab.github.io/scholar/)** · [full publication list](https://palo-alto-ai-research-lab.github.io/scholar/publications/)

---

## 🔨 What I'm building right now

- **A second brain that survives a context reset** — facts in SQL, meaning in embeddings, relations in a graph, one SQLite file, no infrastructure. → [`sqlite-graph-memory`](https://github.com/tonydzi/sqlite-graph-memory)
- **A fleet that negotiates instead of drifting** — hub, laptops, family machines and a VPS anchor run propose → counter → accept → commit, and wake the human only for money or the irreversible. → [`claude-consensus`](https://github.com/tonydzi/claude-consensus)
- **Deterministic gates around the model, not better prompts inside it** — citation checks, authority routing, an 8-domain leash for delegated authority. → [`verbatim-citation-gate`](https://github.com/tonydzi/verbatim-citation-gate) · [`agent-leash`](https://github.com/tonydzi/agent-leash)
- **A reliability bench for agent runtimes** — replay, idempotency and consensus-integrity scenarios distilled from real fleet incidents, not from a whiteboard. → [`agent-runtime-integrity-bench`](https://github.com/tonydzi/agent-runtime-integrity-bench)
- **The whole thing written down as it happens** — a build-in-public book and an English diary, updated the day something breaks. → [`the-journey`](https://github.com/tonydzi/the-journey) · [`clawrush`](https://github.com/tonydzi/clawrush)

## 📌 Four to start with

| | What it is | Why you'd care |
|---|---|---|
| **[claude-bible](https://github.com/tonydzi/claude-bible)** | One behavioral rulebook every actor obeys — the founder, human assistants, and every Claude in the fleet | Your agents behave the same across repos, sessions and people, because the law lives outside the prompt |
| **[claude-consensus](https://github.com/tonydzi/claude-consensus)** | Cross-machine consensus protocol: dual-rail bus, ACK discipline, heartbeat failover, self-healing sync | Run agents on several machines without state drift, and without a human courier between them |
| **[sqlite-graph-memory](https://github.com/tonydzi/sqlite-graph-memory)** | Graph RAG on plain SQLite: vector retrieval + curated wiki-links, zero infra | Agent memory that outlives the context window and that you can open with `sqlite3` |
| **[verbatim-citation-gate](https://github.com/tonydzi/verbatim-citation-gate)** | Zero-token verbatim check + burden-of-proof judge for RAG answers | Fabricated citations get caught before the user sees them; framework-agnostic, MIT |
| **[verdict-contract](https://github.com/tonydzi/verdict-contract)** | Your LLM reviewer said APPROVE - did it? Prompt rule, parser and exit-code gate in one stdlib file | A review whose verdict never reaches the exit status is a log line, not a gate. 42 counterexamples included |

Also here: [`agent-leash`](https://github.com/tonydzi/agent-leash) (LEASH-8 control model) · [`charm-os`](https://github.com/tonydzi/charm-os) (MCP read-broker) · [`second-brain-starter-kit`](https://github.com/tonydzi/second-brain-starter-kit) (101 skills + a working CRM engine).

<!--kits-series:start-->

## 🧰 Connector & Ops Kits

Eight kits, all published 2026-08-10, each lifted out of the same live fleet after it
survived production rather than written as a demo. They are independent: take one, ignore
the rest. All stdlib-only Python, all free.

| kit | what it solves |
|---|---|
| [`telegram-mcp-kit`](https://github.com/tonydzi/telegram-mcp-kit) | Connect your agent to your own Telegram account in ~15 minutes, with the production patches and every gotcha |
| [`whatsapp-mcp-kit`](https://github.com/tonydzi/whatsapp-mcp-kit) | Link WhatsApp, using a live self-refreshing QR page that makes pairing actually work |
| [`mcp-daemon-diet`](https://github.com/tonydzi/mcp-daemon-diet) | One shared MCP daemon per machine instead of a stdio copy in every session, with a watchdog that will not blind your live sessions |
| [`agent-approval-gate`](https://github.com/tonydzi/agent-approval-gate) | Your agent needs a human's OK and nobody is at the terminal: the ask goes to a messenger, the answer comes back into the run |
| [`fleet-deploy`](https://github.com/tonydzi/fleet-deploy) | Roll a fix to N machines and prove it landed on each one: canary waves and a verify that must read a fact back |
| [`secondop-panel`](https://github.com/tonydzi/secondop-panel) | Nobody reviews themselves, and one reviewer model is one blind spot: fan a change out to several model families with quorum and honest skips |
| [`oss-publish`](https://github.com/tonydzi/oss-publish) | Open up internal work without leaking it: plausible substitutions of the same shape, then a fail-closed gate over the whole tree |
| [`llm-spend-audit`](https://github.com/tonydzi/llm-spend-audit) | What your own wiring charges on every session, and which paid subscriptions are going undrawn |

<!--kits-series:end-->

## 🧰 Stack

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white">
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&logo=anthropic&logoColor=white">
  <img alt="MCP" src="https://img.shields.io/badge/MCP-000000?style=flat-square&logo=modelcontextprotocol&logoColor=white">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white">
  <img alt="Bash" src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white">
  <img alt="Telegram API" src="https://img.shields.io/badge/Telegram%20API-229ED9?style=flat-square&logo=telegram&logoColor=white">
  <img alt="Obsidian" src="https://img.shields.io/badge/Obsidian-7C3AED?style=flat-square&logo=obsidian&logoColor=white">
  <img alt="macOS" src="https://img.shields.io/badge/macOS-000000?style=flat-square&logo=apple&logoColor=white">
  <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
  <img alt="Windows" src="https://img.shields.io/badge/Windows-0078D4?style=flat-square&logo=windows&logoColor=white">
</p>

Python and SQLite for everything that has to survive a crash; Claude Code as the runtime; MCP for tools; GitHub Actions and cron for the routines. The house rule is **AK-47**: the simplest thing that works and that a non-technical founder can repair with a hammer and a screwdriver.

## ✍️ Latest writing

Essays from the fleet — what was built, what broke, what was learned. Pulled automatically from [`clawrush`](https://github.com/tonydzi/clawrush) ([RSS](https://github.com/tonydzi/clawrush/raw/main/feed.xml)).

<!-- BLOG-POST-LIST:START -->- [Two Days to Burn a Subscription](https://github.com/Palo-Alto-AI-Research-Lab/clawrush/blob/main/longreads/session-map-and-burning-limits.md) &nbsp;<sub>Aug 13, 2026</sub>
- [A Recipe Beats a Prohibition](https://github.com/Palo-Alto-AI-Research-Lab/clawrush/blob/main/longreads/superpowers-measured-their-rules.md) &nbsp;<sub>Aug 13, 2026</sub>
- [n8n or a Session: Where the Line Actually Falls](https://github.com/Palo-Alto-AI-Research-Lab/clawrush/blob/main/longreads/n8n-or-a-session.md) &nbsp;<sub>Aug 13, 2026</sub>
- [Link the Sessions, Not the Notes](https://github.com/Palo-Alto-AI-Research-Lab/clawrush/blob/main/longreads/link-sessions-not-notes.md) &nbsp;<sub>Aug 12, 2026</sub>
- [Where My Sessions Went](https://github.com/Palo-Alto-AI-Research-Lab/clawrush/blob/main/longreads/where-my-sessions-went.md) &nbsp;<sub>Aug 12, 2026</sub>
<!-- BLOG-POST-LIST:END -->

## 📖 The book

**[相棒 AIBŌ · The Partner](https://github.com/tonydzi/the-journey)** — a build-in-public book of the whole journey, day by day, since 2026-05-27. How a non-technical founder and an AI built a second brain: what we tried, what broke, what we learned. Two forms side by side: a story for humans (RU/EN) and [`llms-full.txt`](https://github.com/tonydzi/the-journey/blob/main/llms-full.txt) for machines — point your coding agent at it and it inherits our patterns and skips our mistakes.

## 🔁 Contributing upstream

**37 pull requests into 26 repositories across 24 organisations** — Anthropic, OpenAI, Google, Microsoft, Mistral, Cohere, Hugging Face, xAI, Qwen, deepset, and the agent-ecosystem lists. 33 open, 4 closed, **0 merged so far** *(verified 2026-08-01)*.

📋 **[The full list, with live status →](https://palo-alto-ai-research-lab.github.io/contributions/)** — generated straight from the GitHub API, closed ones included. Nothing is left off it to make the record look better.

Representative work in flight:

| PR | What it proposes |
|---|---|
| [anthropics/claude-cookbooks#787](https://github.com/anthropics/claude-cookbooks/pull/787) | Authority routing — ADVISE / EXECUTE / DEFER / STOP as a gate on agent actions. |
| [anthropics/claude-cookbooks#778](https://github.com/anthropics/claude-cookbooks/pull/778) | *Coordinating agents that don't share memory* — message-bus consensus + liveness. |
| [anthropics/claude-cookbooks#788](https://github.com/anthropics/claude-cookbooks/pull/788) | Pipeline vs barrier sub-agent composition — when a barrier actually earns its wall-clock cost. |
| [anthropics/claude-agent-sdk-demos#70](https://github.com/anthropics/claude-agent-sdk-demos/pull/70) | `verified-ops-agent` — propose → adversarial verify → execute, as a runnable demo. |
| [openai/openai-cookbook#2880](https://github.com/openai/openai-cookbook/pull/2880) | Zero-token check for fabricated citations in RAG. |
| [huggingface/cookbook#366](https://github.com/huggingface/cookbook/pull/366) | A self-verifying search agent — the agent checks its own retrieval before answering. |
| [anthropics/skills#1460](https://github.com/anthropics/skills/pull/1460) | `reasoning-quality-gate` skill. |
| [google/adk-python-community#172](https://github.com/google/adk-python-community/pull/172) | `AuthorityRoutingPlugin` for ADK. |

The pattern behind most of them is the same one that runs in production here: **a deterministic gate around the model, not a better prompt inside it.**

The most useful response so far was a rejection: [deepset-ai/haystack#12142](https://github.com/deepset-ai/haystack/pull/12142) was closed by a maintainer with an actual review — not enough added value to justify the new component. A reviewed no beats a silent queue, and it is on the list above like everything else.

## 📊 The numbers, unedited

<p align="center">
  <img alt="GitHub activity, community and repository stats" src="/metrics.svg">
</p>

<sub>Rendered nightly from the GitHub API by <a href="https://github.com/tonydzi/tonydzi/blob/main/.github/workflows/metrics.yml">a workflow in this repo</a> and committed as an SVG — not hotlinked from a public widget host, because on 2026-08-01 the usual two (github-readme-stats, github-profile-trophy) were answering 503 and 402. Achievement badges are GitHub's own, on the profile sidebar. The full contribution record is on <a href="https://palo-alto-ai-research-lab.github.io/contributions/">the contributions page</a>, generated straight from the API.</sub>

## 👤 Who's behind this

**Anton Dziatkovskii** (Tony) — founder, non-technical — and **Mike**, his AI cofounder running on Claude Code. Every repo here is extracted from a live production system: an always-on hub, laptops, family machines and a VPS anchor that talk to each other, reach consensus autonomously, and self-heal their own sync.

Anton has done developer activation for a frontier platform before — when smart contracts were where LLM agents are now: Solidity curricula and a dev incubator with 40+ engineers across APAC, hackathons and cohorts at Platinum VC & Incubator ($35M AUM). CS security (MEPhI), ~20 academic papers, PhD in Education (IT). Full page: [palo-alto-ai-research-lab.github.io](https://palo-alto-ai-research-lab.github.io/) · [resume (PDF)](https://palo-alto-ai-research-lab.github.io/resume.pdf) · [academic profile](https://palo-alto-ai-research-lab.github.io/scholar/).

Academic identity: Anton publishes as **Anton Dziatkovskii** ([ORCID 0000-0001-7408-3054](https://orcid.org/0000-0001-7408-3054), [Google Scholar](https://scholar.google.com/citations?user=b8gKHiMAAAAJ), [Academia.edu](https://tylip.academia.edu/AntonDziatkovskii)).

*AI collaboration policy, honest by design: built with Claude as implementation collaborator. Anton owns problem framing, architecture, evaluation, product decisions and final QA. No fabricated experience; metrics are published or absent.*

## AI contributors

This project is built by a human + AI team, and the git log says so: Claude
writes most of the code, Codex and Grok review it, Gemini feeds the research.
Each is credited on a commit **only if its output changed that commit's
content** — no decorative credits. Lab-wide policy, one source for every repo:
[AI-CONTRIBUTORS.md](https://github.com/tonydzi/.github/blob/main/AI-CONTRIBUTORS.md).

## 📬 Contact

Questions, war stories, or you want to test-drive any of this with your own fleet:

- 💬 WhatsApp: **+1 341 222 9178**
- 🐦 X: [@Tony_Stef_](https://x.com/Tony_Stef_)
- 📣 Telegram: [@ClawRus](https://t.me/ClawRus) (RU) · [@ClawEng](https://t.me/ClawEng) (EN)
- 💼 Wellfound: [anton-dziatkovskii-3](https://wellfound.com/u/anton-dziatkovskii-3)

If something here helps you, a star is the currency that keeps it free.

---

<!--ecosystem-map:start-->

## 🧩 One piece of a working system

This repository is one piece lifted out of a live operation: one non-technical founder, an AI
cofounder, and a fleet of machines that reach consensus with each other and wake the human only
for money or the irreversible. It was extracted after it survived production, not written as a
demo — and it runs on its own: nothing here phones home to the rest.

**See how the whole thing fits together → [SYSTEM.md](https://github.com/tonydzi/tonydzi/blob/main/SYSTEM.md)**

<!--ecosystem-map:end-->
