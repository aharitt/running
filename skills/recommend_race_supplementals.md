# Skill: Recommend Race Supplementals

## Purpose

Produce race-specific recommendations for footwear, nutrition, warm-up protocol, and form cues — tailored to the athlete's running profile and each race's demands.

## Input

- Running profile from [[analyze_running_profile]]
- Race details: distance, date, goal pace, course conditions
- Training context: current weekly volume, phase in training plan

## Recommendation Areas

### 1. Race-Day Footwear

#### Carbon Plated Shoes
Carbon-plated race shoes provide energy return and propulsive assist via a stiff carbon fibre plate embedded in the midsole. They are most effective at faster paces where the plate can compress and rebound efficiently.

**Suitability criteria:**
- Goal pace ≤ 7:30/km → carbon plates provide measurable benefit
- Cadence ≥ 165 SPM on race day → plate rebound is fully utilized
- Use carbon shoes for race day only — not for training runs

**Evaluation by race:**

| Race | Goal Pace | Carbon Benefit | Notes |
|------|-----------|---------------|-------|
| 10K | 6:00/km | High | Ideal pace range for carbon plates |
| HM | 7:07/km | Moderate–High | Still beneficial; choose slightly more cushioned option |

**Recommended models (2025):**

For **10K (6:00/km)**:
| Shoe | Stack/Drop | Weight | Best For |
|------|-----------|--------|----------|
| Nike Vaporfly 3 | 40mm/8mm | ~190g | 5:30–7:00/km, high energy return |
| Adidas Adizero Adios Pro 3 | 39mm/6mm | ~195g | 5:30–7:00/km, stable at speed |
| Saucony Endorphin Pro 4 | 38mm/8mm | ~195g | Versatile, forgiving for first carbon race |

For **HM (7:07/km)**:
| Shoe | Stack/Drop | Weight | Best For |
|------|-----------|--------|----------|
| Saucony Endorphin Pro 4 | 38mm/8mm | ~195g | Best cushion/plate balance for longer races |
| Nike Vaporfly 3 | 40mm/8mm | ~190g | If legs are strong enough for 21 km in low-stack shoe |
| Hoka Rocket X 2 | 38mm/5mm | ~210g | More cushion, gentler on legs for HM distance |

**Break-in protocol:** Wear race shoes for 2–3 short runs (20–30 min) during Phase 3/Peak training before race day. Never debut carbon shoes on race day.

#### Daily Training Shoes (separate from race shoes)
All Zone 2 and LSD training should be done in a cushioned daily trainer — not carbon plates. Suggested categories:
- **Zone 2 / LSD:** Max-cushion trainer (e.g., Hoka Clifton, Brooks Ghost, ASICS Gel-Nimbus)
- **Tempo runs (Phase 2+):** Plated trainer or moderate stack (e.g., Saucony Endorphin Speed, Nike Pegasus Turbo)

---

### 2. Race Nutrition

#### 10K (sub-60 min)
- No mid-race gels needed for 60-minute effort
- **Pre-race:** Light meal 2–3 hours before (oats, banana, toast). Avoid high-fat or high-fibre foods
- **Race morning:** 200–300ml water + electrolytes 30 min before start
- **During:** Water at aid stations only if offered; 10K is short enough to run without fueling
- **Post-race:** Protein + carbs within 30 min (recovery meal)

#### Half Marathon (sub-2:30)
- **Pre-race:** Same as 10K but larger meal — add rice or sweet potato
- **During:** Take 1 energy gel at km 7 and km 14 (every ~50 min). Practice this in long runs during Phase 7
- **Hydration:** Drink ~150ml at every aid station (every 2–3 km at Phoenix Marathon)
- **Electrolytes:** Consider salt tabs or electrolyte drink if sweating heavily
- **Practice:** Run at least 2 LSD sessions using race-day nutrition protocol before Dec 12

---

### 3. Warm-Up Protocol

#### 10K Warm-Up (start 25 min before gun)
1. 10 min easy jog at Zone 1 pace (~10:30/km)
2. Dynamic stretches: leg swings, hip circles, high knees — 3 min
3. 4 × 100m strides gradually accelerating to race pace (6:00/km)
4. 2 min walk to start corral

#### Half Marathon Warm-Up (start 15 min before gun)
1. 8 min easy jog at Zone 1 pace
2. Dynamic stretches — 3 min
3. 2 × 100m strides at HM pace (7:07/km)
4. Walk to start

---

### 4. Cadence & Form Cues

Based on training cadence of 153–165 SPM, the following cues will improve efficiency at race pace:

- **Target race cadence:** 172–178 SPM at 6:00/km, 168–174 SPM at 7:07/km
- **Training drill:** Once per week during Phase 2+, run 5 min at normal pace, then 5 min focusing on quick, light footstrikes — count steps for 15 seconds, multiply by 4
- **Cue:** "Quick feet, quiet landing" — avoid heavy heel striking which wastes energy and increases injury risk with carbon plates
- **Arm swing:** Keep elbows at ~90°, drive arms backward (not across the body) to aid turnover

---

### 5. Race-Day Checklist

#### Both Races
- [ ] Race shoes broken in (2–3 short runs done)
- [ ] Race socks tested in training (no new socks on race day)
- [ ] Race bib pinned the night before
- [ ] GPS watch charged and race pace alert set
- [ ] Weather checked — adjust layers accordingly

#### HM Additional
- [ ] Gels pre-loaded in shorts pocket or race vest
- [ ] Body Glide / anti-chafe applied (thighs, underarms, nipples for long run)
- [ ] Arrive 60+ min before start for parking and warm-up time

## Output Format

```
## Race Preparation Report

### Running Profile Summary
...

### 10K (Sep 26) — Supplemental Recommendations
**Footwear:** ...
**Nutrition:** ...
**Warm-up:** ...
**Form focus:** ...

### Half Marathon (Dec 12) — Supplemental Recommendations
**Footwear:** ...
**Nutrition:** ...
**Warm-up:** ...
**Form focus:** ...

### Race-Day Checklists
...
```
