"""
Zone 2 Running Analyzer
Reads Apple Fitness screenshots, extracts pace/HR via Claude vision,
and plots adjusted pace trend at 125 bpm reference heart rate.
"""

import base64
import json
import os
import re
from pathlib import Path

import anthropic
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

DATA_DIR = Path(__file__).parent.parent / "data" / "zone 2 records"
OUTPUT_DIR = Path(__file__).parent.parent / "output"
TARGET_HR = 125


def encode_image(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def extract_run_data(client: anthropic.Anthropic, image_path: Path) -> dict | None:
    """Use Claude vision to extract date, avg pace, avg HR from a screenshot."""
    image_data = encode_image(image_path)

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": (
                            "Extract the following from this Apple Fitness workout screenshot "
                            "and return ONLY a JSON object with no extra text:\n"
                            '{"date": "YYYY-MM-DD", "avg_pace": "M:SS", "avg_hr": 000}\n\n'
                            "- date: the workout date shown at the top (assume year 2025 if not shown)\n"
                            "- avg_pace: Avg. Pace in min:sec per km (e.g. 10:15)\n"
                            "- avg_hr: Avg. Heart Rate as an integer bpm"
                        ),
                    },
                ],
            }
        ],
    )

    raw = response.content[0].text.strip()
    # Strip markdown code fences if present
    raw = re.sub(r"^```[a-z]*\n?", "", raw).rstrip("`").strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        print(f"  [warn] Could not parse response for {image_path.name}: {raw}")
        return None


def pace_to_seconds(pace_str: str) -> float:
    """Convert 'M:SS' or 'M'SS"' string to total seconds."""
    pace_str = pace_str.replace('"', "").replace("'", ":").replace("’", ":")
    parts = pace_str.split(":")
    return int(parts[0]) * 60 + int(parts[1])


def seconds_to_pace(seconds: float) -> str:
    """Convert seconds to 'M:SS' string."""
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m}:{s:02d}"


def adjusted_pace(actual_pace_sec: float, actual_hr: int) -> float:
    """Scale pace to TARGET_HR using linear HR-pace relationship."""
    return actual_pace_sec * (actual_hr / TARGET_HR)


def main():
    client = anthropic.Anthropic()
    OUTPUT_DIR.mkdir(exist_ok=True)

    image_files = sorted(DATA_DIR.glob("*.PNG")) + sorted(DATA_DIR.glob("*.png"))
    if not image_files:
        print(f"No PNG files found in {DATA_DIR}")
        return

    records = []
    print(f"{'File':<15} {'Date':<12} {'Pace':>8} {'HR':>6} {'Adj. Pace':>10}")
    print("-" * 55)

    for img in image_files:
        data = extract_run_data(client, img)
        if data is None:
            continue

        pace_sec = pace_to_seconds(data["avg_pace"])
        adj_sec = adjusted_pace(pace_sec, data["avg_hr"])
        date = datetime.strptime(data["date"], "%Y-%m-%d")

        records.append(
            {
                "date": date,
                "avg_pace_sec": pace_sec,
                "avg_hr": data["avg_hr"],
                "adj_pace_sec": adj_sec,
            }
        )

        print(
            f"{img.name:<15} {data['date']:<12} "
            f"{seconds_to_pace(pace_sec):>8} "
            f"{data['avg_hr']:>5}bpm "
            f"{seconds_to_pace(adj_sec):>10}/km"
        )

    if not records:
        print("No records extracted.")
        return

    records.sort(key=lambda r: r["date"])

    # --- Chart ---
    dates = [r["date"] for r in records]
    adj_paces = [r["adj_pace_sec"] for r in records]
    actual_paces = [r["avg_pace_sec"] for r in records]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, adj_paces, marker="o", linewidth=2, label=f"Adjusted pace (@{TARGET_HR} bpm)", color="#2196F3")
    ax.plot(dates, actual_paces, marker="s", linewidth=1.5, linestyle="--", label="Actual pace", color="#90CAF9", alpha=0.7)

    # Y-axis: display as M:SS, lower = better (invert axis)
    y_min = min(adj_paces + actual_paces) - 15
    y_max = max(adj_paces + actual_paces) + 15
    ax.set_ylim(y_max, y_min)  # inverted: faster pace at top
    y_ticks = range(int(y_min // 30) * 30, int(y_max // 30 + 1) * 30, 30)
    ax.set_yticks(list(y_ticks))
    ax.set_yticklabels([seconds_to_pace(t) for t in y_ticks])

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    fig.autofmt_xdate()

    ax.set_title(f"Zone 2 Pace Trend (adjusted to {TARGET_HR} bpm)", fontsize=14, fontweight="bold")
    ax.set_ylabel("Pace (min/km)  ← faster")
    ax.set_xlabel("Date")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    out_path = OUTPUT_DIR / "zone2_trend.png"
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    print(f"\nChart saved: {out_path}")
    plt.show()


if __name__ == "__main__":
    main()
