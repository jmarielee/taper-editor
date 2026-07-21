# The Taper Editor

An editor for AI-generated endurance training plans — running and triathlon. It doesn't rewrite your plan and it doesn't coach your body. It reads what an AI wrote for you, checks it against eight structural rules and one deterministic race-week check, and hands it back with findings: what the plan says, what rule it breaks, what that costs you, and a question for you to answer. You decide what to do with it.

Built for Clief Notes Comp #9. Domain: AI-generated endurance training plans, for the runner or triathlete about to follow one.

## Why this exists

A taper is one of endurance training’s most basic principles: reduce the load so the athlete reaches race day recovered.

I knew that. But when ChatGPT gave me a heavier race-week plan, I followed it anyway. The plan sounded confident, and I let that confidence override my better judgment.

I felt fine at the starting line. Midway through the race, I discovered how fatigued I actually was. I finished in 1:44, four minutes slower than the previous year, when my bike shoe broke at the start of the ride and I completed most of the cycling leg without a full pedal stroke.

The plan had also labeled race day “Fri, July 12.” July 12, 2025 was a Saturday. That mistake did not cost me the race, but it showed that the plan had not checked even its own calendar.

Newer, self-coached athletes may not know what to question. Experienced athletes may see the problem and still defer to a system that sounds more informed or authoritative. Either way, confidence can carry an athlete past the moment they should stop and reconsider.

The Taper Editor exists to create that stopping point.

It does not replace a coach, prescribe training, or declare a plan safe. It checks whether an AI-generated endurance plan follows its own calendar, respects the basic purpose of a taper, and provides enough evidence to justify the workload it assigns.

Every rule in this repository traces back to something a real AI-generated plan actually did wrong. examples.md, Specimen 1, is the report I wish I had read before deciding the AI probably knew better.

## Quickstart

**As a Claude project:** drop this whole folder into a Claude project. Paste in an AI-generated endurance plan. You'll get a report back in the format below.

**As a deterministic checker**, no model required:
```
python3 checker.py --selftest          # confirms the rule engine itself: 7/7, including one test that must NOT fire
python3 checker.py trap-plan.ledger    # reproduces any specimen's verdict from its ledger
```
Every ledger in this repo reproduces its **final** verdict exactly, on demand. Where a specimen went through intermediate HOLDs before a declaration landed (Specimens 3 and 4), the intermediate receipts are preserved in `runs/`, but the ledgers were updated in place as athlete declarations were recorded — so the committed ledger reproduces the final state, and the earlier receipts document the path. That scoping is stated here so nobody has to discover it.

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

`examples.md` holds six real, dated runs — every verdict the checker can return, each backed by a receipt in `runs/`:

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

- `python3 checker.py --selftest` — 7/7, deterministic, including a clean control case that must not fire.
- Every specimen's committed ledger reproduces its receipt in `runs/` exactly, on demand (final-state scoping noted in Quickstart).
- Four of six specimens ship their full source plan text (`evidence-adjusted-plan-verbatim.md` for Specimen 1, `trap-plan.md` for Specimen 2, `evidence-detroit-half-verbatim.md` for Specimen 3, `evidence-pam-triathlon-verbatim.md` for Specimen 6 — her own prompt included, committed with consent), so every quote in those reports can be checked by hand against a committed file. Specimens 4 and 5 do **not** ship their source text — Specimen 4 by deliberate decision (the plan belongs to an anonymous witness), Specimen 5 for the same witness-privacy reason. Known gaps, stated up front, not discovered later. Quotes in those two reports are verifiable by the athletes who own the plans, not by a stranger from this repo alone.
- `evidence-detroit-half-verbatim.md` carries one deliberate redaction: the word "knee" is replaced with the visible marker `[joint]`. Race name and injury history are kept as originally written — a documented choice, not an omission. `evidence-recovered-summaries.md` documents a separate honesty check: an early AI-written summary of the 2025 plan quietly corrected a weekday error the verbatim source actually contained. Caught, logged, kept.

## Where this tool disagrees with itself, on the record

Specimen 6's plan states most of its training in yards and miles, not minutes. Run as written, the checker returned BLOCK — race week's load looked heavier than the eleven weeks before it, because those eleven weeks are full of real 60-to-90-minute sessions the checker has no pace to convert, so it counted them as zero. Rerun with the athlete's own real paces attached to those same sessions, the block clears. Both runs are committed.

The athlete who owns that plan read the same evidence and disagreed with the framing above. Her full reaction is in Specimen 6; the short version is that she reads the plan's inconsistency between distances and times as a genuine red flag in its own right, not just a limitation in how this tool measures load. That disagreement is written up, unresolved, in `LIMITATIONS.md` — including why it isn't being patched into `checker.py` two days before a deadline. A tool that only shows you its wins isn't more trustworthy than one that shows you where a real user pushed back on it.

## File map

```
identity.md                          who the editor is, what it reviews
rules.md                             the 8 rules, severity, what it must never do
examples.md                          all six specimens, full reports, witness reactions
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
