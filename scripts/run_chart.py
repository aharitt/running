"""Standalone chart generator using extracted Zone 2 data."""

from datetime import datetime, timedelta
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches

OUTPUT_DIR = Path(__file__).parent.parent / "output"
TARGET_HR = 125

# All records sorted by date. Same-day runs get a small time offset for clarity.
records = [
    {"date": "2025-04-17", "avg_pace": "8:20",  "avg_hr": 144, "offset_h": 0},
    {"date": "2025-04-20", "avg_pace": "10:22", "avg_hr": 115, "offset_h": 0},
    {"date": "2025-04-20", "avg_pace": "8:48",  "avg_hr": 136, "offset_h": 8},
    {"date": "2025-04-22", "avg_pace": "9:50",  "avg_hr": 107, "offset_h": 0},
    {"date": "2025-04-22", "avg_pace": "8:25",  "avg_hr": 142, "offset_h": 8},
    {"date": "2025-04-25", "avg_pace": "8:41",  "avg_hr": 147, "offset_h": 0},
    {"date": "2025-04-29", "avg_pace": "8:58",  "avg_hr": 142, "offset_h": 0},
    {"date": "2025-04-30", "avg_pace": "9:17",  "avg_hr": 137, "offset_h": 0},
    {"date": "2025-05-02", "avg_pace": "7:54",  "avg_hr": 155, "offset_h": 0},
    {"date": "2025-05-04", "avg_pace": "8:01",  "avg_hr": 111, "offset_h": 0},
    {"date": "2025-05-04", "avg_pace": "9:15",  "avg_hr": 121, "offset_h": 8},
    {"date": "2025-05-06", "avg_pace": "7:29",  "avg_hr": 147, "offset_h": 0},
    {"date": "2025-05-07", "avg_pace": "7:44",  "avg_hr": 151, "offset_h": 0},
    {"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126, "offset_h": 0},
    {"date": "2025-05-11", "avg_pace": "9:58",  "avg_hr": 128, "offset_h": 0},
    {"date": "2025-05-12", "avg_pace": "10:14", "avg_hr": 130, "offset_h": 0},
    {"date": "2025-05-14", "avg_pace": "9:40",  "avg_hr": 130, "offset_h": 0},
    {"date": "2025-05-16", "avg_pace": "8:53",  "avg_hr": 137, "offset_h": 0},
    {"date": "2025-05-18", "avg_pace": "9:29",  "avg_hr": 129, "offset_h": 0},
]

def pace_to_sec(s):
    m, sec = s.split(":")
    return int(m) * 60 + int(sec)

def sec_to_pace(s):
    return f"{int(s)//60}:{int(s)%60:02d}"

def hr_color(hr):
    if hr < 120:   return "#81D4FA"  # Zone 1 — light blue
    if hr <= 140:  return "#1565C0"  # Zone 2 — blue
    if hr <= 160:  return "#F57C00"  # Zone 3/4 — orange
    return "#C62828"                 # Zone 5 — red

OUTPUT_DIR.mkdir(exist_ok=True)

dates, actual, adjusted, hrs, colors = [], [], [], [], []
print(f"{'Date':<13} {'Pace':>8} {'HR':>6} {'Adj. Pace':>10}  Zone")
print("-" * 50)

for r in records:
    d = datetime.strptime(r["date"], "%Y-%m-%d") + timedelta(hours=r["offset_h"])
    ap = pace_to_sec(r["avg_pace"])
    adj = ap * (r["avg_hr"] / TARGET_HR)
    zone = ("Z1" if r["avg_hr"] < 120 else
            "Z2" if r["avg_hr"] <= 140 else
            "Z3/4" if r["avg_hr"] <= 160 else "Z5")
    dates.append(d)
    actual.append(ap)
    adjusted.append(adj)
    hrs.append(r["avg_hr"])
    colors.append(hr_color(r["avg_hr"]))
    print(f"{r['date']:<13} {r['avg_pace']:>8} {r['avg_hr']:>5}bpm {sec_to_pace(adj):>10}/km  {zone}")

fig, ax = plt.subplots(figsize=(14, 6))

# Connecting line for adjusted pace
ax.plot(dates, adjusted, linewidth=1.2, color="#BBDEFB", zorder=2, alpha=0.6)

# Scatter with HR-based colors
ax.scatter(dates, adjusted, c=colors, s=70, zorder=4)

# Actual pace line
ax.plot(dates, actual, linewidth=1, linestyle="--", color="#CFD8DC", alpha=0.6, zorder=1)

# Annotate each point
for d, adj, hr in zip(dates, adjusted, hrs):
    ax.annotate(f"{sec_to_pace(adj)}\n{hr}bpm",
                xy=(d, adj), xytext=(0, 10), textcoords="offset points",
                ha="center", fontsize=7, color="#37474F")

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

ax.set_title(f"Zone 2 Pace Trend — Adjusted to {TARGET_HR} bpm  (Apr–May 2025)",
             fontsize=14, fontweight="bold")
ax.set_ylabel("Pace (min/km)   ← faster")
ax.set_xlabel("Date")
ax.grid(axis="y", linestyle="--", alpha=0.3)
ax.grid(axis="x", linestyle=":", alpha=0.2)

legend_items = [
    mpatches.Patch(color="#81D4FA", label="Zone 1 (<120 bpm)"),
    mpatches.Patch(color="#1565C0", label="Zone 2 (120–140 bpm)"),
    mpatches.Patch(color="#F57C00", label="Zone 3/4 (141–160 bpm)"),
    mpatches.Patch(color="#C62828", label="Zone 5 (>160 bpm)"),
    plt.Line2D([0], [0], linestyle="--", color="#CFD8DC", label="Actual pace"),
]
ax.legend(handles=legend_items, loc="upper right", fontsize=8)

out = OUTPUT_DIR / "zone2_trend.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"\nChart saved: {out}")
plt.show()
