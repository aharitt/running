# Race Preparation Agent

## Purpose

Recommend race-day supplementals — footwear, nutrition, warm-up, and form cues — tailored to the athlete's current running profile and each race's specific demands.

Recommendations are grounded in observed training data (pace, HR, cadence, LSD distance) rather than generic advice. Each race gets its own recommendation set because a 10K and a half marathon impose different physiological demands and gear priorities.

## Races

| Race | Date | Distance | Goal |
|------|------|----------|------|
| 10K | Sep 26, 2025 | 10 km | Sub-60 min (6:00/km) |
| Phoenix Half Marathon | Dec 12, 2025 | 21.1 km | Sub-2:30 (7:07/km) |

## Skills

| Step | Skill | Description |
|------|-------|-------------|
| 1 | [analyze_running_profile](../skills/analyze_running_profile.md) | Derive running style and biomechanical profile from session data |
| 2 | [recommend_race_supplementals](../skills/recommend_race_supplementals.md) | Recommend footwear, nutrition, warm-up, and form cues per race |

## Inputs

- Session data from Zone 2 analysis: pace, HR, cadence, duration, distance
- Race goals and dates from `training_plan_agent.md`
- Current fitness baseline from `../output/coaching_report.md`

## Output

- Race preparation report: `../output/race_prep_report.md`
