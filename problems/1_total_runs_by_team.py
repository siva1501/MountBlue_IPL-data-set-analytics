"""Calculate total runs scored by each team."""

import csv

from plot import data_plotting


def to_int(value: str, default: int = 0) -> int:
    """Convert a value to integer safely."""
    try:
        return int((value or "").strip())
    except ValueError:
        return default


def calculate_total_runs_by_team(filepath: str) -> dict[str, int]:
    """Calculate total runs scored by each team."""

    team_runs = {}

    # Read deliveries and calculate runs for each team.
    with open(filepath, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            team = (row.get("batting_team") or "").strip()

            if not team:
                continue

            runs = to_int(row.get("total_runs"))
            team_runs[team] = team_runs.get(team, 0) + runs

    return team_runs


result = calculate_total_runs_by_team("../data/deliveries.csv")

# Sort teams by total runs.
sorted_teams = sorted(result.items(), key=lambda item: item[1], reverse=True)

# Print the result.
for team, runs in sorted_teams:
    print(team, runs)

teams, runs = zip(*sorted_teams)

# Plot the result using the common plotting module.
data_plotting(
    "Total Runs Scored by Each Team in IPL",
    teams,
    runs,
    "Teams",
    "Total Runs",
)