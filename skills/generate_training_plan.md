# Skill: Generate Training Plan

## Purpose

Produce a periodized training plan from the athlete's current fitness baseline to their race goals, applying standard endurance coaching principles.

## Inputs

- Current fitness baseline (Zone 2 adjusted pace, LSD volume, weekly km)
- Race schedule: distances, dates, and time goals
- Today's date (plan start)

## Periodization Structure

Divide the full training window into phases based on standard 10K / half-marathon preparation:

### Phase Guide

| Phase | Focus | Key Sessions |
|-------|-------|--------------|
| **Base** | Aerobic volume, Zone 2 discipline | Zone 2 (60–75 min), LSD growing to 90–120 min |
| **Build** | Introduce quality, raise threshold | Tempo runs (Zone 3, 20–35 min), Zone 2, LSD |
| **Peak** | Race-specific intensity | Intervals at goal pace, tempo, reduced LSD |
| **Taper** | Freshness for race day | Volume cut 40–50%, short quality sessions |
| **Recovery** | Post-race rebuild | Zone 1–2 only, 1–2 weeks |

### Weekly Session Structure

**Rule: No back-to-back Zone 2 days.** Every Zone 2 or LSD session requires at least one rest day before it. The only accepted consecutive pair is Mon (easy Zone 2) → Tue (quality tempo/intervals): an easy prep day before a hard session is standard practice. Two Zone 2 days in a row without a rest day accumulate fatigue without quality stimulus.

This caps the maximum sustainable session count at **4 per week** (Base phase) or **4 per week** (Build/Peak with 1 quality session):

**Base phase (4 sessions):**

| Day | Session | Notes |
|-----|---------|-------|
| Mon | Zone 2 — 60 min | Controlled HR 121–131 bpm |
| Tue | Rest | |
| Wed | Zone 2 — 60–75 min | |
| Thu | Rest | |
| Fri | Zone 2 — 60–70 min | |
| Sat | Rest | |
| Sun | LSD — 90–120 min | HR ≤ 140 bpm |

**Build/Peak phase (4 sessions, 1 quality):**

| Day | Session | Notes |
|-----|---------|-------|
| Mon | Zone 2 — 60 min | Easy prep before quality |
| Tue | Quality (tempo or intervals) | Hard session |
| Wed | Rest | |
| Thu | Zone 2 — 60–65 min | |
| Fri | Rest | |
| Sat | Rest | |
| Sun | LSD — 110–120 min | HR ≤ 140 bpm |

## Pace Targets by Phase

Calculate from goal race pace, working backwards:

| Session Type | Pace Guideline |
|-------------|----------------|
| Zone 2 | ~125–135% of goal 10K pace |
| LSD | ~130–140% of goal 10K pace (very comfortable) |
| Tempo | ~105–108% of goal 10K pace |
| 10K Intervals | Goal 10K pace (6:00/km) |
| HM Tempo | Goal HM pace (7:07/km) |

## Progressive Overload Rules

- Increase weekly volume by no more than **10% per week**
- Every **4th week**: reduce volume by 20–30% (recovery week)
- LSD: increase by **10–15 min every 1–2 weeks**
- Never increase both volume and intensity in the same week

## Output Format

Produce the plan in the following structure:

```
## Training Plan: [Start Date] → [Race 2 Date]

### Phase Overview
| Phase | Weeks | Dates | Focus |
...

### Weekly Detail
#### Phase 1: Base Building (Weeks 1–N)
**Weekly Target:** X sessions / ~XX km / LSD: XX min

| Week | Mon | Wed | Fri | Sun (LSD) | Volume |
...

(Repeat for each phase)

### Race Week Protocols
#### 10K Race Week (Sep 22–26)
...
#### Half Marathon Race Week (Dec 8–12)
...
```

## Coaching Notes to Include

- Flag recovery weeks explicitly
- Note when new session types are introduced (first tempo, first interval)
- Remind athlete to prioritize HR over pace during Zone 2 and LSD
- For Phoenix HM in December: weather will be mild (~15–20°C) — no heat adjustment needed
