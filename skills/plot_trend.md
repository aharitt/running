# Skill: Plot Trend Chart

## Purpose

Generate a time-series chart showing the trend of adjusted pace over time, with actual pace shown for reference.

## Input

List of run records with both actual and adjusted pace:
```json
{"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126, "adj_pace": "10:19"}
```

## Chart Spec

- **X-axis:** Date (one tick per session)
- **Y-axis:** Pace in M:SS per km — **inverted** so faster pace appears at the top
- **Series 1 (primary):** Adjusted pace @125 bpm — solid line, filled markers
- **Series 2 (reference):** Actual pace — dashed line, lighter color
- **Annotations:** Label each data point with adjusted pace and actual HR
- **Title:** `Zone 2 Pace Trend — Adjusted to 125 bpm`
- **Y-axis label:** `Pace (min/km)  ← faster`

## Output

- Save chart as `../output/zone2_trend.png` at 150 dpi
- Print a summary table to console: `date | avg_pace | avg_hr | adj_pace`

## Implementation

Use `matplotlib`. See `../scripts/run_chart.py` for a working reference implementation.
