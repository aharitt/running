# Running Agents

Agents for analyzing personal running data from Apple Fitness screenshots.

## Agents

### Zone 2 Analyzer
Analyzes Zone 2 running sessions and tracks aerobic fitness improvement over time.

Each session's avg. pace is adjusted to a **125 bpm reference heart rate**, so sessions can be fairly compared regardless of daily HR variation. A downward trend in adjusted pace means improving aerobic efficiency.

**Skills:**
- `extract_run_data` — reads Apple Fitness screenshots via Claude vision to extract date, avg. pace, and avg. heart rate
- `calculate_adjusted_pace` — normalizes pace using `adjusted_pace = actual_pace × (actual_hr / 125)`
- `plot_trend` — generates a time-series chart of adjusted pace with actual pace shown for reference

## Structure

```
running/
├── agents/
│   └── zone2_agent.md              # Agent definition (orchestrates skills)
├── skills/
│   ├── extract_run_data.md         # Vision extraction from screenshots
│   ├── calculate_adjusted_pace.md  # 125 bpm pace normalization formula
│   └── plot_trend.md               # Trend chart specification
├── scripts/
│   ├── zone2_analyzer.py           # Claude vision extractor + chart (requires API key)
│   └── run_chart.py                # Standalone chart from pre-extracted data
├── data/                           # Apple Fitness PNG screenshots (local only, not tracked)
│   └── zone 2 records/
└── output/                         # Generated charts (local only, not tracked)
    └── zone2_trend.png
```

## Usage

```bash
cd scripts
pip install anthropic matplotlib
export ANTHROPIC_API_KEY=sk-...
python zone2_analyzer.py
```

The script reads all PNG screenshots from `data/zone 2 records/`, extracts workout data using Claude vision, calculates adjusted paces, and saves a trend chart to `output/zone2_trend.png`.
