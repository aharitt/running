# Running Agents

Agents for analyzing personal running data and generating race training plans from Apple Fitness screenshots.

## Agents

### Zone 2 Analyzer
Analyzes Zone 2 and LSD running sessions to track aerobic fitness improvement over time.

Each session's avg. pace is adjusted to a **125 bpm reference heart rate** for fair comparison. Sessions are classified as Zone 2 (HR 121–131 bpm, < 75 min) or LSD (≥ 75 min) and displayed with distinct markers on the trend chart.

**Skills:** `extract_run_data` → `classify_run_type` → `calculate_adjusted_pace` → `plot_trend` → `coaching_analysis`

---

### Training Plan Agent
Generates a personalized, periodized training plan from current fitness to race day.

**Races:**
| Race | Date | Goal |
|------|------|------|
| 10K | Sep 26, 2025 | Sub-60 min (6:00/km) |
| Phoenix Half Marathon | Dec 12, 2025 | Sub-2:30 (7:07/km) |

The plan covers 29 weeks across 8 phases: Base → Build → 10K Peak → Taper → Recovery → HM Base → HM Build → HM Taper.

**Skills:** `generate_training_plan`

---

## Structure

```
running/
├── agents/
│   ├── zone2_agent.md              # Zone 2 + LSD analysis agent
│   └── training_plan_agent.md      # Race training plan agent
├── skills/
│   ├── extract_run_data.md         # Vision extraction from screenshots
│   ├── classify_run_type.md        # Zone 2 vs LSD vs Other classification
│   ├── calculate_adjusted_pace.md  # 125 bpm pace normalization formula
│   ├── plot_trend.md               # Trend chart specification
│   ├── coaching_analysis.md        # Expert coaching interpretation
│   └── generate_training_plan.md   # Periodized plan generation
├── scripts/
│   ├── zone2_analyzer.py           # Claude vision extractor + chart (requires API key)
│   └── run_chart.py                # Standalone chart from pre-extracted data
├── data/                           # Apple Fitness PNG screenshots (local only)
│   └── zone 2 records/
└── output/                         # Generated outputs (local only)
    ├── zone2_trend.png
    ├── coaching_report.md
    └── training_plan.md
```

## Usage

```bash
cd scripts
pip install anthropic matplotlib
export ANTHROPIC_API_KEY=sk-...
python zone2_analyzer.py
```
