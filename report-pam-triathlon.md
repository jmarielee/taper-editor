<!--
repo metadata (not part of the athlete-facing report below):
Source: AI-generated triathlon training plan, provided by an external witness
(Pam), reviewed with her consent. Prompt named the race and its recurrence
rule ("Anchor Bay Triathlon ... always the second weekend in July"); the
AI-generated plan text itself names no race, contains no identifying detail.
Race date anchored to 2027-07-10 (Saturday) — an assumption, not a
confirmed date. The athlete's prompt states only "next year," with no date
and no scheduling rule. The event ran Sat 2025-07-12 and is scheduled Sat
2026-07-11 (event's official site, checked 2026-07-21); no 2027 date is
published. 2027-07-10 follows the second-Saturday pattern observed in
those two years. (Corrected 2026-07-21: an earlier version of this note
called the date publicly scheduled and attributed the pattern to the
athlete's prompt; neither was supported. The anchor date itself is
unchanged.)
Ledger: pam-triathlon.ledger (built from the plan's stated structure; most
rows uncomputable by design — see Finding on the BLOCK below).
Receipt: runs/2026-07-20-pam-triathlon-run.txt — VERDICT: BLOCK, exit code 2.
Quote note: the source plan formats each session across multiple short lines
("Tuesday" / "Swim" / "20 minutes easy"). Quotes in this report flatten that
line-broken formatting into single lines; every word appears contiguously in
evidence-pam-triathlon-verbatim.md, verified with whitespace-normalized
matching 2026-07-20. No words were added or joined across sessions.
-->

# The Taper Editor — report on your triathlon plan

I read your whole plan. Here's what I found, most important first.

**This plan fails the one check I refuse to compromise on — though not for the reason you'd guess.** Here's why.

---

### Race week comes back heavier than the eleven weeks before it — by the only measure the plan gives me.

**Your plan says:** race week — "Tuesday Swim 20 minutes easy... Wednesday Bike 30 minutes with a few pickups... Thursday Run 20 minutes easy... Saturday 15-minute bike / 10-minute run." Compare that to how nearly everything before it is written: "Swim 1,500 yards," "Bike 90 minutes" is the exception — most read "Run 5 miles," "Bike 11 miles," "Swim 1,600 yards." Distance, not time.

**The problem:** *Race-week load* — computed strictly from what the plan actually states in minutes, your race week averages about 14 minutes of training a day; the eleven weeks before it average about 9. By that count the plan ramps up instead of winding down, which is the one thing this editor won't pass silently. But look at what's driving it: your single biggest day anywhere in the plan — Week 11's 90-minute bike — still beats every day of race week by a wide margin, so it isn't that race week is secretly brutal. It's that race week is the only stretch where almost every session happens to be stated in minutes. Every "5 miles," "1,500 yards," and "11 miles" in the eleven weeks before it computes as zero training minutes on this count — not because you weren't training, but because the plan never converts them, and I don't invent a pace you never gave me.

**What it costs you:** right now, neither the machine count nor I can tell whether your race week genuinely ramps up or whether eleven weeks of real training are simply invisible to a count that only understands minutes. That's not a small gap — it's most of the plan.

**Your call:** What rough pace can you give for each discipline so the distance-based sessions can be recomputed?

---

### Your plan's calendar and the real race are one day apart.

**Your plan says:** "Saturday — 15-minute bike, 10-minute run" ... "Sunday — Race Day."

**The problem:** *Calendar and arithmetic integrity* — the plan never states an actual date, only week numbers and weekday names, so I anchored it using the pattern in the two years I could check — the race fell on Sat July 12 in 2025 and is scheduled for Sat July 11 in 2026, always the second Saturday of the month. No 2027 date has been published yet, so July 10, 2027 is my best estimate from that pattern, not a confirmed date. Under that estimate, your race week falls across July 5–11, 2027, with race day landing on a Saturday. Under the plan's own day-by-day template, the day it calls a light shakeout is the estimated race day, and the day it calls "Race Day" is the Sunday after.

**What it costs you:** if you followed the plan's labels as written, you'd expect one more easy day between your shakeout and the start line. There isn't one.

**Your call:** which governs — the plan's generic Saturday/Sunday template, or the real date, once you confirm it?

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

### Witness reaction (2026-07-20, verbatim, consent given)

> This was actually very helpful!  Now that it's been pointed out to me (thanks, AI!) I can't unsee that the original plan was written with both distances and times.  That IS a huge red flag, especially if your true intention is to taper before race day. The lack of consistency in the original training plan seems glaring now.
>
> I do like that it points out the need to provide a few pacing data points. And that I should have provided a race date. I'm exactly the kind of person who would start a 12 week training plan that ends on a Sunday even though my race would fall the day before that. (Who's looking 12 weeks ahead like that?)
>
> Overall, I think your math rules worked exactly as intended. That plan SHOULD have failed; it looks good at a cursory glance but a deeper dive shows the inconsistencies could absolutely lead to overtraining.
>
> Regards,
> Pam

Recorded as-is, unedited — and note what it does to the tool's own framing.
`LIMITATIONS.md` presents this block as a false positive: the math was
right for its input, wrong about the training. The athlete read the same
evidence and disagreed — she says the block was *correct*, because a plan
that mixes distances and times so inconsistently is itself the hazard, not
just a unit this tool can't count. Tool says data gap; user says real flag.
That disagreement is kept unresolved, on the record, which is the point.
