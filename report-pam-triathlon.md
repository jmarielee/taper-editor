<!--
repo metadata (not part of the athlete-facing report below):
Source: AI-generated triathlon training plan, provided by an external witness
(Pam), reviewed with her consent. Prompt named the race and its recurrence
rule ("Anchor Bay Triathlon ... always the second weekend in July"); the
AI-generated plan text itself names no race, contains no identifying detail.
Race date anchored to 2027-07-10 (Saturday), confirmed against the event's
public schedule (anchorbaytri.com and independent race calendars, checked
2026-07-20).
Ledger: pam-triathlon.ledger (built from the plan's stated structure; most
rows uncomputable by design — see Finding on the BLOCK below).
Receipt: runs/2026-07-20-pam-triathlon-run.txt — VERDICT: BLOCK, exit code 2.
Quote note: the source plan formats each session across multiple short lines
("Tuesday" / "Swim" / "20 minutes easy"). Quotes in this report flatten that
line-broken formatting into single lines; every word appears contiguously in
evidence-pam-triathlon-verbatim.md, verified with whitespace-normalized
matching 2026-07-20. No words were added or joined across sessions.
>>> CORRECTED 2026-07-21: the calendar finding previously called July 10, 2027
>>> "publicly scheduled" and attributed the second-weekend pattern to the
>>> athlete's prompt. Both claims were unsupported: the prompt says only "next
>>> year," and no 2027 date is published (2025 ran Sat Jul 12; 2026 is Sat
>>> Jul 11, per the event's official site, checked 2026-07-21). The date anchor
>>> itself is unchanged and is now labeled the assumption it always was. The
>>> as-sent witness PDF preserves the original wording; it is not edited.
-->

# The Taper Editor — report on your triathlon plan

I read your whole plan. Here's what I found, most important first.

**This plan fails the one check I refuse to compromise on — though not for the reason you'd guess.** Here's why.

---

### Race week comes back heavier than the eleven weeks before it — by the only measure the plan gives me.

**Your plan says:** race week — "Tuesday Swim 20 minutes easy... Wednesday Bike 30 minutes with a few pickups... Thursday Run 20 minutes easy... Saturday 15-minute bike / 10-minute run." Compare that to how nearly everything before it is written: "Swim 1,500 yards," "Bike 90 minutes" is the exception — most read "Run 5 miles," "Bike 11 miles," "Swim 1,600 yards." Distance, not time.

**The problem:** *Race-week load* — computed strictly from what the plan actually states in minutes, your race week averages about 14 minutes of training a day; the eleven weeks before it average about 9. By that count the plan ramps up instead of winding down, which is the one thing this editor won't pass silently. But look at what's driving it: your single biggest day anywhere in the plan — Week 11's 90-minute bike — still beats every day of race week by a wide margin, so it isn't that race week is secretly brutal. It's that race week is the only stretch where almost every session happens to be stated in minutes. Every "5 miles," "1,500 yards," and "11 miles" in the eleven weeks before it computes as zero training minutes on this count — not because you weren't training, but because the plan never converts them, and I don't invent a pace you never gave me.

**What it costs you:** right now, neither the machine count nor I can tell whether your race week genuinely ramps up or whether eleven weeks of real training are simply invisible to a count that only understands minutes. That's not a small gap — it's most of the plan.

**Your call:** attach a rough pace to the distance-based sessions — even one number per discipline — and this can be recomputed. If your real training load is anywhere near what those distances imply, this block almost certainly clears.

---

### Your plan's calendar and the real race are one day apart.

**Your plan says:** "Saturday — 15-minute bike, 10-minute run" ... "Sunday — Race Day."

**The problem:** *Calendar and arithmetic integrity* — the plan never states an actual date, only week numbers and weekday names, so evaluating it required an anchor, and that anchor is an assumption on the record, not a fact: your prompt says only "next year." The event ran Saturday, July 12, 2025 and is officially scheduled for Saturday, July 11, 2026 (the race's own site); no 2027 date is published yet. On that second-Saturday pattern, race day would be Saturday, July 10, 2027 — placing your race week across July 5–11, 2027. Under the plan's own day-by-day template, the day it calls a light shakeout is the assumed race day, and the day it calls "Race Day" is the Sunday after the race already happened.

**What it costs you:** if you followed the plan's labels as written, you'd expect one more easy day between your shakeout and the start line. There isn't one.

**Your call:** what is the confirmed 2027 race date — and once you have it, which governs: the plan's generic Saturday/Sunday template, or that date?

---

### The plan states three different finish-time goals, and none of them agree.

**Your plan says:** "Your goal should be to finish around 1:38–1:42, which is very realistic with consistent training over the next year" — and later, its own table: "Overall | 1:51:16 | 1:35–1:40."

**The problem:** *Calendar and arithmetic integrity*, again — every number has to reconcile with the others. The opening paragraph names one range; the closing table names a different one; and that same table's own five per-discipline goals — 17:30–18:30, 2:00, 40:00–42:00, 1:15, 32:00–34:00 — sum to 1:32:45–1:37:45, which matches neither of the other two. (Worth noting, since it cuts the other way: this year's five actual splits sum exactly to your stated finish time, 1:51:16 — that part of the plan's arithmetic is clean.)

**What it costs you:** three numbers, one goal, and none of them were checked against each other before this reached you.

**Your call:** which of these is the real target — and does the rest of the plan's math agree with it once you pick?

---

### The plan grades its own goal before the numbers underneath it agree.

**Your plan says:** "Your goal should be to finish around 1:38–1:42, which is very realistic with consistent training over the next year."

**The problem:** *Self-certification* — a plan's claims about its own adequacy are claims, not facts. Calling a number "very realistic" in the same paragraph that number contradicts the plan's own later table, per the finding above, is grading homework nobody checked.

**What it costs you:** confident language here is doing the job of reassurance, not verification.

**Your call:** what should "realistic" actually rest on, once the goal numbers above are reconciled into one?

---

### Where this leaves you

The block above stands until the distance-based sessions have paces attached — that's a data gap, not necessarily a training problem, and it's fixable with a handful of numbers. The three findings below it are independent of the block and stand regardless of how it resolves. This report points at the plan; it doesn't rewrite it. Your call, on all of it.
