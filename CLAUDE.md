# Running Agents

This directory contains agents for analyzing personal running data.

## Agents

| Agent | Spec | Purpose |
|-------|------|---------|
| Zone 2 Analyzer | `agents/zone2_agent.md` | Adjusted pace trend, run classification, coaching report |
| Training Plan | `agents/training_plan_agent.md` | Periodized plan from current fitness to race goals |
| Race Prep | `agents/race_prep_agent.md` | Race-day supplementals: shoes, nutrition, warm-up, form |

## Structure

```
Running/
├── CLAUDE.md
├── agents/
│   ├── zone2_agent.md              # Zone 2 + LSD analysis agent
│   └── training_plan_agent.md      # Race training plan agent
├── skills/
│   ├── extract_run_data.md         # Vision extraction from screenshots
│   ├── classify_run_type.md        # Zone 2 vs LSD vs Other classification
│   ├── calculate_adjusted_pace.md  # 125 bpm pace normalization formula
│   ├── plot_trend.md               # Trend chart specification
│   ├── coaching_analysis.md        # Expert coaching interpretation
│   ├── generate_training_plan.md   # Periodized plan generation
│   ├── analyze_running_profile.md  # Cadence, pace-HR, efficiency profile
│   └── recommend_race_supplementals.md  # Shoes, nutrition, warm-up, form cues
├── scripts/
│   ├── zone2_analyzer.py           # Claude vision extractor + chart
│   └── run_chart.py                # Standalone chart from extracted data
├── data/
│   └── zone 2 records/             # Apple Fitness PNG screenshots
└── output/
    ├── zone2_trend.png             # Generated chart
    ├── coaching_report.md          # Latest coaching analysis
    ├── training_plan.md            # Race training plan
    └── race_prep_report.md         # Race-day supplemental recommendations
```

## Data Source

- **App:** Apple Fitness (Workout Details screen)
- **Format:** PNG screenshots
- **Fields used:** Date, Avg. Pace (min/km), Avg. Heart Rate (bpm)

## Running an Agent

```bash
cd scripts
pip install anthropic matplotlib
export ANTHROPIC_API_KEY=sk-...
python zone2_analyzer.py
```
