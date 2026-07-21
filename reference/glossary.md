# glossary.md — every training term used in this repo, in plain language

Reports define terms like *taper* and *brick* the first time they appear, per
identity.md. This file collects every term of art used anywhere in the repo so
nothing depends on the reader already being a training nerd.

**A-race / goal race** — the race the whole plan exists for. Rule 1's block
applies only to a declared goal race.

**Training race / B-race** — a race entered as practice or a fitness test for
a larger goal. May legitimately be trained through; the editor never decides
which kind a race is — the athlete declares it.

**Taper** — reducing training in the final stretch before a race so you arrive
at the start line rested instead of tired. The one thing this editor blocks on,
for a declared goal race.

**Race week** — as this repo computes it: the 7 calendar days ending on race
day, inclusive. Race day's own effort is excluded from race-week *training*
load (the gate governs the load around the race, not the race).

**Load** — how much training a body absorbs. This repo's proxy for load is
scheduled minutes, because minutes are the only unit every plan states. The
proxy's blind spot is documented in LIMITATIONS.md.

**Ramp** — the comparison between race-week load and the load of the weeks
before it. A plan whose race week out-trains its earlier weeks ramps up when
it should wind down.

**Brick** — a bike ride followed immediately by a run, the most demanding
common session in triathlon training.

**Sprint triathlon** — the shortest common triathlon distance (roughly a
half-mile swim, an 11–13 mile bike, a 3 mile run; exact distances vary by
event).

**Easy pace / conversational pace** — an effort at which you could speak in
full sentences. "Easy" is an effort description, not a number, which is why
the checker can't compute it without a stated pace.

**Long run** — the week's single longest run, usually on a weekend; the
backbone session of most running plans.

**Intervals** — repeated short, hard efforts separated by recovery (e.g.
6x400m). Intensity work.

**Tempo** — a sustained, comfortably-hard effort; harder than easy, easier
than racing.

**Strides / openers / pickups** — very short accelerations used to stay sharp
on otherwise light days, especially in race week.

**Shakeout** — a very short, very easy session in the last day or two before
a race, meant to loosen the body, not train it.

**Run/walk** — deliberately alternating running and walking intervals (e.g.
2 minutes running, 1 walking) from the start, rather than walking only when
forced to.

**Recovery week / cutback week** — a planned lighter week inside a training
build, so the body absorbs the work.

**Race pace / marathon effort** — the effort you intend to hold on race day;
sessions "at race pace" rehearse it.

**Open water swim** — swimming in a lake or sea rather than a pool; race
conditions for most triathlons.

**Ledger** — this repo's machine-readable extraction of a plan: one row per
dated session, quoted from the plan, arithmetic left to `checker.py`. The
format spec lives only in `checker.py`'s docstring.

**Receipt** — the committed, dated output of an actual checker run, in
`runs/`. Receipts are never edited after commit.

**Verdicts** — the checker returns CLEAN (nothing fired), FINDINGS
(flag-level issues), HOLD (one question must be answered first), or BLOCK
(the plan fails Rule 1 for a declared goal race). The editor's plain-English
reports carry the same outcomes without the vocabulary: a pass, a question,
or a fail. DECLINE is the editor's own outcome for out-of-scope plans — the
checker never runs on those.
