"""Standalone chart generator using extracted Zone 2 data."""

from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

OUTPUT_DIR = Path(__file__).parent.parent / "output"
TARGET_HR = 125

records = [
    {"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126},
    {"date": "2025-05-11", "avg_pace": "9:58",  "avg_hr": 128},
    {"date": "2025-05-12", "avg_pace": "10:14", "avg_hr": 130},
    {"date": "2025-05-14", "avg_pace": "9:40",  "avg_hr": 130},
    {"date": "2025-05-16", "avg_pace": "8:53",  "avg_hr": 137},
    {"date": "2025-05-18", "avg_pace": "9:29",  "avg_hr": 129},
]

def pace_to_sec(s):
    m, sec = s.split(":")
    return int(m) * 60 + int(sec)

def sec_to_pace(s):
    return f"{int(s)//60}:{int(s)%60:02d}"

OUTPUT_DIR.mkdir(exist_ok=True)

dates, actual, adjusted, hrs = [], [], [], []
print(f"{'Date':<12} {'Pace':>8} {'HR':>6} {'Adj. Pace':>10}")
print("-" * 40)
for r in records:
    d = datetime.strptime(r["date"], "%Y-%m-%d")
    ap = pace_to_sec(r["avg_pace"])
    adj = ap * (r["avg_hr"] / TARGET_HR)
    dates.append(d)
    actual.append(ap)
    adjusted.append(adj)
    hrs.append(r["avg_hr"])
    print(f"{r['date']:<12} {r['avg_pace']:>8} {r['avg_hr']:>5}bpm {sec_to_pace(adj):>10}/km")

fig, ax1 = plt.subplots(figsize=(11, 5))

ax1.plot(dates, adjusted, marker="o", linewidth=2.5, color="#1565C0",
         label=f"Adjusted pace (@{TARGET_HR} bpm)", zorder=3)
ax1.plot(dates, actual,   marker="s", linewidth=1.5, linestyle="--", color="#90CAF9",
         alpha=0.8, label="Actual pace", zorder=2)

for d, adj, hr in zip(dates, adjusted, hrs):
    ax1.annotate(f"{sec_to_pace(adj)}\n({hr}bpm)",
                 xy=(d, adj), xytext=(0, 10), textcoords="offset points",
                 ha="center", fontsize=8, color="#1565C0")

y_vals = actual + adjusted
y_min = min(y_vals) - 30
y_max = max(y_vals) + 60
ax1.set_ylim(y_max, y_min)

tick_step = 30
ticks = range(int(y_min // tick_step) * tick_step,
              int(y_max // tick_step + 1) * tick_step, tick_step)
ax1.set_yticks(list(ticks))
ax1.set_yticklabels([sec_to_pace(t) for t in ticks])

ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax1.xaxis.set_major_locator(mdates.DayLocator())
fig.autofmt_xdate()

ax1.set_title(f"Zone 2 Pace Trend — Adjusted to {TARGET_HR} bpm", fontsize=14, fontweight="bold")
ax1.set_ylabel("Pace (min/km)   ← faster")
ax1.set_xlabel("Date")
ax1.legend(loc="upper right")
ax1.grid(axis="y", linestyle="--", alpha=0.35)
ax1.grid(axis="x", linestyle=":", alpha=0.2)

out = OUTPUT_DIR / "zone2_trend.png"
fig.tight_layout()
fig.savefig(out, dpi=150)
print(f"\nChart saved: {out}")
plt.show()
