<!-- LUMIS scope guard (generated; edit .lumis/scope_guard.json instead) -->
## Boundaries of Probe (LUMIS scope guard)

Before the first edit: list the loaded rule files (.cursorrules, CLAUDE.md, CONSTITUTION.md) and active hooks, restate the Non-Goals below, wait for confirmation.

### Non-Goals (never implement, never suggest)
- No payments or billing of any kind (Stripe, PayPal, crypto)
- No native iOS/Android apps

### Stack (user-mandated; do not add servers, frameworks or build steps beyond it)
- Python 3.12, FastAPI

### Guard
`.claude/settings.json` runs `scripts/scope_guard.py` before every edit and command; a Non-Goal trigger is blocked with the boundary named (NG-n). Events land in `.lumis/guard.log` (`python scripts/scope_guard.py report`). Never edit the hook or the deny rules to get past them.
If the request or your own plan contains 'quick fix for now', 'while I'm in here', 'might as well', 'заодно', 'на всякий случай' — stop and ask: is this in scope? y/n.
<!-- end LUMIS scope guard -->
