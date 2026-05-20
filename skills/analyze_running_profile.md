# Skill: Analyze Running Profile

## Purpose

Derive the athlete's running style and biomechanical profile from available session data — cadence, pace, HR, and duration. This profile feeds into gear and supplemental recommendations.

## Input

Session records from [[extract_run_data]], including cadence where visible:
```json
{"date": "2025-05-16", "duration_min": 90.6, "avg_pace": "8:53", "avg_hr": 137, "avg_cadence": 165}
```

## Profile Dimensions

### 1. Cadence
Extract avg cadence from each session and compute overall average.

| Cadence | Profile | Implication |
|---------|---------|-------------|
| < 160 SPM | Low — overstriding likely | Longer ground contact, higher impact force per step |
| 160–170 SPM | Moderate | Acceptable; room to improve efficiency |
| 170–180 SPM | Good | Efficient turnover for recreational/competitive runners |
| > 180 SPM | Elite range | Minimal overstriding |

### 2. Pace-HR Relationship
- Compare training pace vs. goal race pace to estimate the speed increase required
- Large gap (> 2:00/km) between Zone 2 pace and goal race pace indicates the athlete will be running significantly harder on race day — gear stiffness and energy return matter more

### 3. Aerobic Efficiency Trend
- Use adjusted pace trend from [[calculate_adjusted_pace]] — improving trend = increasing fitness
- Rate of improvement informs how much speed gain is realistic by race day

### 4. Run Duration Profile
- Longest LSD distance = endurance ceiling today
- Compare to race distance to estimate relative difficulty

## Output

A running profile summary:
```
## Running Profile

- Avg cadence (training): XXX SPM → [Low / Moderate / Good]
- Goal race pace vs. current Zone 2: +X:XX/km gap
- Aerobic trend: improving / plateau / declining
- Longest run to date: XX km (race distance: XX km)
- Estimated readiness: [Early base / Building / Race-ready]
```
