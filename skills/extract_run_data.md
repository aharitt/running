# Skill: Extract Run Data

## Purpose

Read an Apple Fitness "Workout Details" screenshot and extract structured workout data using Claude vision.

## Input

- One or more PNG screenshot files from the Apple Fitness app (Workout Details screen)

## Instructions

For each image:
1. Read the image file
2. Identify the following fields from the screen:
   - **Date** — shown at the top (e.g. "Sat, May 9") → convert to YYYY-MM-DD, assume year 2025 if not shown
   - **Start time** — shown below the activity name (e.g. "8:45PM–9:45PM") → extract start only, normalize to 24h "HH:MM" (e.g. "20:45")
   - **Duration** — "Workout Time" field shown as H:MM:SS → convert to total minutes as a float (e.g. 1:30:37 → 90.6)
   - **Avg. Pace** — shown as M'SS"/KM → normalize to M:SS format (e.g. 10:15)
   - **Avg. Heart Rate** — shown as XXX BPM → extract as integer
3. Return a JSON record per image:
   ```json
   {"date": "2025-05-09", "start_time": "20:45", "duration_min": 60.1, "avg_pace": "10:15", "avg_hr": 126}
   ```

## Output

List of JSON records, one per image, sorted by date ascending.

## Notes

- If a field is not visible or unreadable, set its value to `null`
- Pace may appear as `10'15"/KM` or `10:15/km` — normalize to `M:SS`
- Heart rate is always a whole number
- Duration should be converted precisely: 1:30:37 = 90 + 37/60 ≈ 90.6 min
