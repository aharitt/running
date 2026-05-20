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

records = [
    {"date": "2025-05-09", "duration_min": 60.1, "avg_pace": "10:15", "avg_hr": 126},
    {"date": "2025-05-11", "duration_min": 60.1, "avg_pace": "9:58",  "avg_hr": 128},
    {"date": "2025-05-12", "duration_min": 60.2, "avg_pace": "10:14", "avg_hr": 130},
    {"date": "2025-05-14", "duration_min": 60.1, "avg_pace": "9:40",  "avg_hr": 130},
    {"date": "2025-05-16", "duration_min": 90.6, "avg_pace": "8:53",  "avg_hr": 137},
    {"date": "2025-05-18", "duration_min": 60.1, "avg_pace": "9:29",  "avg_hr": 129},
    {"date": "2025-05-20", "duration_min": 64.3, "avg_pace": "9:20",  "avg_hr": 131},
]

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

dates, actual, adjusted, hrs, run_types = [], [], [], [], []
print(f"{'Date':<12} {'Duration':>9} {'Pace':>8} {'HR':>6} {'Adj. Pace':>10}  {'Type':<7}")
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
          f"{sec_to_pace(adj):>10}/km  {rtype:<7}")

fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(dates, adjusted, linewidth=2, color="#BBDEFB", zorder=2)
ax.plot(dates, actual, linewidth=1.5, linestyle="--", color="#CFD8DC", alpha=0.7,
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
                   color=color, s=120 if marker == "*" else 70,
                   marker=marker, zorder=4, label=rtype)

for d, adj, hr, rtype in zip(dates, adjusted, hrs, run_types):
    ax.annotate(f"{sec_to_pace(adj)}\n({hr}bpm)",
                xy=(d, adj), xytext=(0, 12), textcoords="offset points",
                ha="center", fontsize=8, color="#37474F")

y_vals = actual + adjusted
y_min = min(y_vals) - 30
y_max = max(y_vals) + 70
ax.set_ylim(y_max, y_min)

tick_step = 30
ticks = range(int(y_min // tick_step) * tick_step,
              int(y_max // tick_step + 1) * tick_step, tick_step)
ax.set_yticks(list(ticks))
ax.set_yticklabels([sec_to_pace(t) for t in ticks])

ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
fig.autofmt_xdate()

ax.set_title(f"Zone 2 Pace Trend — Adjusted to {TARGET_HR} bpm  (May 2025)",
             fontsize=14, fontweight="bold")
ax.set_ylabel("Pace (min/km)   ← faster")
ax.set_xlabel("Date")
ax.legend(loc="upper right")
ax.grid(axis="y", linestyle="--", alpha=0.35)
ax.grid(axis="x", linestyle=":", alpha=0.2)

out = OUTPUT_DIR / "zone2_trend.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"\nChart saved: {out}")
plt.show()
