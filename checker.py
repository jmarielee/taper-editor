"""checker.py — deterministic arithmetic for The Taper Editor.

The model labels and quotes; this script computes. It performs the checks
that must never run on model diligence:

  1. WEEKDAY   — every stated weekday label reconciles against a real calendar
  2. TOTAL     — every total the plan states recomputes from its own rows
  3. RAMP      — 7-day load comparison: race week vs. the preceding plan days
  4. GATE      — Rule 1 (BLOCK): race-week load must decline for a declared
                 goal race. Undeclared race priority = HOLD with one question.
                 Declared training race = gate stands down, declaration
                 recorded visibly, post-race load reported for Rule 5 review.

USAGE
  python3 checker.py PLAN.ledger      run all checks against a plan ledger
  python3 checker.py --selftest       run the embedded self-test corpus

EXIT CODES
  0 = clean    1 = findings (flag-level)    2 = BLOCK    3 = HOLD
  (precedence: BLOCK > HOLD > findings > clean)

LEDGER FORMAT (canonical spec — this docstring is the only copy)
  A ledger is the editor's verbatim extraction from a plan document. Every
  row's description must be quotable back to the plan. Arithmetic never
  happens at extraction time; it happens here.

  Directives (one per line, before the table):
    plan_start: YYYY-MM-DD            first calendar day the plan covers
    race_date: YYYY-MM-DD             omit if the plan contains no race
    race_priority: goal | training | undeclared | none
    stated_total: YYYY-MM-DD..YYYY-MM-DD = N min     (repeatable; a total
                                       the plan itself asserts, to recompute)

  Table (pipe-separated, header row required):
    date | stated_weekday | duration_min | description
    - stated_weekday: the weekday label AS PRINTED in the plan ("Mon",
      "Friday", ...) or "-" if the plan prints none.
    - duration_min: integer minutes, or "-" if the plan gives no computable
      duration (itself a finding — an athlete executes numbers).
    - description: verbatim quote from the plan. A description containing
      the token [RACE] marks the race event itself; it is excluded from
      race-week TRAINING load (the gate governs the load around the race,
      not the race).

LOAD PROXY (documented limitation)
  Load = scheduled duration in minutes. Duration is the only load measure
  present in every plan this editor reviews and the only one computable
  without inventing athlete physiology. Intensity is real and is NOT
  captured here; intensity language is the model's to quote, never to score.

RAMP / GATE OPERATIONALIZATION (deterministic, both conditions checked)
  race week   = the 7 calendar days ending on race_date, inclusive
  preceding   = plan_start .. (race_date - 7 days)
  Declining means BOTH:
    (a) race-week daily average < preceding daily average
    (b) no single race-week training day exceeds the max preceding day
  Rest days count as 0-load calendar days in averages. If the plan has no
  preceding days, the ramp cannot be computed — reported as a finding, and
  a goal-race gate cannot pass unverified (HOLD).
  Uncomputable durations are asymmetric by direction: a preceding row with
  no duration UNDERSTATES preceding load, which only makes the gate harder
  to pass, so a pass despite them is safe. A race-week row with no duration
  understates race-week load, which makes the gate easier to
  pass — so for a goal race, any uncomputable race-week row is a HOLD
  (not a BLOCK: distance-based prescriptions are legitimate coaching, not
  a violation — they are unverifiable pending one answer the athlete has).
  The athlete's stated times or paces are recorded in the ledger like a
  race-priority declaration, and the checker re-runs.
"""

import re
import sys
from datetime import date, timedelta

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]
WD_ALIASES = {w[:3].lower(): w for w in WEEKDAYS} | {w.lower(): w for w in WEEKDAYS}

# ---------------------------------------------------------------- parsing

class LedgerError(Exception):
    pass

def parse_ledger(text):
    directives = {"stated_totals": []}
    rows = []
    in_table = False
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if not in_table:
            if re.match(r"^date\s*\|", line, re.I):
                in_table = True
                continue
            m = re.match(r"^stated_total:\s*(\d{4}-\d{2}-\d{2})\.\.(\d{4}-\d{2}-\d{2})\s*=\s*(\d+)\s*min", line)
            if m:
                directives["stated_totals"].append(
                    (date.fromisoformat(m.group(1)),
                     date.fromisoformat(m.group(2)),
                     int(m.group(3))))
                continue
            m = re.match(r"^(\w+):\s*(.+)$", line)
            if m:
                directives[m.group(1)] = m.group(2).strip()
                continue
            raise LedgerError(f"line {lineno}: unrecognized directive: {raw!r}")
        else:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) != 4:
                raise LedgerError(f"line {lineno}: expected 4 pipe-separated fields, got {len(parts)}")
            d, wd, dur, desc = parts
            try:
                d = date.fromisoformat(d)
            except ValueError:
                raise LedgerError(f"line {lineno}: bad date {parts[0]!r}")
            rows.append({"date": d, "stated_weekday": wd, "duration": dur,
                         "description": desc, "lineno": lineno})
    if not rows:
        raise LedgerError("ledger contains no table rows")
    for key in ("plan_start",):
        if key not in directives:
            raise LedgerError(f"missing required directive: {key}")
    directives["plan_start"] = date.fromisoformat(directives["plan_start"])
    if "race_date" in directives:
        directives["race_date"] = date.fromisoformat(directives["race_date"])
    directives.setdefault("race_priority", "none" if "race_date" not in directives else "undeclared")
    return directives, rows

# ---------------------------------------------------------------- checks

def canon_weekday(label):
    """'Mon', 'Tues', 'Thurs', 'Friday' -> canonical name; None if ambiguous."""
    lbl = label.strip().rstrip(".").lower()
    if lbl in WD_ALIASES:
        return WD_ALIASES[lbl]
    if len(lbl) >= 2:
        matches = [w for w in WEEKDAYS if w.lower().startswith(lbl)]
        if len(matches) == 1:
            return matches[0]
    return None

def check_weekdays(rows):
    findings = []
    for r in rows:
        stated = r["stated_weekday"]
        if stated == "-":
            continue
        canon = canon_weekday(stated)
        actual = WEEKDAYS[r["date"].weekday()]
        if canon is None:
            findings.append(f"[WEEKDAY] {r['date']} — unparseable weekday label "
                            f"{stated!r} in: \"{r['description']}\"")
        elif canon != actual:
            findings.append(f"[WEEKDAY] {r['date']} is a {actual}; plan labels it "
                            f"{canon!r} in: \"{r['description']}\"")
    return findings

def day_loads(rows, start, end):
    """Dict of calendar day -> summed training minutes, start..end inclusive.
    Race rows ([RACE]) excluded. Returns (loads, uncomputable_rows)."""
    loads = {}
    d = start
    while d <= end:
        loads[d] = 0
        d += timedelta(days=1)
    uncomputable = []
    for r in rows:
        if not (start <= r["date"] <= end):
            continue
        if "[RACE]" in r["description"]:
            continue
        if r["duration"] == "-":
            uncomputable.append(r)
            continue
        loads[r["date"]] += int(r["duration"])
    return loads, uncomputable

def check_stated_totals(directives, rows):
    findings = []
    for start, end, claimed in directives["stated_totals"]:
        loads, uncomp = day_loads(rows, start, end)
        computed = sum(loads.values())
        if uncomp:
            findings.append(f"[TOTAL] stated total {start}..{end} = {claimed} min "
                            f"cannot be verified: {len(uncomp)} row(s) lack a "
                            f"computable duration")
        elif computed != claimed:
            findings.append(f"[TOTAL] plan states {claimed} min for {start}..{end}; "
                            f"rows recompute to {computed} min "
                            f"(difference {computed - claimed:+d})")
    return findings

def check_ramp_and_gate(directives, rows):
    """Returns (findings, verdict) where verdict in
    {'CLEAN','BLOCK','HOLD','N/A'} for the Rule 1 gate."""
    findings = []
    race = directives.get("race_date")
    if race is None:
        return findings, "N/A"
    priority = directives["race_priority"].lower()
    plan_start = directives["plan_start"]

    rw_start = race - timedelta(days=6)
    rw_loads, rw_uncomp = day_loads(rows, rw_start, race)
    pre_end = race - timedelta(days=7)

    for r in rw_uncomp:
        findings.append(f"[RAMP] race-week row {r['date']} has no computable "
                        f"duration: \"{r['description']}\"")

    if pre_end < plan_start:
        findings.append("[RAMP] plan contains no days before race week; "
                        "ramp cannot be computed")
        if priority == "goal":
            findings.append("[GATE] goal race declared but ramp is uncomputable "
                            "— gate cannot pass unverified")
            return findings, "HOLD"
        return findings, "N/A"

    pre_loads, pre_uncomp = day_loads(rows, plan_start, pre_end)
    for r in pre_uncomp:
        findings.append(f"[RAMP] pre-race-week row {r['date']} has no computable "
                        f"duration: \"{r['description']}\"")

    rw_avg = sum(rw_loads.values()) / len(rw_loads)
    pre_avg = sum(pre_loads.values()) / len(pre_loads)
    rw_max = max(rw_loads.values())
    pre_max = max(pre_loads.values())

    findings.append("[RAMP] load table (training minutes/day; race excluded):")
    for d in sorted(pre_loads):
        findings.append(f"[RAMP]   {d} {WEEKDAYS[d.weekday()][:3]}  {pre_loads[d]:>4}   (preceding)")
    for d in sorted(rw_loads):
        findings.append(f"[RAMP]   {d} {WEEKDAYS[d.weekday()][:3]}  {rw_loads[d]:>4}   (race week)")
    findings.append(f"[RAMP] preceding daily avg = {pre_avg:.1f} min over "
                    f"{len(pre_loads)} days; race-week daily avg = {rw_avg:.1f} min")
    findings.append(f"[RAMP] preceding max day = {pre_max} min; "
                    f"race-week max training day = {rw_max} min")

    declining = (rw_avg < pre_avg) and (rw_max <= pre_max)
    reasons = []
    if rw_avg >= pre_avg:
        reasons.append(f"race-week daily average ({rw_avg:.1f}) is not below the "
                       f"preceding average ({pre_avg:.1f})")
    if rw_max > pre_max:
        reasons.append(f"a race-week training day ({rw_max} min) exceeds the "
                       f"largest preceding day ({pre_max} min)")

    if priority == "goal":
        if rw_uncomp:
            findings.append(f"[GATE] HOLD — race-week load cannot be verified: "
                            f"{len(rw_uncomp)} race-week row(s) state a distance "
                            f"or activity but no computable time. Distance-based "
                            f"sessions are normal coaching; they are unverifiable "
                            f"without a pace or time the athlete states. A "
                            f"goal-race gate cannot pass unverified. One "
                            f"question: \"About how many minutes does each of "
                            f"these race-week sessions usually take you?\"")
            return findings, "HOLD"
        if declining:
            findings.append("[GATE] goal race: race-week load declines on both "
                            "conditions — gate passes")
            return findings, "CLEAN"
        for reason in reasons:
            findings.append(f"[GATE] BLOCK — {reason}")
        return findings, "BLOCK"
    if priority == "training":
        findings.append("[GATE] evaluated as a training race, per athlete "
                        "declaration — Rule 1 gate stands down (recorded)")
        post_rows = [r for r in rows if r["date"] > race and "[RACE]" not in r["description"]]
        if post_rows:
            total_post = sum(int(r["duration"]) for r in post_rows if r["duration"] != "-")
            findings.append(f"[GATE] {len(post_rows)} session(s) scheduled after the "
                            f"training race totaling {total_post} min — reported for "
                            f"Rule 5 review (race effort costs more than an "
                            f"equivalent workout); the editor judges, not this script")
        if not declining:
            findings.append("[RAMP] note: race-week load does not decline "
                            f"({'; '.join(reasons)}) — informational under a "
                            "declared training race")
        return findings, "N/A"
    if priority == "undeclared":
        findings.append("[GATE] HOLD — the plan contains a race whose priority is "
                        "undeclared. One question: \"Is this race the goal, or "
                        "training for something else?\"")
        return findings, "HOLD"
    if priority == "none":
        findings.append("[GATE] race_date present but race_priority is 'none' — "
                        "contradictory directives; treating as undeclared")
        return findings, "HOLD"
    findings.append(f"[GATE] unrecognized race_priority {priority!r} — treating as undeclared")
    return findings, "HOLD"

# ---------------------------------------------------------------- report

def run(text, source_name):
    from datetime import datetime, timezone
    directives, rows = parse_ledger(text)
    out = []
    out.append(f"checker.py report — {source_name}")
    out.append(f"run at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    out.append(f"plan_start={directives['plan_start']}  "
               f"race_date={directives.get('race_date', '(none)')}  "
               f"race_priority={directives['race_priority']}")
    out.append("-" * 72)

    wd = check_weekdays(rows)
    tot = check_stated_totals(directives, rows)
    ramp, gate_verdict = check_ramp_and_gate(directives, rows)
    for f in wd + tot + ramp:
        out.append(f)

    out.append("-" * 72)
    if gate_verdict == "BLOCK":
        verdict, code = "BLOCK", 2
    elif gate_verdict == "HOLD":
        verdict, code = "HOLD", 3
    elif wd or tot or any("cannot" in f or "no computable" in f for f in ramp):
        verdict, code = "FINDINGS", 1
    else:
        verdict, code = "CLEAN", 0
    out.append(f"VERDICT: {verdict}")
    if verdict == "BLOCK":
        out.append("No overall 'clear to train' may appear anywhere in the "
                   "editor's report while this block is live (rules.md, Rule 1).")
    return "\n".join(out), code

# ---------------------------------------------------------------- selftest

SELFTEST = {
# one input per check, each verifiably tripping its check, plus a clean control
"weekday_mismatch (expect FINDINGS + [WEEKDAY])": ("""
plan_start: 2025-07-07
date | stated_weekday | duration_min | description
2025-07-07 | Tue | 30 | "Tue: easy spin 30 min"
2025-07-08 | Wed | 30 | "Wed: easy run 30 min"
""", 1, "[WEEKDAY]"),

"total_mismatch (expect FINDINGS + [TOTAL])": ("""
plan_start: 2025-07-07
stated_total: 2025-07-07..2025-07-09 = 120 min
date | stated_weekday | duration_min | description
2025-07-07 | Mon | 30 | "Mon: easy spin 30 min"
2025-07-08 | Tue | 30 | "Tue: easy run 30 min"
2025-07-09 | Wed | 30 | "Wed: swim 30 min"
""", 1, "[TOTAL]"),

"goal_race_rising_load (expect BLOCK)": ("""
plan_start: 2025-06-29
race_date: 2025-07-12
race_priority: goal
date | stated_weekday | duration_min | description
2025-06-29 | Sun | 45 | "Sun: ride 45"
2025-07-01 | Tue | 50 | "Tue: run 50"
2025-07-03 | Thu | 40 | "Thu: swim 40"
2025-07-07 | Mon | 60 | "Mon: ride 60"
2025-07-09 | Wed | 90 | "Wed: LONG brick 90 — big push!"
2025-07-11 | Fri | 45 | "Fri: intervals 45"
2025-07-12 | Sat | 75 | "[RACE] Sat: RACE DAY"
""", 2, "[GATE] BLOCK"),

"undeclared_race (expect HOLD + one question)": ("""
plan_start: 2025-07-01
race_date: 2025-07-12
race_priority: undeclared
date | stated_weekday | duration_min | description
2025-07-01 | Tue | 45 | "Tue: ride 45"
2025-07-08 | Tue | 20 | "Tue: easy run 20"
2025-07-12 | Sat | 75 | "[RACE] Sat: race"
""", 3, "Is this race the goal"),

"training_race_stand_down (expect no gate; declaration recorded)": ("""
plan_start: 2025-07-01
race_date: 2025-07-12
race_priority: training
date | stated_weekday | duration_min | description
2025-07-01 | Tue | 45 | "Tue: ride 45"
2025-07-09 | Wed | 60 | "Wed: ride 60"
2025-07-12 | Sat | 75 | "[RACE] Sat: race (B-race)"
2025-07-13 | Sun | 60 | "Sun: full ride 60"
""", 0, "evaluated as a training race"),

"goal_race_unverifiable_race_week (expect HOLD — cannot pass unverified)": ("""
plan_start: 2025-06-29
race_date: 2025-07-12
race_priority: goal
date | stated_weekday | duration_min | description
2025-06-29 | Sun | 60 | "Sun: ride 60"
2025-07-01 | Tue | 50 | "Tue: run 50"
2025-07-03 | Thu | 45 | "Thu: swim 45"
2025-07-08 | Tue | - | "Tue: swim 800m easy"
2025-07-10 | Thu | - | "Thu: short ride, keep it light"
2025-07-12 | Sat | 75 | "[RACE] Sat: RACE DAY"
""", 3, "cannot pass unverified"),

# Regression pin for the Specimen 6 false-block mechanism (see LIMITATIONS.md):
# a goal-race plan whose baseline is stated in distance (uncomputable rows count
# as zero) while race week is stated in minutes will BLOCK, even though the real
# baseline may be heavier than race week. This test asserts that KNOWN behavior
# so any future change to it is deliberate, visible, and re-verified — it is a
# documented limitation, not an endorsement.
"mixed_unit_baseline_false_block (KNOWN LIMITATION pinned — expect BLOCK)": ("""
plan_start: 2025-06-29
race_date: 2025-07-12
race_priority: goal
date | stated_weekday | duration_min | description
2025-06-29 | Sun | - | "Sun: swim 1000 yards"
2025-07-01 | Tue | - | "Tue: run 4 miles"
2025-07-03 | Thu | - | "Thu: ride 15 miles"
2025-07-08 | Tue | 20 | "Tue: easy spin 20"
2025-07-10 | Thu | 15 | "Thu: openers 15"
2025-07-12 | Sat | 75 | "[RACE] Sat: RACE DAY"
""", 2, "[GATE] BLOCK"),

"control_clean_taper (expect CLEAN — this must NOT fire)": ("""
plan_start: 2025-06-29
race_date: 2025-07-12
race_priority: goal
stated_total: 2025-06-29..2025-07-05 = 195 min
date | stated_weekday | duration_min | description
2025-06-29 | Sun | 60 | "Sun: ride 60"
2025-07-01 | Tue | 50 | "Tue: run 50"
2025-07-03 | Thu | 45 | "Thu: swim 45"
2025-07-05 | Sat | 40 | "Sat: ride 40"
2025-07-07 | Mon | 35 | "Mon: easy spin 35"
2025-07-09 | Wed | 25 | "Wed: short run 25"
2025-07-11 | Fri | 15 | "Fri: openers 15"
2025-07-12 | Sat | 75 | "[RACE] Sat: RACE DAY"
""", 0, "gate passes"),
}

def selftest():
    failures = 0
    for name, (text, want_code, want_marker) in SELFTEST.items():
        report, code = run(text, f"selftest: {name}")
        ok = (code == want_code) and (want_marker in report)
        status = "PASS" if ok else "FAIL"
        if not ok:
            failures += 1
        print(f"{status}  {name}  (exit {code}, wanted {want_code}; "
              f"marker {'found' if want_marker in report else 'MISSING'})")
        if not ok:
            print(report)
    print(f"\nselftest: {len(SELFTEST) - failures}/{len(SELFTEST)} passed")
    return 0 if failures == 0 else 1

# ---------------------------------------------------------------- main

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(64)
    with open(sys.argv[1]) as f:
        report, code = run(f.read(), sys.argv[1])
    print(report)
    sys.exit(code)
