# Zone 2 Running Analyzer

## Purpose

Analyze Zone 2 running sessions from Apple Fitness screenshots to track aerobic fitness improvement over time.

Each session's avg. pace is adjusted to a common reference heart rate of **125 bpm**, allowing fair comparison across sessions regardless of daily HR variation. A downward trend in adjusted pace means improving aerobic efficiency.

## Skills

| Step | Skill | Description |
|------|-------|-------------|
| 1 | [extract_run_data](../skills/extract_run_data.md) | Read screenshots and extract date, avg pace, avg HR |
| 2 | [calculate_adjusted_pace](../skills/calculate_adjusted_pace.md) | Normalize pace to 125 bpm reference HR |
| 3 | [plot_trend](../skills/plot_trend.md) | Generate time-series trend chart |

## Data Source

- **Location:** `../data/zone 2 records/`
- **Format:** PNG screenshots from the Apple Fitness app (Workout Details screen)

## Output

- Console table: `date | avg_pace | avg_hr | adj_pace`
- Chart: `../output/zone2_trend.png`

## Run

```bash
cd scripts
python zone2_analyzer.py
```

Requires: `anthropic`, `matplotlib`  
Set `ANTHROPIC_API_KEY` in environment or `.env` file.
