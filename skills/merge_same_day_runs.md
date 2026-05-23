# Skill: Merge Same-Day Runs

## Purpose

Combine multiple runs on the same date into a single record when they occur close together — e.g. two segments of the same continuous workout logged separately by the app.

## Input

A list of run records, each with:
```json
{"date": "2025-05-09", "start_time": "20:45", "duration_min": 60.1, "avg_pace": "10:15", "avg_hr": 126}
```

## Algorithm

1. Sort records by `date` ascending, then by `start_time` ascending.
2. Group records by `date`.
3. Within each date group, scan consecutive pairs and calculate the gap:
   ```
   end_time_of_A  = start_time_of_A + duration_min_of_A
   gap_min        = start_time_of_B − end_time_of_A
   ```
4. If `gap_min < 30`, merge A and B into one record:
   - **date**: same date
   - **start_time**: start_time of the first record (A)
   - **duration_min**: sum of all merged durations
   - **avg_pace**: total time ÷ total distance
     - `distance_km = duration_min / avg_pace_min_per_km` for each segment
     - `total_distance = sum(distances)`
     - `total_time_min = sum(duration_min)`
     - `merged_pace_sec = (total_time_min / total_distance) × 60`
   - **avg_hr**: weighted average by duration
     - `merged_hr = sum(avg_hr × duration_min) / total_duration_min`
   - **avg_cadence** (if present): weighted average by duration
5. Continue scanning the merged record against the next record in the group.
6. Records with `gap_min ≥ 30` (or in different date groups) remain separate.

## Output

A new list of records in the same format, with merged records replacing the originals. Sorted by date ascending.

## Notes

- If `start_time` is `null` for any record in a same-day group, treat all records in that group as non-mergeable and leave them separate.
- Pace arithmetic must use seconds (or decimal minutes) — never string manipulation.
- The merged record inherits the `run_type` classification from downstream skills (do not pre-classify before merging).
