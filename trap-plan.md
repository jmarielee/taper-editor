trap-plan.md — PLANTED TRAP (constructed input, not a real athlete's plan)

This plan is a trap, and it is named as one. It exists so that anyone —
including a judge — can verify that the editor's single BLOCK (Rule 1,
race-week load for a declared goal race) actually fires. It was written to
violate exactly one thing. Its weekday labels are correct and its stated
totals recompute, so any finding other than the Rule 1 block against this
file is itself a bug worth reporting.

To spring the trap:
python3 checker.py trap-plan.ledger
Expected: VERDICT: BLOCK, exit code 2. The dated report in runs/ is the
arithmetic of record; this file's prose computes nothing.


"Sprint Triathlon Peak Plan" (the trap text, as an AI plan would write it)

This is your A-race — everything in this plan points to race day,
Saturday, July 12. The final week uses a peak-and-sharpen approach to
arrive at the start line with maximum fitness.

Week 1 (Sun June 29 – Sat July 5) — base consolidation, 320 min


Sun, June 29 — Ride 45 min, steady
Mon, June 30 — Run 50 min, easy
Tue, July 1 — Swim 40 min, drills
Wed, July 2 — Ride 60 min, tempo
Thu, July 3 — Rest
Fri, July 4 — Long ride 75 min
Sat, July 5 — Run 50 min, easy


Week 2 (Sun July 6 – Sat July 12) — race week: peak and sharpen, 330 min


Sun, July 6 — Ride 60 min, tempo
Mon, July 7 — LONG BRICK 90 min (ride 60 + run 30) — biggest session
of the block, bank the fitness now
Tue, July 8 — Run intervals 45 min, hard
Wed, July 9 — Swim 45 min
Thu, July 10 — Ride 60 min with race-pace surges
Fri, July 11 — Run 30 min, strides
Sat, July 12 — RACE DAY (sprint, ~75 min)


This plan focuses on sharpening, not overtraining.


What the trap is built to violate

Both of the gate's deterministic conditions, for a declared goal race:
(a) race-week daily average not below the preceding average, and
(b) a race-week training day exceeding the largest preceding day.
The checker's committed run output states the numbers; nothing in this
file does the math. A must in markdown is a request; a must in code is
a constraint — the trap's own prose obeys that rule too.

(The closing sentence of the trap text — a plan asserting its own
safety — is the source plan's failure pattern reproduced verbatim in
shape. Against a full editor run it would also draw Rule 6; the checker
deliberately scores only what is deterministic.)