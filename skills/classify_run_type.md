# Skill: Classify Run Type

## Purpose

Label each session as **Zone 2**, **LSD**, or **Other** based on duration and heart rate, so downstream skills and charts can handle each type appropriately.

## Input

Records from [[extract_run_data]], each containing `duration_min` and `avg_hr`:
```json
{"date": "2025-05-16", "duration_min": 90.6, "avg_pace": "8:53", "avg_hr": 137}
```

## Classification Rules

| Run Type | Rule | Rationale |
|----------|------|-----------|
| **LSD** | `duration_min >= 75` | Duration is the defining trait of long slow distance — regardless of HR |
| **Zone 2** | `duration_min < 75` AND `121 <= avg_hr <= 131` | Short-to-medium aerobic base session at controlled HR |
| **Other** | Everything else | Recovery (HR < 121), tempo (HR > 131, short), or unclassified |

> LSD takes priority over HR zone. A 90-minute run at HR 137 is LSD, not Zone 3.

## Output

Original records with an added `run_type` field:
```json
{"date": "2025-05-09", "duration_min": 60.1, "avg_pace": "10:15", "avg_hr": 126, "run_type": "Zone 2"}
{"date": "2025-05-16", "duration_min": 90.6, "avg_pace": "8:53",  "avg_hr": 137, "run_type": "LSD"}
```

## Chart Marker Convention

| Run Type | Marker | Color |
|----------|--------|-------|
| Zone 2 | Circle (●) | Blue `#1565C0` |
| LSD | Star (★) | Green `#2E7D32` |
| Other | Diamond (◆) | Orange `#F57C00` |
