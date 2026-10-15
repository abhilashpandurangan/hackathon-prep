# DEMO_SCRIPT.md template

Copy this file into your hackathon repo as `docs/DEMO_SCRIPT.md` and fill it
in before the event. Rehearse it twice against the clock.

## The 3-minute demo

| Time | Beat | Exact input | Expected output | If it fails |
|---|---|---|---|---|
| 0:00-0:20 | Hook | Say the one-person, one-number opener | - | - |
| 0:20-0:40 | Problem | Say the sourced number | - | - |
| 0:40-1:40 | Live demo, beat 1 | Type/click: ... | Shows: ... | Fallback: cached output in `demo/fallback-1/` |
| 1:40-2:20 | Live demo, beat 2 | Type/click: ... | Shows: ... | Fallback: cached output in `demo/fallback-2/` |
| 2:20-2:40 | The number | Say the quantified result | - | - |
| 2:40-3:00 | Vision | Say the 6-month vision and the ask | - | - |

## Fallback plan

- Every live API call has a cached response committed in `demo/fallbacks/`.
  The UI checks the API first and serves the cache silently on failure.
- Pre-run all inputs once on venue WiFi during setup. Screenshot each
  expected output and keep them open in tabs as a last resort.
- If the demo dies completely: narrate the screenshots, name what broke,
  and finish the pitch. A composed recovery beats a silent collapse.

## Red-team checks (run before the demo)

- [ ] Duplicate input: system refuses or dedups, does not double-count
- [ ] Adversarial input: prompt injection attempt is refused with a reason
- [ ] Changed details mid-flow: system flags the inconsistency
- [ ] Empty/malformed input: system fails closed with a clear message
