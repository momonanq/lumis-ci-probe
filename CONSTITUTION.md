# 🏛️ CONSTITUTION: Probe
> Boundaries set by the founder on 2026-09-29 (LUMIS scope guard skill, no model involved — every line is the founder's own).

## 📜 ARTICLE I: EXPLICIT NON-GOALS (set by the founder)
- ⛔ **FORBIDDEN:** No payments or billing of any kind (Stripe, PayPal, crypto)
- ⛔ **FORBIDDEN:** No native iOS/Android apps

## 📜 ARTICLE II: APPROVED STACK
- **Approved stack (mandated by the founder):** Python 3.12, FastAPI

## 📜 ARTICLE III: REQUIRED INVARIANTS
- (none declared)

## 📜 ARTICLE IV: DRIFT RULE
If a request or your own plan contains "quick fix for now", "while I'm in here", "might as well" — stop and ask: is this inside the specification? y/n.
A change that touches Article I or III is a Feature Delta: ask the founder, never improvise. The hooks in `.claude/settings.json` run
`scripts/scope_guard.py` on every edit and block the triggers listed in `.lumis/scope_guard.json`.
