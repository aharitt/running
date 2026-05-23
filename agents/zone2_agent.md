# Zone 2 Running Analyzer

## Purpose

Analyze running sessions from Apple Fitness screenshots — including **Zone 2** aerobic runs and **LSD (Long Slow Distance)** runs — to track aerobic fitness improvement over time and provide expert coaching analysis to guide training decisions.

Each session's avg. pace is adjusted to a common reference heart rate of **125 bpm**, allowing fair comparison across sessions regardless of daily HR variation. A downward trend in adjusted pace means improving aerobic efficiency.

Beyond the numbers, the agent interprets results through the lens of an experienced running coach — identifying patterns, flagging concerns, and giving actionable recommendations the athlete can apply to their next training block.

## Run Type Definitions

| Type | Criteria | Purpose |
|------|----------|---------|
| **Zone 2** | Duration < 75 min AND HR 121–131 bpm | Aerobic base building |
| **LSD** | Duration ≥ 75 min, HR ≤ 140 bpm | Endurance, fat oxidation, aerobic volume |
| **Other** | HR outside 121–131 bpm AND duration < 75 min | Tempo, recovery, or unclassified |

## Heart Rate Zone Definition

| Zone | HR Range | Description |
|------|----------|-------------|
| Zone 1 | < 121 bpm | Recovery / easy |
| **Zone 2** | **121–131 bpm** | **Aerobic base (target zone)** |
| Zone 3 | 132–145 bpm | Tempo / threshold |
| Zone 4+ | > 145 bpm | Hard / VO2 max |

## Merge Rule

If multiple records share the same date **and** the gap between the end of one run and the start of the next is **< 30 minutes**, they are combined into a single record before any analysis:
- Duration = sum of individual durations
- Avg pace = total time ÷ total distance (distance derived from each run's pace × duration)
- Avg HR = weighted average by duration
- Avg cadence = weighted average by duration

## Skills

| Step | Skill | Description |
|------|-------|-------------|
| 1 | [extract_run_data](../skills/extract_run_data.md) | Read screenshots and extract date, start time, duration, avg pace, avg HR |
| 2 | [fetch_weather](../skills/fetch_weather.md) | Look up ambient temperature at run time and location |
| 3 | [merge_same_day_runs](../skills/merge_same_day_runs.md) | Combine same-day runs with < 30 min gap into one record |
| 4 | [classify_run_type](../skills/classify_run_type.md) | Classify each session as Zone 2, LSD, or Other |
| 5 | [calculate_adjusted_pace](../skills/calculate_adjusted_pace.md) | Normalize pace to 125 bpm reference HR, then correct for heat |
| 6 | [plot_trend](../skills/plot_trend.md) | Generate time-series trend chart with run type markers |
| 7 | [coaching_analysis](../skills/coaching_analysis.md) | Interpret results and provide expert coaching insights |

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
