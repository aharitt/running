# Skill: Fetch Weather

## Purpose

Look up the ambient temperature at the time and location of each run, to feed into [[calculate_adjusted_pace]] for heat correction.

## Input

List of run records with date, start_time, and location:
```json
{"date": "2025-05-09", "start_time": "20:45", "location": "Glendale, AZ"}
```

## Method

Use historical weather data for the run location. Preferred sources (in order):

1. **Weather Underground** — `wunderground.com/history/daily/us/az/glendale` — hourly observations
2. **TimeAndDate** — `timeanddate.com/weather/usa/glendale-az/historic` — hourly history
3. **Open-Meteo API** (no key required) — `https://archive-api.open-meteo.com/v1/archive?latitude=33.54&longitude=-112.19&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&hourly=temperature_2m&timezone=America%2FPhoenix`

## Location Reference

| Location | Latitude | Longitude | Timezone |
|----------|----------|-----------|----------|
| Glendale, AZ | 33.54 | −112.19 | America/Phoenix (UTC−7, no DST) |

## Output

For each run record, add `temp_c`: the temperature in Celsius at the start of the run (nearest hour is sufficient).

```json
{"date": "2025-05-09", "start_time": "20:45", "temp_c": 31}
```

## Fallback — Glendale AZ Historical Estimates

If live lookup is unavailable, use these documented values for the May 2025 training block:

| Date | Start | Daily High | Run Temp (°C) | Source |
|------|-------|-----------|---------------|--------|
| May 9 | 20:45 | 38°C (100°F) | 31 | AccuWeather / search |
| May 11 | 06:52 | 37°C (99°F) | 23 | AccuWeather / search |
| May 12 | 20:54 | 36°C (97°F) | 30 | AccuWeather / search |
| May 14 | 20:28 | 27°C (81°F) | 20 | AccuWeather / search (cold front) |
| May 16 | 06:13 | 33°C (~91°F) | 22 | Estimated — post-front recovery |
| May 18 | 07:41 | 36°C (~96°F) | 25 | Estimated |
| May 20 | 07:44 | 37°C (~98°F) | 25 | Estimated |
| May 21 | 20:58 | 37°C (~99°F) | 30 | Estimated |
| May 23 | 07:00 | 40°C (~104°F) | 28 | Hot day confirmed by athlete |

> Run temperature is estimated from daily high using typical Phoenix diurnal pattern:
> - Morning runs (6–8 AM): daily_high − 13°C
> - Evening runs (8–10 PM): daily_high − 8°C

## Notes

- Temperature is measured at 2m above ground (standard weather station height)
- Wind and humidity also affect perceived effort but are not currently modelled
- Heat correction formula is in [[calculate_adjusted_pace]]
