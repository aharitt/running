# Skill: Coaching Analysis

## Purpose

Interpret Zone 2 training data through the lens of an experienced running coach. Go beyond raw numbers to identify patterns, flag concerns, and provide actionable recommendations for the next training block.

## Input

The full dataset produced by [[calculate_adjusted_pace]], including:
- Date, avg pace, avg HR, adjusted pace (@125 bpm) for each session
- HR zone classification per session (Z1–Z5)
- The trend chart produced by [[plot_trend]]

## Analysis Areas

### 1. Aerobic Fitness Trend
- Is the adjusted pace improving (decreasing) over time?
- How many weeks of consistent data exist? Is the sample size sufficient to draw conclusions?
- Estimate the rate of improvement (sec/km per week) if trend is clear

### 2. Zone Discipline
- What fraction of sessions are true Zone 2 (HR **121–131 bpm**)?
- Are there sessions where HR drifted above Zone 2 (> 131 bpm)? What does this suggest (heat, fatigue, terrain, effort)?
- Flag sessions with HR > 131 bpm as "not Zone 2" — note them separately and do not include them in the core aerobic trend

### 3. Training Consistency
- How many days between sessions on average?
- Are there gaps > 5 days? Note potential detraining risk
- Identify clusters of back-to-back hard efforts that may indicate under-recovery

### 4. Cardiac Drift / Decoupling
- If two sessions have similar pace but diverging HR, note positive or negative cardiac drift
- Sessions where HR was significantly higher than expected for the pace may indicate accumulated fatigue or environmental stress (heat, humidity)

### 5. Warmup / Short Run Patterns
- Short runs (< 20 min or < 3 km) often reflect warmups or cooldowns rather than full Zone 2 sessions
- Flag these separately — they are less useful for trend analysis but may indicate structured workout days

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
