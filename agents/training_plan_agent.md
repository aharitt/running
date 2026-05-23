# Training Plan Agent

## Purpose

Generate a personalized, periodized training plan from today through the athlete's next races, grounded in current fitness data from the Zone 2 analysis.

The plan bridges where the athlete is now (aerobic base) to where they need to be on race day — structured in phases with clear weekly session targets, progressive overload, and appropriate tapers.

## Race Goals

| Race | Date | Distance | Goal (Target) | A Goal | C Goal |
|------|------|----------|---------------|--------|--------|
| 10K | Sep 26, 2025 | 10 km | Sub-57:30 (5:45/km) | Sub-55:00 (5:30/km) | Sub-60:00 (6:00/km) |
| Phoenix Half Marathon | Dec 12, 2025 | 21.1 km | Sub-2:20 (6:38/km) | Sub-2:15 (6:23/km) | Sub-2:30 (7:07/km) |

> Training plans are generated to the **Target** level. A Goal is achievable if training goes exceptionally well. C Goal is the minimum acceptable outcome.

## Fitness Baseline (as of May 20, 2025)

Derived from Zone 2 analysis output (`../output/coaching_report.md`):

- **Zone 2 adjusted pace:** ~9:46/km at 125 bpm
- **LSD:** 91 min / 10.2 km at 8:53/km (HR 137 bpm)
- **Weekly volume:** ~30 km/week over 4 sessions
- **HR Zone 2:** 121–131 bpm

## Skills

| Step | Skill | Description |
|------|-------|-------------|
| 1 | [generate_training_plan](../skills/generate_training_plan.md) | Build periodized phases from current fitness to race goals |

## Output

- Training plan: `../output/training_plan.md`

## Run

Open `../output/coaching_report.md` for current fitness context, then apply the `generate_training_plan` skill to produce the plan.
