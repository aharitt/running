"""Standalone chart generator using extracted Zone 2 data."""

from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

OUTPUT_DIR = Path(__file__).parent.parent / "output"
TARGET_HR = 125
ZONE2_MIN = 121
ZONE2_MAX = 131

records = [
    {"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126},
    {"date": "2025-05-11", "avg_pace": "9:58",  "avg_hr": 128},
    {"date": "2025-05-12", "avg_pace": "10:14", "avg_hr": 130},
    {"date": "2025-05-14", "avg_pace": "9:40",  "avg_hr": 130},
    {"date": "2025-05-16", "avg_pace": "8:53",  "avg_hr": 137},
    {"date": "2025-05-18", "avg_pace": "9:29",  "avg_hr": 129},
    {"date": "2025-05-20", "avg_pace": "9:20",  "avg_hr": 131},
]

def pace_to_sec(s):
    m, sec = s.split(":")
    return int(m) * 60 + int(sec)

def sec_to_pace(s):
    return f"{int(s)//60}:{int(s)%60:02d}"

OUTPUT_DIR.mkdir(exist_ok=True)

dates, actual, adjusted, hrs, in_z2 = [], [], [], [], []
print(f"{'Date':<12} {'Pace':>8} {'HR':>6} {'Adj. Pace':>10}  {'Zone':>5}")
print("-" * 48)
for r in records:
    d = datetime.strptime(r["date"], "%Y-%m-%d")
    ap = pace_to_sec(r["avg_pace"])
    adj = ap * (r["avg_hr"] / TARGET_HR)
    z2 = ZONE2_MIN <= r["avg_hr"] <= ZONE2_MAX
    dates.append(d)
    actual.append(ap)
    adjusted.append(adj)
    hrs.append(r["avg_hr"])
    in_z2.append(z2)
    zone_label = "Z2" if z2 else "!Z2"
    print(f"{r['date']:<12} {r['avg_pace']:>8} {r['avg_hr']:>5}bpm {sec_to_pace(adj):>10}/km  {zone_label:>5}")

fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(dates, adjusted, linewidth=2, color="#BBDEFB", zorder=2)
ax.plot(dates, actual, linewidth=1.5, linestyle="--", color="#CFD8DC", alpha=0.7,
        label="Actual pace", zorder=1)

# Z2 and non-Z2 markers plotted separately for legend
z2_dates  = [d for d, z in zip(dates, in_z2) if z]
z2_adj    = [a for a, z in zip(adjusted, in_z2) if z]
nz2_dates = [d for d, z in zip(dates, in_z2) if not z]
nz2_adj   = [a for a, z in zip(adjusted, in_z2) if not z]

ax.scatter(z2_dates,  z2_adj,  color="#1565C0", s=70, zorder=4, label=f"Zone 2 ({ZONE2_MIN}–{ZONE2_MAX} bpm)")
ax.scatter(nz2_dates, nz2_adj, color="#F57C00", s=70, zorder=4, marker="D", label=f"Outside Zone 2 (>{ZONE2_MAX} bpm)")

for d, adj, hr in zip(dates, adjusted, hrs):
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
