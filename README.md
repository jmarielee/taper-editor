# The Taper Editor

An editor for AI-generated endurance training plans — running and triathlon — with particular authority over the final phase: whether the calendar, the workload, and the race-week claims support an actual taper. It doesn't rewrite your plan and it doesn't coach your body. It reads what an AI wrote for you, checks it against eight structural rules — with the race-week rule, and all calendar and total arithmetic, enforced by a deterministic checker rather than model judgment, and hands it back with findings: what the plan says, what rule it breaks, what that costs you, and a question for you to answer. You decide what to do with it.

Built for Clief Notes Comp #9. Domain: checking AI-generated endurance training plans, for the runner or triathlete about to follow one.

## The sixty-second version

Paste an AI-generated endurance plan into this editor. You get back at most five findings, ranked by consequence, each in the same four-part shape: **Your plan says** (the exact line, quoted) → **The problem** (the rule it breaks, in plain English) → **What it costs you** → **Your call** (a question — never a rewritten line).

Here is a real one, excerpted from a committed report (`report-trap-plan-block.md`; machine receipt `runs/2026-07-19-trap-plan-run.txt`):

> **Your plan says:** "Mon, July 7 — LONG BRICK 90 min (ride 60 + run 30) — biggest session of the block, bank the fitness now."
>
> **The problem:** *Race-week load* — when a race is your goal race, the final seven days have to wind down compared to the training that came before. [...] your plan fails it two ways, by machine count, not by my impression: Your final week averages **47 minutes of training a day**. The rest of your plan averaged **46**. Race week isn't lighter — it's heavier. [...] The single biggest training day of your entire plan — **90 minutes** — sits *inside* race week.
>
> **What it costs you:** the race. [...] You'd start the race your whole plan exists for carrying the fatigue of its hardest week.
>
> **Your call:** I don't rewrite plans and I won't tell you which session to change — that's yours.

That plan is the repo's planted trap — committed in full (`trap-plan.md`) so anyone can re-spring it themselves: `python3 checker.py trap-plan.ledger`. The editor never produces a corrected plan, never invents a pace or baseline the athlete didn't state, and when it can't evaluate a rule without more information, it holds and asks one question rather than guessing.

**Validation status:** a tested prototype with committed, reproducible receipts — not a clinically or scientifically validated training assessment tool.

## Why this exists

In July 2025, I asked ChatGPT for a taper plan for a local sprint triathlon. I followed it. I felt fine at the start line until I found out how fried I was in the middle of the race, when there was nothing left to find. I finished in 1:44.

The year before, my bike shoe broke at the start of the bike leg. Any cyclist can tell you what that costs: the pull-up half of every pedal stroke, gone for the entire ride. That race, with broken equipment and half a pedal stroke, was still four minutes faster than the race where I followed the plan.

The plan had also labeled race day "Fri, July 12." July 12, 2025 was a Saturday. I didn't catch it, and the plan didn't catch itself. That mistake didn't cost me the race, but it told me what I was dealing with: a plan that can't count days shouldn't be trusted to count load unchecked.

The worst part: I knew better. I've raced enough to know what a taper is supposed to look like, and that final week didn't look like one. But the plan sounded so informed, so sure of itself, that I followed it over my own judgment. That's the failure this editor exists for. A newer athlete doesn't know which claims to question; an experienced one can still be talked out of what she knows. Either way, the plan's confidence goes unchecked, so this tool checks it.

Every rule in this repo traces back to something a real AI-generated plan actually did wrong. Most of them from that same plan. Some from plans that came after it, while this tool was being built. `examples.md`, Specimen 1, is the report I wish I'd had before July 12.

## Quickstart

**As a Claude project:** drop this whole folder into a Claude project. Paste in an AI-generated endurance plan. You'll get a report back in the format below.

**As a deterministic checker**, no model required:
```
python3 checker.py --selftest          # confirms the rule engine itself: 8/8, including one test that must NOT fire and one that pins a known limitation
python3 checker.py trap-plan.ledger    # reproduces any specimen's verdict from its ledger
```
Every ledger in this repo reproduces its committed **machine receipt** — the checker's deterministic output — exactly, on demand. (The editor's full verdicts in the table below layer model-reviewed editorial flags on top of that machine state; the flags live in the reports, the arithmetic lives in the receipts.) Where a specimen went through intermediate HOLDs before a declaration landed (Specimens 3 and 4), the intermediate receipts are preserved in `runs/`, but the ledgers were updated in place as athlete declarations were recorded — so the committed ledger reproduces the final state, and the earlier receipts document the path. That scoping is stated here so nobody has to discover it.

## What a report looks like

Every finding has four parts, in this order, always:

1. **Your plan says** — the exact line the finding is about, quoted.
2. **The problem** — which of the 8 rules it breaks, in plain English.
3. **What it costs you** — stated plainly, no hedging.
4. **Your call** — a question. Never a rewritten line.

Findings are ranked by consequence, capped at five. If a rule can't be evaluated without more information, the editor holds and asks one question rather than guessing. It never invents a pace, a baseline, or an injury history the athlete didn't state.

## What it checks

One check blocks; the rest are flags the athlete may accept. Full detail, failure patterns, and real examples are in `rules.md`. A one-line-per-rule index is in `reference/rules-quick-reference.md`, and every training term used anywhere in this repo is defined in `reference/glossary.md`.

Before any rule applies, a scope precondition asks two questions: is this AI-generated, and is it an endurance plan? If either is false, the editor declines and says so — it doesn't invent findings to have something to say. Specimen 5 in `examples.md` is that decline, live.

## The five specimens, plus one

`examples.md` holds six real, dated runs — every verdict the editor can return, each backed by a receipt in `runs/`:

| # | What | Verdict |
|---|---|---|
| 1 | The original 2025 plan that started this project | HOLD |
| 2 | A constructed trap, built to violate the one hard rule | BLOCK |
| 3 | A real Detroit half marathon plan | PASS, 5 flags |
| 4 | A real NYC Marathon plan, external witness | PASS, 3 flags |
| 5 | A real strength program — the scope decline | DECLINE |
| 6 | A real triathlon plan, second external witness | BLOCK, disputed — see below |

Four of these six specimens are constructed or real-but-private test cases; two — Specimens 4 and 6 — came from people who are not the builder, reviewing plans they actually intended to follow, with consent and preview before anything was committed. The Specimen 4 witness is anonymous by her own request, and stays that way everywhere in this repo.

## Verification

- `python3 checker.py --selftest` — 8/8, deterministic, including a clean control case that must not fire and a regression test that pins the Specimen 6 mixed-unit false block as documented, known behavior (receipts: `runs/2026-07-19-selftest-run.txt` and `runs/2026-07-20-selftest-run.txt` at 8/8 before the pin was added 2026-07-21, `runs/2026-07-21-selftest-run.txt` at 8/8 after).
- Every specimen's committed ledger reproduces its receipt in `runs/` exactly, on demand (final-state scoping noted in Quickstart).
- Specimen 4's plan and report were additionally reviewed blind by an independent professional — a trainer, named with consent, who had not seen `rules.md`. Her feedback independently converged with Finding 1 and Rule 8, and exposed one gap the eight rules don't cover, logged in `LIMITATIONS.md` rather than patched. Her verbatim texts are in `examples.md`, Specimen 4 addendum.
- Four of six specimens ship their full source plan text (`evidence-adjusted-plan-verbatim.md` for Specimen 1, `trap-plan.md` for Specimen 2, `evidence-detroit-half-verbatim.md` for Specimen 3, `evidence-pam-triathlon-verbatim.md` for Specimen 6 — her own prompt included, committed with consent), so every quote in those reports can be checked by hand against a committed file. Specimens 4 and 5 do **not** ship their source text — Specimen 4 by deliberate decision (the plan belongs to an anonymous witness), Specimen 5 for the same witness-privacy reason. Known gaps, stated up front, not discovered later. Quotes in those two reports are verifiable by the athletes who own the plans, not by a stranger from this repo alone.
- `evidence-detroit-half-verbatim.md` carries one deliberate redaction: the word "knee" is replaced with the visible marker `[joint]`. Race name and injury history are kept as originally written — a documented choice, not an omission. `evidence-recovered-summaries.md` documents a separate honesty check: an early AI-written summary of the 2025 plan quietly corrected a weekday error the verbatim source actually contained. Caught, logged, kept.

## Where this tool disagrees with itself, on the record

One external test (Specimen 6) exposed a mixed-unit limitation: run as written, the checker returned a BLOCK that was deterministic, reproducible — and arguably wrong. The athlete who owns that plan read the same evidence and disputes even that framing: she reads the plan's unit inconsistency as a genuine red flag in its own right. Both runs are committed, the disagreement is kept unresolved, and the full mechanism — including why it isn't being patched under deadline pressure — is in `LIMITATIONS.md`. The full exchange is Specimen 6 in `examples.md`.

## File map

```
identity.md                          who the editor is, what it reviews
rules.md                             the 8 rules, severity, what it must never do
examples.md                          all six specimens with their reports and witness reactions (Specimen 1 abridged; its standalone report is canonical)
reference/
  glossary.md                        every term used but not defined inline
  rules-quick-reference.md           one line per rule
LIMITATIONS.md                       the load-proxy edge case, receipts, the disagreement
checker.py                           the deterministic rule engine
parse_workouts.py                    turns an Apple Health export into a workout table
july-2025-workouts.txt               that table, machine-generated, for the 2025 race window
*.ledger                             one per specimen, checker.py's actual input
evidence-*-verbatim.md, trap-plan.md source plan text, quoted from directly
evidence-recovered-summaries.md      recovered AI summaries, labeled as such; the silent weekday repair, caught and kept
report-2025-adjusted-plan.md         Specimen 1's report as a standalone file (canonical)
report-trap-plan-block.md            Specimen 2's report (canonical)
report-detroit-half-pass.md          Specimen 3's report (canonical)
report-nyc-marathon.md               Specimen 4's report (canonical)
report-pam-triathlon.md              Specimen 6's report (canonical)
runs/                                every checker run, timestamped, reproducible
witness-pdfs/                        what was actually sent to the witnesses
LICENSE
```

## What this editor will never do

Rewrite, redraft, or produce a corrected plan. Prescribe volume, intensity, weight, or pace. Comment on your body. Assess whether an injury accommodation is medically adequate — that's a clinician's call, and the editor says so when it declines. Perform arithmetic by guesswork when the checker can run instead. Praise. A pass gets a short pass and the reminder that a pass is not a prescription.
