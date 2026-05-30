"""Standalone chart generator using extracted Zone 2 data."""

from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

OUTPUT_DIR = Path(__file__).parent.parent / "output"
TARGET_HR = 125
ZONE2_MIN = 121
ZONE2_MAX = 131
LSD_MIN_MIN = 75  # minutes
MERGE_GAP_MIN = 30

records = [
    {"date": "2026-05-09", "start_time": "20:45", "duration_min": 60.1, "avg_pace": "10:15", "avg_hr": 126},
    {"date": "2026-05-11", "start_time": "06:52", "duration_min": 60.1, "avg_pace": "9:58",  "avg_hr": 128},
    {"date": "2026-05-12", "start_time": "20:54", "duration_min": 60.1, "avg_pace": "10:14", "avg_hr": 130},
    {"date": "2026-05-14", "start_time": "20:28", "duration_min": 60.1, "avg_pace": "9:40",  "avg_hr": 130},
    {"date": "2026-05-16", "start_time": "06:13", "duration_min": 90.6, "avg_pace": "8:53",  "avg_hr": 137},
    {"date": "2026-05-18", "start_time": "07:41", "duration_min": 60.1, "avg_pace": "9:29",  "avg_hr": 129},
    {"date": "2026-05-20", "start_time": "07:44", "duration_min": 64.3, "avg_pace": "9:20",  "avg_hr": 131},
    {"date": "2026-05-21", "start_time": "20:58", "duration_min": 60.1, "avg_pace": "9:34",  "avg_hr": 130},
    {"date": "2026-05-23", "start_time": "07:00", "duration_min": 80.3, "avg_pace": "9:12",  "avg_hr": 138},
    {"date": "2026-05-23", "start_time": "08:30", "duration_min": 4.0,  "avg_pace": "10:02", "avg_hr": 141},
    {"date": "2026-05-23", "start_time": "08:42", "duration_min": 9.5,  "avg_pace": "9:54",  "avg_hr": 132},
    {"date": "2026-05-25", "start_time": "20:09", "duration_min": 60.1, "avg_pace": "9:04",  "avg_hr": 128},
    {"date": "2026-05-27", "start_time": "06:26", "duration_min": 60.1, "avg_pace": "9:06",  "avg_hr": 131},
    {"date": "2026-05-28", "start_time": "21:23", "duration_min": 40.4, "avg_pace": "9:06",  "avg_hr": 129},
    {"date": "2026-05-30", "start_time": "06:13", "duration_min": 94.0, "avg_pace": "8:32",  "avg_hr": 138},
]

def merge_same_day_runs(recs):
    from itertools import groupby
    sorted_recs = sorted(recs, key=lambda r: (r["date"], r.get("start_time") or ""))
    merged = []
    for date, group in groupby(sorted_recs, key=lambda r: r["date"]):
        group = list(group)
        if any(r.get("start_time") is None for r in group):
            merged.extend(group)
            continue
        stack = [group[0]]
        for nxt in group[1:]:
            cur = stack[-1]
            end_min = _time_to_min(cur["start_time"]) + cur["duration_min"]
            gap = _time_to_min(nxt["start_time"]) - end_min
            if gap < MERGE_GAP_MIN:
                stack[-1] = _combine(cur, nxt)
            else:
                stack.append(nxt)
        merged.extend(stack)
    return merged

def _time_to_min(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)

def _combine(a, b):
    a_dist = a["duration_min"] / (pace_to_sec(a["avg_pace"]) / 60)
    b_dist = b["duration_min"] / (pace_to_sec(b["avg_pace"]) / 60)
    total_dist = a_dist + b_dist
    total_dur = a["duration_min"] + b["duration_min"]
    merged_pace_sec = (total_dur / total_dist) * 60
    merged_hr = (a["avg_hr"] * a["duration_min"] + b["avg_hr"] * b["duration_min"]) / total_dur
    return {
        "date": a["date"],
        "start_time": a["start_time"],
        "duration_min": round(total_dur, 1),
        "avg_pace": sec_to_pace(merged_pace_sec),
        "avg_hr": round(merged_hr),
    }

def classify(duration_min, avg_hr):
    if duration_min >= LSD_MIN_MIN:
        return "LSD"
    if ZONE2_MIN <= avg_hr <= ZONE2_MAX:
        return "Zone 2"
    return "Other"

def pace_to_sec(s):
    m, sec = s.split(":")
    return int(m) * 60 + int(sec)

def sec_to_pace(s):
    return f"{int(s)//60}:{int(s)%60:02d}"

OUTPUT_DIR.mkdir(exist_ok=True)

records = merge_same_day_runs(records)

dates, actual, adjusted, hrs, run_types = [], [], [], [], []
print(f"{'Date':<12} {'Duration':>9} {'Pace':>8} {'HR':>6} {'Adj.Pace':>9}  {'Type':<7}")
print("-" * 58)
for r in records:
    d = datetime.strptime(r["date"], "%Y-%m-%d")
    ap = pace_to_sec(r["avg_pace"])
    adj = ap * (r["avg_hr"] / TARGET_HR)
    rtype = classify(r["duration_min"], r["avg_hr"])
    dates.append(d)
    actual.append(ap)
    adjusted.append(adj)
    hrs.append(r["avg_hr"])
    run_types.append(rtype)
    print(f"{r['date']:<12} {r['duration_min']:>7.1f}m {r['avg_pace']:>8} {r['avg_hr']:>5}bpm "
          f"{sec_to_pace(adj):>9}/km  {rtype:<7}")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(dates, adjusted, linewidth=2, color="#BBDEFB", zorder=2,
        label=f"HR adj. pace (@{TARGET_HR}bpm)")
ax.plot(dates, actual, linewidth=1, linestyle=":", color="#90A4AE", alpha=0.6,
        label="Actual pace", zorder=1)

MARKERS = {
    "Zone 2": ("o", "#1565C0"),
    "LSD":    ("*", "#2E7D32"),
    "Other":  ("D", "#F57C00"),
}
for rtype, (marker, color) in MARKERS.items():
    idx = [i for i, t in enumerate(run_types) if t == rtype]
    if idx:
        ax.scatter([dates[i] for i in idx], [adjusted[i] for i in idx],
                   color=color, s=140 if marker == "*" else 80,
                   marker=marker, zorder=4, label=rtype)

for d, adj, hr, rtype in zip(dates, adjusted, hrs, run_types):
    ax.annotate(f"{sec_to_pace(adj)}\n({hr}bpm)",
                xy=(d, adj), xytext=(0, 14), textcoords="offset points",
                ha="center", fontsize=7.5, color="#37474F")

y_vals = actual + adjusted
y_min = min(y_vals) - 30
y_max = max(y_vals) + 80
ax.set_ylim(y_max, y_min)

tick_step = 30
ticks = range(int(y_min // tick_step) * tick_step,
              int(y_max // tick_step + 1) * tick_step, tick_step)
ax.set_yticks(list(ticks))
ax.set_yticklabels([sec_to_pace(t) for t in ticks])

ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
fig.autofmt_xdate()

date_range = f"{dates[0].strftime('%b %d')} – {dates[-1].strftime('%b %d, %Y')}"
ax.set_title(f"Zone 2 Pace Trend — HR Adjusted (@{TARGET_HR}bpm)  ({date_range})",
             fontsize=13, fontweight="bold")
ax.set_ylabel("Pace (min/km)   ← faster")
ax.set_xlabel("Date")
ax.legend(loc="upper right", fontsize=8)
ax.grid(axis="y", linestyle="--", alpha=0.35)
ax.grid(axis="x", linestyle=":", alpha=0.2)

out = OUTPUT_DIR / "zone2_trend.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"\nChart saved: {out}")
plt.show()
