# What this editor can't do

Every tool oversells itself somewhere. Here's where this one's checks reach their limit — found, checked, and receipted rather than smoothed over.

## The load proxy has a blind spot, and it can flip a verdict, not just soften one.

`checker.py`'s own docstring already names the design tradeoff: load is measured in scheduled minutes, because minutes are the only unit every plan states and the only one computable without inventing an athlete's pace. The documented assumption was that this is a *safe* simplification — an uncomputable preceding-week row gets treated as zero, which only makes Rule 1's gate harder to pass, so a pass despite missing data was assumed trustworthy.

That assumption holds for false passes. It does not hold for false blocks — and we found the case that breaks it.

**The case.** A real AI-generated triathlon plan (Specimen 6, `examples.md`) states almost every session in yards and miles rather than minutes: swim sets in yards, long rides and runs in miles, only race week itself stated in minutes. Run against the plan exactly as written, the checker returned **BLOCK** — race week's daily average (13.6 min) came back higher than the preceding eleven weeks' average (9.1 min).

That's the correct output for the input it was given. It's also wrong, in the sense that matters: those eleven weeks are full of real 60-to-90-minute sessions — a 90-minute ride, an 11-mile race-simulation brick, the race-specific weeks' 1,600-yard swims — that the checker had no way to convert to minutes, so it counted them as zero. Race week looked heavy only because it was the one stretch of the plan stated in a unit the checker could read.

**The proof, not just the theory.** We reran the identical plan with one change: every distance-based session was converted to minutes using the athlete's own actual race-day paces (her stated splits from this year, applied flat across easy and hard sessions alike — if anything an underestimate, since real easy-day pace is normally slower than race pace). Nothing else changed. The preceding average moved from 9.1 to **24.5 minutes a day**. The gate passed. Verdict moved from BLOCK to FINDINGS.

That's not a hunch about what might be happening under the hood — it's the same ledger, same plan, same rules, one directly measurable input added, and the verdict flips. The mechanism is real.

**Receipts:**
- `runs/2026-07-20-pam-triathlon-run.txt` — the original run, VERDICT: BLOCK, exit code 2.
- `pam-triathlon.ledger` — the input, reproducing that receipt exactly on demand.
- `evidence-pam-triathlon-verbatim.md` — the full source plan, so every ledger row can be checked against the plan's own words.
- `witness-pdfs/pamtriathlonfollowup.pdf` — the paced follow-up report as actually sent to the witness.
- `runs/2026-07-20-pam-triathlon-paced-run.txt` / `pam-triathlon-paced.ledger` — the paced rerun's machine receipt and input, reproducing each other on demand.

The athlete's verbatim reaction to both reports is in `examples.md`, Specimen 6.

## One place arithmetic does happen at extraction time — on the record

`checker.py`'s docstring says arithmetic never happens at extraction time. One committed ledger bends that: `nyc-marathon.ledger`'s run durations are the plan's stated miles multiplied by the athlete's stated 12-minute mile, converted when the ledger was built, under direction-safety rules recorded in the ledger's own header (lower mile count for the preceding period, upper for race week — each choice can only make the gate harder to pass). Every converted row carries its source miles in its description, so any single multiplication can be checked by hand against the row itself. A proper fix is the same pace-directive feature described below; until then, the conversion is disclosed here rather than hidden in a comment.

## Why this isn't patched in `checker.py`

A proper fix needs athlete-stated pace directives — never an assumed default pace, since inventing one would be exactly the phantom-athlete failure Rule 4 exists to catch in the plans this editor reviews. That's real feature work: new directives, distance parsing, and new selftest coverage proving it changes nothing for every ledger that doesn't use it. Two days before a submission deadline, with five other specimens' credibility riding on `checker.py`'s current, tested behavior, that trade wasn't worth making. Documented and receipted beats quietly patched under deadline pressure — a claim a stranger can rerun is worth more than a fix nobody had time to verify.

## Effort labels the checker cannot see — found by an independent reviewer

On 2026-07-20, an independent professional (Natalie — trainer, named with consent; her review is committed verbatim in `examples.md`, Specimen 4 addendum) reviewed Specimen 4's plan and report without seeing `rules.md` first. Two of her points converged with what the tool already found. One did not: a plan's intensity vocabulary — "easy," "hard," "medium" — can go entirely unanchored to any pace or measurable target, and no rule here evaluates that. Rule 3 catches specific rows whose amounts can't be computed; it cannot catch a plan that computes perfectly and still never defines what "easy" means for the athlete holding it.

This is logged as a limitation rather than patched, for the same reason as the load-proxy case above: a ninth rule the day before submission would be untested against six specimens whose credibility rides on the current, tested eight, and the design gate — eight rules is the ceiling; new edge cases become test artifacts or documented boundaries — exists precisely for this moment.

## The honest summary

This editor will occasionally block a plan that is actually fine, specifically when that plan states most of its volume in distance rather than time. When that happens, the fix is the same one this editor already asks for in Findings 1 and 2 of Specimen 3, and Findings 1 and 2 of Specimen 6: give it a pace. Until then, a BLOCK from this tool means "the math didn't clear," not "the plan is unsafe" — and the report says so, every time, rather than letting a technical verdict masquerade as a training judgment.
