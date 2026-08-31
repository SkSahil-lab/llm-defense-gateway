# 🔵 LLM Defense Gateway

Phase 2 of a 3-phase AI Application Security build — defense engineering for every attack proven in Phase 1.

## Why this exists

[`llm-redteam-framework`](https://github.com/SkSahil-lab/llm-redteam-framework) proved 10/10 OWASP LLM Top 10 (2026) categories with working exploits. This repo builds the countermeasure for each one, from scratch — and proves it works by running the *exact same attack payloads* from Phase 1 against the new defense.

**The standard for "done" here isn't a description of what a defense should do — it's the original exploit, re-run, now showing `BLOCKED` instead of `SUCCEEDED`.**

## Structure

```
llm-defense-gateway/
├── day11-llm01-prompt-injection-defense/
│   ├── defense_day11.py       # PromptInjectionGuard - the defense itself
│   └── test_day11.py          # Re-runs Day 2's real attack payloads against it
├── DEFENSE_SCORECARD.md       # Running score: how many defenses complete
└── README.md
```

Each `dayNN-*` folder is self-contained — a `defense_dayNN.py` implementing one countermeasure, and a `test_dayNN.py` that imports it and checks it against real attack payloads pulled directly from the matching day in `llm-redteam-framework`.

## Why no Docker this phase

Phase 1 already proved containerization and multi-container networking extensively (Days 1-10). Repeating that daily here would add overhead without teaching anything new. This phase is pure Python — one command to run, one command to verify — so the focus stays entirely on the security logic itself. Docker and Kubernetes return in Phase 3, where they actually matter for a deployable capstone.

## How to run any day

```bash
cd dayNN-<category-name>
python test_dayNN.py
```

Output shows every attack payload with a BLOCKED/ALLOWED verdict, plus baseline (normal) messages confirmed to still pass through — proving the defense stops attacks without breaking legitimate use.

## Progress

| Day | Defends Against | Status |
|---|---|---|
| 11 | LLM01 Prompt Injection | ✅ Complete — 3/3 attacks blocked, 0 false positives |

See [DEFENSE_SCORECARD.md](./DEFENSE_SCORECARD.md) for full detail.

## Project Roadmap

| Phase | Focus | Status | Repo |
|---|---|---|---|
| 🔴 Phase 1 — Red Team | Attack every OWASP LLM Top 10 (2026) category | ✅ Complete (10/10) | [`llm-redteam-framework`](https://github.com/SkSahil-lab/llm-redteam-framework) |
| 🔵 Phase 2 — Blue Team (this repo) | Defend against every attack from Phase 1 | 🔄 In progress | `llm-defense-gateway` |
| 🟣 Phase 3 — Capstone SaaS | Unified attack + defense platform, deployed on Kubernetes | ⏳ Planned | `llm-attack-defense-saas` |

**Interactive architecture map** (all 3 phases, click-through explanations): https://sksahil-lab.github.io/architecture-map/

---
Built and documented daily as part of a public AI AppSec learning sprint.
