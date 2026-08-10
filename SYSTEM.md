# The system, part by part

One link to answer "what do you actually do".

There is one live operation here: a non-technical founder, an AI cofounder, and a fleet of
machines — an always-on hub, laptops, family machines and a VPS anchor — that reach consensus
with each other and wake the human only for money or the irreversible. Every public repo below
was **cut out of that running system**, not written as a demo. That is the only reason any of it
is worth your time: it already survived a night shift.

Each piece is small on purpose and stands alone. Take one, ignore the rest.

**Rule of the house — AK-47:** the simplest thing that works and that a non-technical founder can
repair with a hammer and a screwdriver. Python and SQLite where it must survive a crash, no
service you have to run, no key you have to buy.

---

## How the pieces fit

```
                    ┌───────────────────────────────┐
   how agents  ───► │  GOVERNANCE   claude-bible     │  rules live outside the prompt
   are allowed      │               agent-leash      │  8 domains of delegated authority
   to behave        │               charm-os         │  humans and agents as relationships
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
   what they    ───►│  MEMORY       sqlite-graph-memory   facts in SQL, meaning in vectors
   remember         │               second-brain-starter-kit
                    │               voice2brain      │  voice in, linked markdown out
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
   what proves  ───►│  GATES        verbatim-citation-gate   fabricated citations
   they did it      │               verdict-contract         "APPROVE" that reaches exit code
                    │               claim-check              every number bound to its artifact
                    │               verified-ops-starter     exit 0 is not evidence
                    │               agent-runtime-integrity-bench
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
   how the      ───►│  FLEET        claude-consensus │  propose → counter → accept → commit
   fleet runs       │               claude-mac-patrol│  the janitor for agent machines
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
   what they    ───►│  CONNECTORS   telegram-mcp-kit │  your own Telegram, in ~15 minutes
   reach into       │                                │  (whatsapp-mcp-kit next)
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
   said out     ───►│  IN PUBLIC    the-journey · clawrush · dashboards · cofounder
   loud             │               awesome-verified-agents
                    └───────────────────────────────┘
```

The direction matters: a gate is worthless if the governance layer never told the agent what it
may do, and governance is theatre if no gate can prove what actually happened.

---

## Governance — what an agent is allowed to do

| Repo | What it is | Take it if |
|---|---|---|
| **[claude-bible](https://github.com/Palo-Alto-AI-Research-Lab/claude-bible)** | Rules-as-files governance with precedence, a declined-decisions journal, objection sparring | Your agents behave differently in every repo, session and pair of hands |
| **[agent-leash](https://github.com/Palo-Alto-AI-Research-Lab/agent-leash)** | LEASH-8: an 8-domain control model for delegated authority, with a scorecard and the plan-vs-authorize pattern | You are about to give an agent a credential and want to bound the blast radius first |
| **[charm-os](https://github.com/Palo-Alto-AI-Research-Lab/charm-os)** | CharmOS — humans *and* AI agents as first-class relationships on a personal second brain, driven by the recall→deep-research loop | Your CRM has rows for people and nothing for the machines doing the work |

## Memory — what survives the context window

| Repo | What it is | Take it if |
|---|---|---|
| **[sqlite-graph-memory](https://github.com/Palo-Alto-AI-Research-Lab/sqlite-graph-memory)** | Graph RAG on plain SQLite: vector retrieval + a hand-curated wikilink graph + cross-encoder rerank, plus a zero-token per-turn ledger | You want agent memory you can open with `sqlite3` and no vector database to operate |
| **[second-brain-starter-kit](https://github.com/Palo-Alto-AI-Research-Lab/second-brain-starter-kit)** | The method, not the data: 101 skills, a working CRM engine, vault templates, the handover map | You want to run Claude Code as a second brain and would rather not rediscover the layout |
| **[voice2brain](https://github.com/Palo-Alto-AI-Research-Lab/voice2brain)** | Four small Python scripts: voice note → text → linked, tagged, searchable markdown | You think out loud and lose it by evening |

## Gates — evidence instead of trust

| Repo | What it is | Take it if |
|---|---|---|
| **[verbatim-citation-gate](https://github.com/Palo-Alto-AI-Research-Lab/verbatim-citation-gate)** | Zero-token verbatim check plus a burden-of-proof judge, framework-agnostic | Your RAG answer cites a passage that does not exist in the source |
| **[verdict-contract](https://github.com/Palo-Alto-AI-Research-Lab/verdict-contract)** | Prompt rule + parser + exit-code gate in one stdlib file, with the 42 counterexamples that forced every line | Your LLM reviewer says APPROVE into a log nobody reads and CI stays green |
| **[claim-check](https://github.com/Palo-Alto-AI-Research-Lab/claim-check)** | Bind every published number to the artifact it came from; CI fails when they drift. No LLM, no key, no dependencies | Your README claims a benchmark number from three months ago |
| **[verified-ops-starter](https://github.com/Palo-Alto-AI-Research-Lab/verified-ops-starter)** | Three stdlib checks: output freshness, silent no-op detection, rollout proof by reading the fact back | You have a scheduled job that exits 0 and has quietly done nothing for a week |
| **[agent-runtime-integrity-bench](https://github.com/Palo-Alto-AI-Research-Lab/agent-runtime-integrity-bench)** | Deterministic fault-injection scenarios against real SDKs, distilled from actual fleet incidents | You want to know how your runtime fails before it fails on a customer |

## Fleet — many machines, one mind

| Repo | What it is | Take it if |
|---|---|---|
| **[claude-consensus](https://github.com/Palo-Alto-AI-Research-Lab/claude-consensus)** | Consensus protocol (propose / counter / accept / commit), dual-rail message bus, ACK discipline, self-healing sync | You run agents on more than one machine and a human is the courier between them |
| **[claude-mac-patrol](https://github.com/Palo-Alto-AI-Research-Lab/claude-mac-patrol)** | A dependency-free janitor for machines running Claude Code, plus the field procedure it came from | Your Mac is not old, it is holding thirty half-dead agent sessions |

## Connectors — what the agents can actually reach

| Repo | What it is | Take it if |
|---|---|---|
| **[telegram-mcp-kit](https://github.com/Palo-Alto-AI-Research-Lab/telegram-mcp-kit)** | Connect Claude to **your own** Telegram account in ~15 minutes: a paste-in install prompt for Claude Code/Codex, the patches we run in production (one shared daemon per machine instead of a copy per session, six extra search tools, multi-account), a watchdog, and ten dated gotchas. Built on upstream [`chigwell/telegram-mcp`](https://github.com/chigwell/telegram-mcp) | Your agent writes code all day but cannot read the chat where the work is actually decided |

## In public — the work, said out loud

| Repo | What it is |
|---|---|
| **[the-journey](https://github.com/Palo-Alto-AI-Research-Lab/the-journey)** | A build-in-public book of the whole collaboration, day by day. Two voices, human-readable and machine-readable — point your agent at `llms-full.txt` and it inherits the patterns and skips the mistakes |
| **[clawrush](https://github.com/Palo-Alto-AI-Research-Lab/clawrush)** | The English diary and longreads: what was built, what broke, what it cost. RU edition on Telegram [@ClawRus](https://t.me/ClawRus) |
| **[dashboards](https://github.com/Palo-Alto-AI-Research-Lab/dashboards)** | The panels we actually stare at while the fleet runs |
| **[awesome-verified-agents](https://github.com/Palo-Alto-AI-Research-Lab/awesome-verified-agents)** | A curated list with a hard inclusion bar: name the artifact a human can inspect later |
| **[cofounder](https://github.com/Palo-Alto-AI-Research-Lab/cofounder)** | The open call — what we are looking for and what you get |

---

## Everything is MIT, and there is no catch

Take it, fork it, ship it in a product, do not credit us. If a piece saves you a bad week, a star
is how the next person finds it — that is the whole price.

Contributions: issues labelled `accepted` are scoped and free to take, comment **"claiming this"**
and it is yours for seven days. No CLA, ever — you keep the copyright to your code. We answer
every issue and PR within 48 hours including "no, and here is why"; our silence is our bug, so
ping the thread. Full deal in
[CONTRIBUTING.md](https://github.com/Palo-Alto-AI-Research-Lab/.github/blob/main/CONTRIBUTING.md).

## Who is behind it

**Anton Dziatkovskii** (Tony), founder, non-technical — and **Mike**, his AI cofounder running on
Claude Code. The git log is honest about which of us wrote what: lab-wide policy in
[AI-CONTRIBUTORS.md](https://github.com/Palo-Alto-AI-Research-Lab/.github/blob/main/AI-CONTRIBUTORS.md).

Want to run any of this on your own fleet, or have a war story to trade:

- 💬 WhatsApp **+1 341 222 9178**
- 📣 Telegram [@ClawEng](https://t.me/ClawEng) (EN) · [@ClawRus](https://t.me/ClawRus) (RU)
- 🐦 X [@Tony_Stef_](https://x.com/Tony_Stef_)
- 🌐 [palo-alto.ai](https://palo-alto.ai) · [START HERE — one page of proof](https://palo-alto-ai-research-lab.github.io/)
