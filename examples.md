# examples.md — what the editor's voice sounds like in practice

This file is canonical for tone and demonstrates rules.md and identity.md in
practice. Every specimen below is a real, dated run — the editor's plain-English
output, exactly as returned, backed by a committed machine receipt in `runs/`.
Nothing here is authored or hypothetical. Where a specimen's report exists as
its own file elsewhere in the repo, that file remains canonical for its
content; this file exists so the six specimens can be read together, in
order, as one demonstration of the voice across every verdict the editor can
return: HOLD, BLOCK (twice — once planted, once live and disputed),
PASS-with-flags (twice), and DECLINE.

---

## Specimen 1 — The origin case: HOLD

**Source:** the real 2025 triathlon plan that started this project — a
ChatGPT-generated race-week plan, recovered and secured verbatim
(`evidence-adjusted-plan-verbatim.md`).
**Receipt:** `runs/2026-07-19-adjusted-plan-run.txt` — verdict HOLD, exit
code 3.
**Why it's here:** every rule in this repo traces back to something this
plan actually did wrong. This is the report a stranger would have needed
in July 2025.

# The Taper Editor — report on your July 2025 triathlon plan

I read your whole plan. Before I can finish, one question:

**ON HOLD — one question before the race-week check resolves.**
Your plan builds toward a race on July 12, but it never says what that race is *for*. **Is this race the goal, or training for something else?** Those are different plans — how hard you should be working in the final week depends entirely on the answer, so I can't rule on that part until you tell me.

One honest note on that check: even after you answer, I can't fully verify your final week, because of Finding 2 below.

Everything else I found stands on its own. Here it is, most important first.

---

### 1. Every single date in your plan is on the wrong day — including race day.

**Your plan says:** "Fri, July 12 — TRIATHLON DAY! — Race strong and enjoy what you've trained for."

**The problem:** *Calendar and arithmetic integrity* — every date's weekday has to match a real calendar, and every number has to add up. July 12, 2025 was a **Saturday**, not a Friday. And it isn't just race day: all twelve days in your plan's table are labeled one weekday off. July 1 is labeled "Mon" — it was a Tuesday. The whole table is shifted, and the plan even contradicts itself: its own opening line correctly says "Sprint triathlon on Saturday, July 12," then the table calls that day Friday.

**What it costs you:** You execute the calendar, not the intention. A plan whose days are all mislabeled can put your hardest workout, your rest day, or your gear prep on the wrong real day — and it puts "race day" on a day the race isn't happening. If you trusted the labels over the dates, you'd taper for Friday and race tired on Saturday.

**Your call:** Which do you follow — the dates or the day names? And what does it tell you about the rest of this plan that nothing in it caught this?

---

### 2. Ten of your twelve training days have no session length. Your final week can't be checked.

**Your plan says:** "Wed, July 3 — Recovery + Core — Light walk or yoga + 15–20 min core" — and that's one of the *more* specific days. Most read like "Tues, July 9 — Pickleball — Just pickleball today — keep pace moderate."

**The problem:** *Calendar and arithmetic integrity*, again — if a plan's training amounts can't be added up, that itself is a finding. An athlete executes numbers. Only two of twelve days state how long anything should take, so there is no way — for you or for me — to compute whether your final week actually winds down.

---

## Specimen 2 — The planted trap: BLOCK

**Source:** `trap-plan.md` / `trap-plan.ledger` — a constructed plan, labeled
as a trap, built to violate exactly one thing: Rule 1.
**Receipt:** `runs/2026-07-19-trap-plan-run.txt` — verdict BLOCK, exit
code 2.
**Why it's here:** anyone, including a judge, can spring this trap themselves
— `python3 checker.py trap-plan.ledger` — and confirm the one check this
editor refuses to compromise on actually fires.

# The Taper Editor — report on your July 12 race plan

I read your whole plan. Here's what I found, most important first.

**This plan fails.** One problem is serious enough that I won't pass the plan until it's resolved — everything else waits behind it.

---

### 1. Your final week is the hardest stretch of your whole plan. For a goal race, that's backwards.

**Your plan says:** "Mon, July 7 — LONG BRICK 90 min (ride 60 + run 30) — biggest session of the block, bank the fitness now." A **brick** is a bike ride followed immediately by a run — the most demanding kind of session in triathlon training — and your plan schedules its longest one five days before your race and tells you to go get it.

**The problem:** *Race-week load* — when a race is your goal race, the final seven days have to wind down compared to the training that came before. That winding-down is called a **taper**: you reduce training in the last stretch so you arrive at the start line rested instead of tired. This is the one check I refuse to compromise on, and your plan fails it two ways, by machine count, not by my impression:

- Your final week averages **47 minutes of training a day**. The rest of your plan averaged **46**. Race week isn't lighter — it's heavier.
- The single biggest training day of your entire plan — **90 minutes** — sits *inside* race week. Nothing before it ever exceeded 75.

**What it costs you:** the race. Race-week load reduction is one of the few near-universal principles in endurance training — you declared this race the goal, and this plan spends your race-day legs in the five days before you need them. You'd start the race your whole plan exists for carrying the fatigue of its hardest week.

**Your call:** I don't rewrite plans and I won't tell you which session to change — that's yours. But this editor will not pass this plan while its final week out-trains the weeks before it. Resolve the final week, or race knowing the plan failed its one hard check.

---

### Where this leaves you

Until the finding above is resolved, there is no clean bill anywhere in this report — a failed race-week check outranks everything.

---

## Specimen 3 — A fresh real plan, passed: PASS with 5 flags

**Source:** a real 13-week Detroit half marathon plan, generated 2026-07-19,
redacted per repo privacy policy (`evidence-detroit-half-verbatim.md` —
"knee" replaced with the visible marker "[joint]"; race name and injury
history kept as originally written, a deliberate choice).
**Receipt:** `runs/2026-07-19-detroit-half-run.txt` (HOLD, priority
undeclared) → `runs/2026-07-19-detroit-half-run2-goal-declared.txt` (gate
passes both conditions after the athlete declared GOAL in session).
**Why it's here:** this is what the editor's plain-English voice sounds
like when the one hard check passes and everything else is a flag, not a
fail — and it's the specimen for the output contract's quote-or-no-finding
standard (a finding that cannot quote its evidence may not be reported): every quote below was re-checked word-for-word
against `evidence-detroit-half-verbatim.md` on 2026-07-20.

# The Taper Editor — report on your Detroit half marathon plan

I read your whole plan. Here's what I found, most important first.

**Your final week passes the one check I refuse to compromise on.** You told me this race is the goal — recorded, October 18 — and I checked the plan that way. By machine count, your last seven days average 6 minutes of scheduled training a day against 10 a day across the twelve weeks before, and race week's biggest session (25 minutes) is well under your biggest training day (45). The plan winds down. That's a pass on that check — and a pass is not a prescription. Five warnings below are yours to weigh; I state each once.

Also on the record: your calendar is clean. All 39 dates in the plan's table sit on the weekday the plan says they do — 39 rows checked, 39 clean, per the committed receipt. That's a check performed, not a compliment.

---

### 1. Your biggest sessions are the ones with no time attached.

**Your plan says:** the progression table's column is headed "Sunday long run/walk," and every entry under it is a distance — "3 miles," "10 miles," "6 miles — taper" — never a number of minutes, never a pace.

**The problem:** *Calendar and arithmetic integrity* — every amount in a plan has to be computable, and when it isn't, that's itself a finding. Your Sunday long runs are the largest sessions in the plan, and they're stated in a unit I can't convert to training time without inventing a pace you never stated — so I didn't. Which means the load math above, the very math your pass rests on, is blind exactly where your load is biggest.

**What it costs you:** a 10-mile Sunday could be 90 minutes or three hours depending on your pace, and the plan doesn't know which athlete it's talking to. Every conclusion about how heavy your weeks are — including mine — is partial until those sessions have time attached.

**Your call:** you know roughly what a mile takes you. Should the plan?

---

### 2. Three recurring sessions never enter the math at all.

**Your plan says:** "Tuesday — Pickleball … Keep it moderate." · "Strength train for 35–45 minutes" · "Friday — Rest or shortened pickleball … You can play Friday when the [joint] feels normal, but keep it shorter and easier."

**The problem:** *Calendar and arithmetic integrity*, again. To the plan's credit, it acknowledges your pickleball and strength training exist — that's why I'm not flagging it for ignoring your other sports. But acknowledging isn't counting: these sessions recur every week of a 13-week plan with no computable duration. Tuesday has no length at all; "35–45 minutes" is a range, not a number; "Rest or shortened pickleball" is a coin flip. None of them are in the load table.

**What it costs you:** across thirteen weeks, that's dozens of sessions of real training your body will do and the plan's math will never see. The wind-down I verified is a wind-down of *part* of your training.

**Your call:** in your final two weeks, do pickleball and strength wind down too — and says who?

---

### 3. The plan's limits on your other sports are moods, not rules.

**Your plan says:** "Keep it moderate. Avoid playing four hours or repeatedly chasing every difficult ball while your running volume is climbing."

**The problem:** *Missing ceiling* — every stated limit needs a defined response for when it's broken. Worth saying first: this plan does have one limit with real teeth — its symptom rules define exactly what to do when the load was too high (replace the next run, step back a level). But the limits on pickleball have no such backstop. "Keep it moderate" and "avoid playing four hours" never say what happens when a game runs long — no adjustment to the next day, no change to the week.

**What it costs you:** the plan itself warns that two pickleball days plus three runs makes five impact days a week. If a Tuesday session turns into a marathon afternoon, the plan's answer is silence — Wednesday's strength and Thursday's run arrive on schedule as if nothing happened. A limit without a response has silently decided the answer is "nothing."

**Your call:** when Tuesday goes long — and some Tuesday will — what changes on Wednesday, and says who?

---

### 4. The plan promises you a comfortable finish it can't verify.

**Your plan says:** "You have 13 weeks until Sunday, October 18, 2026 — enough time to finish the Detroit half comfortably…" — and later: "you will be positioned to cross the finish line comfortably."

**The problem:** *Self-certification* — a plan's claims about its own adequacy are claims, not facts. The opening sentence reads like an assessment already happened. It didn't — and per Finding 1, the plan's own load math is unverifiable exactly where it's heaviest, so a plan that can't add itself up shouldn't be promising how race day feels.

**What it costs you:** confident self-assessment is the house style of AI-generated plans. If those sentences made you relax, they did their job — reassurance — without doing the work — verification. Thirteen weeks is a forecast, not a guarantee, and the plan states it as a fact.

**Your call:** the plan says thirteen weeks is enough. What is that claim resting on — and does the plan know?
---

## 5. The plan has a rule for the day you do less — and none for the day you do more.

**Your plan says:** "Do not make up a missed long run by jumping ahead. Repeat the previous successful distance and continue from there."

**The problem:** *No bad-day rule* — a plan needs defined behavior for both ways real training diverges from paper: the missed session and the added one. Credit where due: the missed side genuinely has teeth here — that line, plus the symptom rules, tells you exactly what a skipped session changes. But added training is covered only for Friday pickleball. There is no rule anywhere for the week you feel great and want to do more.

**What it costs you:** self-coached athletes deviate by adding, not skipping. A plan that armors only the direction you don't fail in has left the likelier failure mode unguarded — and you find that out after the fact, in your legs.

**Your call:** what's your rule for the week you feel great and want to add a fourth run — and does the plan know it?

---

### One thing I won't rule on

Your plan contains [joint]-specific guidance and return-to-running conditions — "Replace the next run with swimming or easy cycling," and "recurrent swelling is not something to train through," which "should trigger a sports-medicine or PT reassessment." Whether that protocol is medically adequate is a clinician's question, not a document reviewer's. I checked its structure — those symptom rules are the one limit in this plan with real teeth, and Finding 3 credits them — but I make no judgment on the medicine, and neither should any plan reviewer.

---

## Where this leaves you

The race-week check is passed and your declaration is on the record. The five warnings above are flags, not fails — you may accept any of them; I've said each once and won't nag. This report points at the plan; it doesn't rewrite it. Good luck in October — the call on every finding is yours.

---

## Specimen 4 — The external witness: PASS with 3 flags

**Source:** a real ChatGPT-generated NYC Marathon plan, provided by an
external witness (2026-07-19), reviewed with her consent, previewed by her
before submission.
**Receipt:** `runs/2026-07-20-nyc-marathon-run.txt` (HOLD, 4 uncomputable
race-week rows) → `runs/2026-07-20-nyc-marathon-run2-pace-declared.txt`
(HOLD, narrowed to 1) → `runs/2026-07-20-nyc-marathon-run3-rest-declared.txt`
(CLEAN, gate passes both conditions).
**Why it's here:** this is the repo's external-witness receipt — a real
person, not the builder, generated a real plan and ran it through the
editor. It's also the cleanest demonstration of the HOLD-to-CLEAN path:
two questions asked, two answers recorded, then a pass.

# The Taper Editor — report on your NYC Marathon plan

I read your whole plan. Here's what I found, most important first.

**Your final week passes the one check I refuse to compromise on.** Three things are on the record, each with your name on it: this race is the goal (the plan declares it; you confirmed it); your easy pace is about a 12-minute mile (you stated it — I never guess a pace); and race-week Wednesday's "optional easy swim/rest" is a rest, per your call. With those recorded, the machine count says: your race week averages about 14 minutes of training a day against about 34 a day across the fourteen weeks before it, and race week's biggest session (36 minutes) is a fraction of your biggest training day (four hours — the 20-miler). The plan winds down hard before November 1. That's called a **taper** — reducing training in the last stretch so you arrive at the start rested — and yours passes on both counts. A pass is not a prescription. Three flags below are yours to weigh; I state each once.

Also on the record, as checks performed: all 54 dated sessions in your plan sit on the weekday the plan claims — 54 rows checked, 54 clean, per the committed receipt, and every weekly mileage target I could recompute adds up exactly from its listed runs — ten out of ten.

---

### 1. Two weeks of your plan aren't on the calendar at all.

**Your plan says:** "Week 4: Aug 10–16 — 15–18 mi — 4 easy; 4 easy; 3 easy; 4–6 easy" — and Week 5 reads the same way. Runs with mileage, but no days attached.

**The problem:** *Calendar and arithmetic integrity* — every session in a plan should sit on a date, and every amount should be computable. For your travel weeks, the plan lists runs that exist on no particular day, plus ranges ("4–6 easy," "bike 45–75 min") that aren't numbers until you pick one. Fair is fair: dateless flexibility during travel is sensible coaching, not a defect. But it means my math — including the wind-down I just verified — sees those two weeks as lighter than they may actually be.

**What it costs you:** the plan warns you not to cram mileage around travel, but with no dates and no fixed amounts, neither you nor the plan can later check whether Weeks 4–5 stayed inside their own target. A week that can't be added up can't be kept honest.

**Your call:** when you're on the road, who decides what "4–6 easy" turns into that day — a number you set in advance, or the mood?

---

### 2. The bike has a speed limit with no ticket.

**Your plan says:** "As long runs reach 16, 18, and 20 miles, reduce cycling intensity. A hard two-hour bike ride is not a recovery day simply because it is not running."

**The problem:** *Missing ceiling* — every stated limit needs a defined response for when it's broken. Credit first: this plan's running limits genuinely have teeth ("treat weekly mileage as a ceiling, not a contract," drop the Saturday run before the long run, never cram missed miles). But the cycling limit is advice without a consequence: if you do hammer a two-hour ride the day before your 18-miler, the plan never says what changes — the long run arrives on schedule as if nothing happened.

**What it costs you:** in your peak month, your legs' biggest threat isn't the running the plan counts — it's the riding it doesn't. A limit with no response has silently decided the answer is "nothing," and you'd find that out at mile 14 of a 16-mile Sunday.

**Your call:** if a ride goes hard in October, what changes about that weekend's long run — and says who?

---

### 3. The plan grades its own travel accommodation.

**Your plan says:** "The August 10–26 restriction is manageable and should not be offset by cramming extra-long runs before or immediately after travel."

**The problem:** *Self-certification* — a plan's claims about its own adequacy are claims, not facts. "Manageable" is the plan's own grade for its own solution — and notice it's grading exactly the two weeks that, per Finding 1, sit on no dates and no fixed amounts. The one stretch the plan calls manageable is the one stretch the math can't see.

**What it costs you:** probably little — the advice attached to the claim (don't cram) is sound. But if "manageable" made you stop thinking about August, it did a reviewer's job without a reviewer's work. Whether those weeks were actually manageable will be decided by your legs on August 30, not by that sentence.

**Your call:** what would "Weeks 4–5 went fine" actually look like, in numbers you could check on August 27?

---

### Where this leaves you

The race-week check is passed and all three of your declarations are on the record. The three flags above are warnings, not fails — you may accept any of them; I've said each once and won't nag. This report points at the plan; it doesn't rewrite it, and it doesn't prescribe your training — that stays between you and your plan. See you in November — the call on every finding is yours.

### Witness reaction (2026-07-20, verbatim, consent given)

> I think it's very accurate in reviewing the document and making comments. Meaning the comments it made were accurate so I think your project is a success.
>
> I noticed it's like the response wanted to sound human. I noticed it in these four comments: "...one check I refuse to compromise on", "A pass is not a prescription", "Fair is fair", "I've said each once and won't nag."
>
> That would be the day I'd care about how AI "feels."

Recorded as-is, unedited. This is the repo's honesty tell doing its job: the accuracy claim is externally confirmed, and the voice critique — a real reader flagging the trainer-register phrasing in identity.md as reaching for personality — is kept on the record rather than smoothed over. No change was made to identity.md's voice on the basis of this single reaction; that decision is documented, not avoided.

### Independent professional review (2026-07-20, texted feedback, consent given)

Natalie — a trainer, cross-discipline including runners, and the owner of Specimen 5's strength program — reviewed this specimen's plan and report independently, without seeing `rules.md` first. She is not the Specimen 4 witness; the plan's owner remains anonymous per her recorded terms. Natalie's texted feedback, verbatim:

> Reviewed your plan, it needs metrics to identify what easy, hard, medium look like in terms of pace per mile / speed /
> - Set metric targets
> - Ask for outside training schedule
> - yours attacked the right targets
> - too subjective and generic when written as easy/hard
>
> are you willing to scale your volume swim, running to accommodate your goal
>
> Your prompt is the right direction, addresses intensity / volume, and addresses outside of training/running program

What this converges with, independently: "Ask for outside training schedule" and "addresses outside of training/running program" arrive, blind, at Rule 8 (the solo plan); "needs metrics to identify what easy, hard, medium look like in terms of pace" is Finding 1's computability problem in a coach's words.

What it exposes: "too subjective and generic when written as easy/hard" is broader than anything the checker catches. Rule 3 flags specific rows whose amounts can't be computed — but a plan can state every session in clean, computable minutes and still describe intensity only as "easy" or "hard," anchored to no pace at all, and pass every row check. That gap is logged in `LIMITATIONS.md` as a known limitation, not rushed into a same-day ninth rule — the design gate holds (eight rules is the ceiling; new edge cases become test artifacts or documented boundaries).

Provenance note, kept in the open: this addendum was first recorded 2026-07-20 and was dropped from the repo in that night's rebuild. Restored 2026-07-21, from the reviewer's original texts.

---

## Specimen 5 — Out of scope: DECLINE

**Source:** a real strength-training program (squats, presses, hip thrusts,
rows, Monday/Wednesday/Friday split), linked to what appears to be a
TrueCoach account — provided by an external witness with her consent, as
the deliberate out-of-scope test.
**Receipt:** session run 2026-07-20; declined on both grounds of the scope
precondition, verified against all eight rules individually before
declining, none applicable.
**Why it's here:** this is the receipt for the scope-precondition gate in
rules.md. It demonstrates the editor recognizing two separate reasons a
plan is out of bounds — wrong sport, and not AI-generated — and declining
cleanly instead of inventing findings to have something to say.

# The Taper Editor — response to your strength plan

I read your whole plan. Before I get into findings, I have to flag something more basic first.

This is a strength program — squats, presses, hip thrusts, rows, on a Monday/Wednesday/Friday split. I review AI-generated endurance training plans: running, triathlon, that kind of thing, checking things like whether a race week actually winds down and whether the calendar math holds up. There's no race here, no taper, no endurance load for me to check — the concepts my rules are built around (race-week load, calendar-vs-taper conflicts, phantom pace targets) don't apply to a lifting split. I'd be inventing problems to have something to say, and I won't do that.

One more thing, separate from scope: this plan wasn't generated by an AI. It reads like real programming from a coach — it's linked out to what looks like a TrueCoach account. I'm built to catch the specific failure modes of AI-generated plans (confident arithmetic that doesn't check out, self-certifying language, hollow safeguards). A human coach's program isn't what I'm calibrated against, on top of not being the right sport.

Your call: if you want, I can tell you what I do review — an AI-generated running or triathlon plan, one with a race date on it — and take a real pass at that instead.

### Witness reaction (2026-07-20, reported, not verbatim)

Not a direct quote — relayed by the builder from conversation, not Natalie's own written words, and labeled accordingly rather than formatted like Specimen 4's quoted reaction. Asked why she laughed while reading the report, she said she liked how the AI phrased it.

Recorded as a contrast to Specimen 4: the same trainer-register phrasing the Specimen 4 witness read as reaching for personality landed as likeable, even funny, to a different reader. Kept as reported rather than quoted so the two entries aren't mistaken for the same evidentiary weight.

---

---

## Specimen 6 — The disputed block: BLOCK, on the record

**Source:** a real AI-generated triathlon plan, provided by an external
witness (Pam), reviewed with her consent — the repo's second external
witness. Her full prompt and the plan are committed verbatim
(`evidence-pam-triathlon-verbatim.md`), so every quote below can be checked
by hand. The plan states almost all of its training in yards and miles,
not minutes; race week alone is stated in minutes.
**Receipt:** `runs/2026-07-20-pam-triathlon-run.txt` — verdict BLOCK, exit
code 2, run as written from `pam-triathlon.ledger`. Rerun with the
athlete's own stated paces attached, the block clears — the follow-up
report she received is committed (`witness-pdfs/pamtriathlonfollowup.pdf`;
`pam-triathlon-paced.ledger` and its receipt; the full mechanism, numbers,
and why it isn't patched are in `LIMITATIONS.md`).
**Why it's here:** this is the specimen where the tool disagrees with
itself in public — the checker's verdict was correct for its input and
still misleading about the plan, and the athlete who owns the plan pushed
back on the framing. Both the verdict and the pushback are kept.

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

**The problem:** *Calendar and arithmetic integrity* — the plan never states an actual date, only week numbers and weekday names, so I anchored it using the one fact you gave the AI: this race is always the second weekend in July. That places your race week across July 5–11, 2027 — and the real Anchor Bay Triathlon, publicly scheduled for July 10, 2027, falls on a Saturday. Under the plan's own day-by-day template, the day it calls a light shakeout is the actual race day, and the day it calls "Race Day" is the Sunday after the race already happened.

**What it costs you:** if you followed the plan's labels as written, you'd expect one more easy day between your shakeout and the start line. There isn't one.

**Your call:** which governs — the plan's generic Saturday/Sunday template, or the real date?

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

## What these six specimens cover, together

- **HOLD, BLOCK (twice), PASS (twice), and DECLINE** — every verdict the editor can return, each backed by a dated receipt.
- **Two independent passes** (Specimens 3 and 4) from two different real plans, generated by two different people, on two different platforms — the same voice, the same four-part contract, different findings each time because the findings come from the plan, not a template.
- **Two external-witness sessions** (Specimens 4 and 6) and **one out-of-scope session** (Specimen 5), all from people who are not the builder, all consented and previewed before use.
- **One planted, labeled trap** (Specimen 2) that anyone can re-spring themselves — and **one live, disputed block** (Specimen 6) where a real user pushed back on the tool's framing and the disagreement is kept unresolved, on the record.
