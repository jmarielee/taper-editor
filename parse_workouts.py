"""Extract workouts for a date window from an Apple Health export.xml stream.

Usage: unzip -p export.zip apple_health_export/export.xml | python3 parse_workouts.py
Reads XML from stdin, prints a daily workout table for the window.
Extracts ONLY Workout elements: date, type, duration, distance, energy.
No heart rate, no sleep, no other health records are read or kept.
"""
import sys
import xml.etree.ElementTree as ET
from datetime import date

WINDOW_START = date(2025, 7, 1)
WINDOW_END = date(2025, 7, 13)  # exclusive

def in_window(datestr):
    # startDate like "2025-07-06 08:15:32 -0400"
    try:
        d = date.fromisoformat(datestr[:10])
    except ValueError:
        return False
    return WINDOW_START <= d < WINDOW_END

rows = []
context = ET.iterparse(sys.stdin.buffer, events=("end",))
for _, elem in context:
    if elem.tag == "Workout":
        start = elem.get("startDate", "")
        if in_window(start):
            wtype = elem.get("workoutActivityType", "").replace("HKWorkoutActivityType", "")
            dur = elem.get("duration", "")
            dur_unit = elem.get("durationUnit", "min")
            dist = elem.get("totalDistance", "")
            dist_unit = elem.get("totalDistanceUnit", "")
            energy = elem.get("totalEnergyBurned", "")
            # Newer exports put distance/energy in child WorkoutStatistics.
            # Collect all distance stats, then prefer the one matching the sport
            # (fixes swim distances: DistanceSwimming, not another distance type).
            lap_len = None
            for md in elem.findall("MetadataEntry"):
                if md.get("key") == "HKLapLength":
                    try:
                        lap_len = float(md.get("value", "").split()[0])
                    except (ValueError, IndexError):
                        lap_len = None
            dist_stats = {}
            for stat in elem.findall("WorkoutStatistics"):
                st = stat.get("type", "")
                if "Distance" in st:
                    dist_stats[st] = (stat.get("sum", ""), stat.get("unit", ""))
                if "ActiveEnergyBurned" in st and not energy:
                    energy = stat.get("sum", "")
            if dist_stats:
                preferred = None
                if wtype == "Swimming":
                    preferred = dist_stats.get("HKQuantityTypeIdentifierDistanceSwimming")
                elif wtype == "Cycling":
                    preferred = dist_stats.get("HKQuantityTypeIdentifierDistanceCycling")
                elif wtype in ("Running", "Walking", "Hiking"):
                    preferred = dist_stats.get("HKQuantityTypeIdentifierDistanceWalkingRunning")
                if preferred is None:
                    preferred = next(iter(dist_stats.values()))
                if not dist:
                    dist, dist_unit = preferred
                # Watch lap length misconfigured (e.g. 1 m): the "distance" is
                # really a lap count. Report laps honestly; do not invent meters.
                if wtype == "Swimming" and lap_len is not None and lap_len <= 2:
                    dist, dist_unit = dist, "laps*"
            rows.append({
                "date": start[:10],
                "time": start[11:16],
                "type": wtype,
                "duration": f"{float(dur):.0f} {dur_unit}" if dur else "?",
                "distance": f"{float(dist):.2f} {dist_unit}" if dist else "-",
                "energy_kcal": f"{float(energy):.0f}" if energy else "-",
            })
        elem.clear()
    elif elem.tag in ("Record", "ClinicalRecord", "Correlation"):
        # Health records outside scope: cleared immediately, never inspected
        elem.clear()

rows.sort(key=lambda r: (r["date"], r["time"]))
if not rows:
    print("No workouts found in window 2025-07-01 .. 2025-07-12")
else:
    print(f"{'Date':<12}{'Start':<8}{'Type':<28}{'Duration':<12}{'Distance':<14}{'Energy':<8}")
    print("-" * 84)
    for r in rows:
        print(f"{r['date']:<12}{r['time']:<8}{r['type']:<28}{r['duration']:<12}{r['distance']:<14}{r['energy_kcal']:<8}")
    print(f"\n{len(rows)} workouts in window")
    if any(r["distance"].endswith("laps*") for r in rows):
        print("* Watch pool lap length was set to 1 m, so swim distance was recorded as a lap count.")
        print("  True distance = laps x actual pool length (unverified from this export alone).")
