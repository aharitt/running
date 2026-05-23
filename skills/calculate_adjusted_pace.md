# Skill: Calculate Adjusted Pace

## Purpose

Normalize each run's avg. pace to a common reference heart rate (125 bpm) **and** a common reference temperature (15°C), so sessions can be fairly compared regardless of daily HR and weather variation.

## Input

List of run records including temperature at time of run:
```json
{"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126, "temp_c": 31}
```

Temperature is sourced from [[fetch_weather]] using the run's date, start time, and location.

## Step 1 — HR Adjustment

Normalize pace to 125 bpm reference heart rate:

```
hr_adj_pace_sec = actual_pace_sec × (actual_hr / 125)
```

## Step 2 — Heat Adjustment

Strip out the heat penalty above a 15°C baseline (~0.4% pace slowdown per °C):

```
heat_factor     = 1 + 0.004 × max(0, temp_c − 15)
heat_adj_pace_sec = hr_adj_pace_sec / heat_factor
```

- **reference_temp** = 15°C (comfortable running conditions)
- **heat_factor** = 1.0 at 15°C, 1.06 at 30°C, 1.10 at 40°C
- Result is the equivalent pace the athlete would have run in ideal 15°C conditions

## Example

| Pace | HR | Temp | HR-Adj | Heat Factor | Heat-Adj |
|------|----|------|--------|-------------|----------|
| 10:15 (615s) | 126 | 31°C | 619.9s → 10:19 | 1 + 0.004×16 = 1.064 | 619.9/1.064 = 582.6s → **9:43** |
| 9:58 (598s)  | 128 | 23°C | 612.4s → 10:12 | 1 + 0.004×8  = 1.032 | 612.4/1.032 = 593.4s → **9:53** |
| 8:53 (533s)  | 137 | 22°C | 584.2s → 9:44  | 1 + 0.004×7  = 1.028 | 584.2/1.028 = 568.3s → **9:28** |

## Interpretation

- **Heat-adj pace decreasing over time** → aerobic fitness genuinely improving
- **Large gap between HR-adj and heat-adj** → heat was a major factor that day; do not read HR-adj as a fitness regression
- If `temp_c` is unavailable, fall back to HR-adjustment only and flag the session as "no temp data"

## Output

Original records with both adjusted pace fields:
```json
{"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126, "temp_c": 31,
 "adj_pace": "10:19", "heat_adj_pace": "9:43"}
```
