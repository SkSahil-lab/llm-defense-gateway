# Defense Scorecard — Phase 2

Tracking each OWASP category from Phase 1, and whether the matching defense blocks the original exploit.

| Day | Category | Defense | Attack Blocked? |
|---|---|---|---|
| 11 | LLM01 Prompt Injection | `PromptInjectionGuard` — pattern-based override/leak detection | ✅ 3/3 attack payloads blocked, 0/3 false positives |

| 12 | LLM02 Sensitive Information Disclosure | `SafeErrorHandler` — catches exceptions, returns generic message to user, logs full detail internally | ✅ Blocked Day 3's exploit — 0 credentials leaked, error still captured internally |

| 13 | LLM03 Excessive Agency | `AgencyLimitGuard` — hard cap on refund amounts, mandatory human approval for irreversible actions | ✅ Blocked Day 7's exploit — $999,999 refund and account deletion both queued for approval instead of auto-executing |

