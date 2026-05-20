# Skill: Coaching Analysis

## Purpose

Interpret Zone 2 training data through the lens of an experienced running coach. Go beyond raw numbers to identify patterns, flag concerns, and provide actionable recommendations for the next training block.

## Input

The full dataset produced by [[calculate_adjusted_pace]] and [[classify_run_type]], including:
- Date, duration, avg pace, avg HR, adjusted pace (@125 bpm), and `run_type` per session
- The trend chart produced by [[plot_trend]]

## Analysis Areas

### 1. Aerobic Fitness Trend
- Analyze Zone 2 and LSD sessions separately — they serve different training purposes
- For Zone 2: is adjusted pace improving (decreasing) over time? Estimate rate of improvement (sec/km per week)
- For LSD: is the athlete sustaining comfortable effort (HR staying controlled) over increasing distances?
- How many weeks of data exist? Is the sample size sufficient to draw conclusions?

### 2. Zone 2 Session Quality
- What fraction of sessions are true Zone 2 (HR 121–131 bpm, duration < 75 min)?
- Are there sessions where HR drifted above Zone 2 (> 131 bpm)? What does this suggest (heat, fatigue, terrain, effort)?
- Analyze only Zone 2 sessions for the adjusted pace trend — do not mix with LSD

### 3. LSD Session Quality
- How often are LSD runs appearing? Ideal cadence is once per week for aerobic base building
- Is HR controlled during LSD (ideally staying below 140 bpm)? HR creeping high on long runs indicates the pace is too aggressive
- Is distance/duration increasing progressively over time?
- LSD runs train fat oxidation and mitochondrial density — flag if they are absent or infrequent

### 4. Training Balance (80/20 Rule)
- What is the ratio of easy (Zone 1–2 + LSD) to hard (Zone 3+) sessions?
- Ideal: ~80% of sessions at easy effort (Zone 2 + LSD), ~20% at Zone 3+
- Flag imbalance in either direction

### 5. Training Consistency
- How many days between sessions on average?
- Are there gaps > 5 days? Note potential detraining risk
- Identify back-to-back sessions without adequate recovery

### 6. Cardiac Drift / Decoupling
- For LSD sessions especially: if HR rises significantly in the second half of the run, it indicates cardiac drift — the aerobic system is not yet efficient enough for the duration
- For Zone 2: sessions where HR was higher than expected for the pace indicate accumulated fatigue or environmental stress

## Output Format

Produce a written coaching report with the following sections:

```
## Coaching Report

### Summary
One paragraph: overall fitness trajectory and what the data says at a high level.

### What's Working
Bullet points of positive signals in the data.

### Concerns
Bullet points of patterns that warrant attention (not alarm — constructive tone).

### Recommendations
3–5 specific, actionable recommendations for the next 2–4 weeks of training.
Tie each recommendation directly to an observation in the data.

### Next Milestone
One measurable goal to aim for (e.g. "Run 10 km at < 9:30/km adjusted pace within 4 weeks").
```

## Coaching Principles to Apply

- **80/20 rule:** ~80% of weekly volume should be Zone 1–2; flag if too much time is spent in Zone 3+
- **Progressive overload:** small, consistent improvements are better than sudden jumps
- **Recovery is training:** gaps and easy days are features, not failures
- **HR is a proxy for effort:** high HR on a slow day = accumulated fatigue or external stress, not fitness loss
- **Consistency beats intensity:** for aerobic base building, regularity matters more than any single hard session
