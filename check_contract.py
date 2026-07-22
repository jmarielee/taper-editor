"""check_contract.py — deterministic gate for The Taper Editor's OUTPUT CONTRACT.

checker.py proves the *arithmetic* (race-week load). This proves the *contract*:
the promises identity.md and rules.md make about the shape of every report.

It enforces four things, in code, so they can never quietly rot back into prose:

  1. STRUCTURE   — every finding carries all four parts, in order:
                   "Your plan says" / "The problem" / "What it costs you" /
                   "Your call". A finding missing a part, or with them out of
                   order, is blocked. (Heading style doesn't matter; a finding
                   is any section that quotes the plan.)
  2. QUESTION    — every "Your call" hands back a question (contains '?'). This
                   is the no-rewrite rule with teeth: a handoff that is a bare
                   statement, a prescription, or a fix instead of a question is
                   blocked. (It does not attempt to judge tone beyond that; the
                   failure mode it guards is the one that actually occurred —
                   a "Your call" that asks the athlete nothing.)
  3. FABRICATION — every quote in "Your plan says" must appear, as a contiguous
                   run of words, in the specimen's committed evidence file.
                   Matching is word-based: whitespace, table delimiters, emoji,
                   bold markers, and dash style are flattened (rules.md permits
                   flattening table/whitespace formatting), but the WORDS and
                   their order must be present. Invent or reorder words and it
                   fails, no matter how convincing it reads.
  4. COVERAGE    — a report with a shipped evidence file must be quote-checked;
                   a report without one (nyc, by the anonymous witness's terms)
                   is reported SKIPPED, not silently passed.

USAGE
  python3 check_contract.py            # gate every committed report; exit 1 on any block
  python3 check_contract.py --selftest # prove the gate: clears clean, blocks broken
"""

import os
import re
import sys

# report file -> its committed verbatim source (None = no source shipped, by policy)
EVIDENCE = {
    "report-2025-adjusted-plan.md": "evidence-adjusted-plan-verbatim.md",
    "report-trap-plan-block.md":    "trap-plan.md",
    "report-detroit-half-pass.md":  "evidence-detroit-half-verbatim.md",
    "report-nyc-marathon.md":       None,   # anonymous witness; source not shipped, on the record
    "report-pam-triathlon.md":      "evidence-pam-triathlon-verbatim.md",
}

PARTS = ["Your plan says", "The problem", "What it costs you", "Your call"]
MIN_QUOTE_WORDS = 4   # fragments shorter than this aren't fabrication-checked (reported honestly)

# ---------------------------------------------------------------- word matching

def words(text):
    """Lowercase word-tokens; drops punctuation, dashes, emoji, bold markers, pipes."""
    return re.findall(r"[a-z0-9]+", text.lower())

def contains_run(haystack_words, needle_words):
    """True if needle_words appears as a contiguous run inside haystack_words."""
    n = len(needle_words)
    if n == 0:
        return True
    for i in range(len(haystack_words) - n + 1):
        if haystack_words[i:i + n] == needle_words:
            return True
    return False

def strip_metadata(report):
    """Remove the leading HTML-comment repo-metadata block; not athlete-facing."""
    return re.sub(r"<!--.*?-->", "", report, flags=re.S)

# ---------------------------------------------------------------- parsing

def split_findings(report):
    """A finding is any heading-delimited section that quotes the plan.
    Works for numbered '## N.' headings and unnumbered '###' headings alike."""
    body = strip_metadata(report)
    chunks = re.split(r"(?m)^#{1,6}\s+", body)
    return [c for c in chunks if "**Your plan says:**" in c]

def field(finding, label):
    m = re.search(r"\*\*" + re.escape(label) + r":\*\*\s*(.+)", finding)
    return m.group(1).strip() if m else None

def quoted_fragments(plan_says):
    """Every "..."-quoted span, split on ellipsis into checkable word-fragments."""
    frags = []
    src = plan_says.replace("\u201c", '"').replace("\u201d", '"')
    for span in re.findall(r'"([^"]+)"', src):
        for piece in re.split(r"\.\.\.|\u2026", span):
            w = words(piece)
            if len(w) >= MIN_QUOTE_WORDS:
                frags.append((piece.strip(), w))
    return frags

# ---------------------------------------------------------------- checks

def check_report(report_text, evidence_text):
    """Return (violations, (quotes_checked, reports_skipped))."""
    violations = []
    checked = 0
    findings = split_findings(report_text)
    if not findings:
        violations.append(("STRUCTURE", "no findings parsed (no section quotes the plan)"))
    hay = words(evidence_text) if evidence_text is not None else None
    for i, f in enumerate(findings, 1):
        # 1. structure: all parts present, in order
        idxs = []
        for part in PARTS:
            j = f.find(f"**{part}:**")
            if j < 0:
                violations.append(("STRUCTURE", f"finding {i}: missing '{part}'"))
            else:
                idxs.append(j)
        if idxs != sorted(idxs):
            violations.append(("STRUCTURE", f"finding {i}: four parts out of order"))
        # 2. question
        yc = field(f, "Your call")
        if yc is not None and "?" not in yc:
            violations.append(("QUESTION", f"finding {i}: 'Your call' asks no question -> {yc[:70]}"))
        # 3. fabrication
        if hay is not None:
            ps = field(f, "Your plan says")
            if ps:
                for original, w in quoted_fragments(ps):
                    if contains_run(hay, w):
                        checked += 1
                    else:
                        violations.append(("FABRICATION",
                                           f'finding {i}: quote not found in source -> "{original[:70]}"'))
    skipped = 1 if evidence_text is None else 0
    return violations, (checked, skipped)

# ---------------------------------------------------------------- runners

def gate_repo(root="."):
    total_v = 0
    files = 0
    for report, ev in EVIDENCE.items():
        path = os.path.join(root, report)
        if not os.path.exists(path):
            print(f"MISSING  {report}")
            total_v += 1
            continue
        files += 1
        report_text = open(path, encoding="utf-8").read()
        ev_text = open(os.path.join(root, ev), encoding="utf-8").read() if ev else None
        violations, (checked, _) = check_report(report_text, ev_text)
        if violations:
            print(f"BLOCK    {report}")
            for code, detail in violations:
                print(f"           [{code}] {detail}")
            total_v += len(violations)
        else:
            note = f"{checked} quote(s) verified against source" if ev \
                   else "fabrication check SKIPPED (no source shipped, by policy)"
            print(f"PASS     {report}  ({note})")
    print("-" * 72)
    print(f"contract gate: {files} report(s) checked, {total_v} violation(s)")
    return 0 if total_v == 0 else 1

# ---------------------------------------------------------------- selftest

_EV = "Week 1 notes: the quick brown fox jumps over the lazy dog, then rests."
_GOODQ = "What will you change about this before race day?"

def _mini(plan_says, your_call, drop=None):
    parts = {
        "Your plan says": plan_says,
        "The problem": "something is off.",
        "What it costs you": "it costs you time.",
        "Your call": your_call,
    }
    if drop:
        parts.pop(drop)
    body = "## 1. A finding\n\n"
    for k in ["Your plan says", "The problem", "What it costs you", "Your call"]:
        if k in parts:
            body += f"**{k}:** {parts[k]}\n\n"
    return body

def selftest():
    cases = [
        ("clean report clears the gate",
         _mini('"the quick brown fox jumps over the lazy dog"', _GOODQ), None),
        ("question + parenthetical still clears",
         _mini('"the quick brown fox jumps over the lazy dog"',
               "Does the plan know that? (It doesn't.)"), None),
        ("flattened table row still clears (emoji/dashes/tabs ignored)",
         _mini('"the quick brown fox — jumps over — the lazy dog"', _GOODQ), None),
        ("handoff that isn't a question is blocked",
         _mini('"the quick brown fox jumps over the lazy dog"',
               "Change the final week so it tapers."), "QUESTION"),
        ("handoff that ends in a fix is blocked",
         _mini('"the quick brown fox jumps over the lazy dog"',
               "Rewrite slide 8 to fix the magnification error."), "QUESTION"),
        ("fabricated quote is blocked",
         _mini('"the lazy cat sleeps all afternoon in the warm sun"', _GOODQ), "FABRICATION"),
        ("reordered words are blocked (not a verbatim run)",
         _mini('"the brown quick fox jumps over the lazy dog"', _GOODQ), "FABRICATION"),
        ("missing a required part is blocked",
         _mini('"the quick brown fox jumps over the lazy dog"', _GOODQ, drop="What it costs you"),
         "STRUCTURE"),
    ]
    failures = 0
    for name, report, want in cases:
        violations, _ = check_report(report, _EV)
        codes = {c for c, _ in violations}
        ok = (not violations) if want is None else (want in codes)
        print(f"{'PASS' if ok else 'FAIL'}  {name}"
              + ("" if ok else f"  (wanted {want}, got {sorted(codes) or 'none'})"))
        failures += 0 if ok else 1
    print(f"\ncontract selftest: {len(cases) - failures}/{len(cases)} passed")
    return 0 if failures == 0 else 1

# ---------------------------------------------------------------- main

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--selftest":
        sys.exit(selftest())
    root = sys.argv[1] if len(sys.argv) == 2 else "."
    sys.exit(gate_repo(root))
