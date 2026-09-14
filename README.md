# 🔵 LLM Defense Gateway

Phase 2 of a 3-phase AI Application Security build — defense engineering for every attack proven in Phase 1.

> **Phase 2 status: ✅ Complete — 9/9 defenses, each one proven against the exact Phase 1 exploit it defends.**

## Why this exists

[`llm-redteam-framework`](https://github.com/SkSahil-lab/llm-redteam-framework) proved 10/10 OWASP LLM Top 10 (2026) categories with working exploits. This repo builds the countermeasure for each one, from scratch — and proves it works by running the *exact same attack payloads* from Phase 1 against the new defense.

**The standard for "done" here isn't a description of what a defense should do — it's the original exploit, re-run, now showing `BLOCKED` instead of `SUCCEEDED`.**

## Structure

```
llm-defense-gateway/
├── day11-llm01-prompt-injection-defense/
├── day12-llm02-sensitive-info-defense/
├── day13-llm03-excessive-agency-defense/
├── day14-llm04-supply-chain-defense/
├── day15-llm05-data-poisoning-defense/
├── day16-llm06-llm07-consumption-misinfo-defense/
├── day17-llm08-hidden-context-defense/
├── day18-llm09-vector-embedding-defense/
├── day19-llm10-output-handling-defense/
├── DEFENSE_SCORECARD.md       # Full detail on every defense and result
└── README.md
```

Each `dayNN-*` folder is self-contained — a `defense_dayNN.py` implementing one countermeasure, and a `test_dayNN.py` that imports it and checks it against real attack payloads pulled directly from the matching day in `llm-redteam-framework`.

**Note on Day 16:** LLM06 (Unbounded Consumption) and LLM07 (Misinformation) are combined because they were originally paired in Phase 1 (Day 9) as the two lighter builds sharing one day. Phase 2 mirrors Phase 1's day structure exactly, so that pairing carried forward here too.

## Why no Docker this phase

Phase 1 already proved containerization and multi-container networking extensively (Days 1-10). Repeating that daily here would add overhead without teaching anything new. This phase is pure Python — one command to run, one command to verify — so the focus stays entirely on the security logic itself. Docker and Kubernetes return in Phase 3, where they actually matter for a deployable capstone.

## How to run any day

```bash
cd dayNN-<category-name>
python test_dayNN.py
```

Output shows every attack payload with a BLOCKED/ALLOWED verdict, plus baseline (normal) messages confirmed to still pass through — proving the defense stops attacks without breaking legitimate use.

## Progress — Phase 2 complete (9/9)

| Day | Defends Against | Status |
|---|---|---|
| 11 | LLM01 Prompt Injection | ✅ Complete — 3/3 attacks blocked, 0 false positives |
| 12 | LLM02 Sensitive Information Disclosure | ✅ Complete — 0 credentials leaked, error logged internally |
| 13 | LLM03 Excessive Agency | ✅ Complete — $999,999 refund + account deletion routed to human approval |
| 14 | LLM04 Supply Chain | ✅ Complete — compromised plugin code never executed, hash mismatch caught pre-execution |
| 15 | LLM05 Data and Model Poisoning | ✅ Complete — poisoned fact stayed unreachable, approved facts served normally |
| 16 | LLM06 Unbounded Consumption + LLM07 Misinformation | ✅ Complete — loop capped at 5 iterations, ungrounded questions refused |
| 17 | LLM08 Hidden Context Exposure | ✅ Complete — internal context structurally unreachable, both attack phrasings blocked |
| 18 | LLM09 Vector & Embedding Weaknesses | ✅ Complete — poisoned document quarantined, never a retrieval candidate |
| 19 | LLM10 Improper Output Handling | ✅ Complete — script tags rendered as inert text via HTML escaping |

See [DEFENSE_SCORECARD.md](./DEFENSE_SCORECARD.md) for full detail, including the six distinct control types used across the nine defenses.

## Project Roadmap

| Phase | Focus | Status | Repo |
|---|---|---|---|
| 🔴 Phase 1 — Red Team | Attack every OWASP LLM Top 10 (2026) category | ✅ Complete (10/10) | [`llm-redteam-framework`](https://github.com/SkSahil-lab/llm-redteam-framework) |
| 🔵 Phase 2 — Blue Team (this repo) | Defend against every attack from Phase 1 | ✅ Complete (9/9) | `llm-defense-gateway` |
| 🟣 Phase 3 — Capstone SaaS | Unified attack + defense platform, deployed on Kubernetes | ⏳ Starting next | `llm-attack-defense-saas` |

**Interactive architecture map** (all 3 phases, click-through explanations): https://sksahil-lab.github.io/architecture-map/

---
Built and documented daily as part of a public AI AppSec learning sprint.