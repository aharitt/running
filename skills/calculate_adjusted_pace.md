# Skill: Calculate Adjusted Pace

## Purpose

Normalize each run's avg. pace to a common reference heart rate (125 bpm) so sessions can be fairly compared regardless of daily HR variation.

## Input

List of run records:
```json
{"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126}
```

## Formula

```
adjusted_pace_sec = actual_pace_sec × (actual_hr / reference_hr)
```

- **reference_hr** = 125 bpm
- Convert pace string to total seconds before applying the formula
- Convert result back to M:SS for display

## Example

| Actual Pace | Actual HR | Adjusted Pace @125bpm |
|-------------|-----------|----------------------|
| 10:15 (615s) | 126 | 615 × (126/125) = 619.9s → 10:19 |
| 9:58 (598s)  | 128 | 598 × (128/125) = 612.4s → 10:12 |
| 8:53 (533s)  | 137 | 533 × (137/125) = 584.2s → 9:44  |

## Interpretation

- Adjusted pace **decreasing over time** → aerobic efficiency improving (running faster at the same HR)
- Adjusted pace **higher than actual** → HR was above 125 bpm during the run
- Adjusted pace **lower than actual** → HR was below 125 bpm during the run

## Output

Original records with an additional `adj_pace` field:
```json
{"date": "2025-05-09", "avg_pace": "10:15", "avg_hr": 126, "adj_pace": "10:19"}
```
