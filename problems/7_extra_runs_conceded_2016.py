"""Extra runs conceded per team in IPL 2016."""

import csv

from plot import data_plotting


def extra_runs_conceded_2016(matches_file, deliveries_file):
    """Calculate extra runs conceded by each team in 2016."""

    matches_2016 = set()

    # Get match IDs from the 2016 season.
    with open(matches_file, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row["season"] == "2016":
                matches_2016.add(row["id"])

    extra_runs = {}

    # Calculate extra runs for each bowling team.
    with open(deliveries_file, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row["match_id"] in matches_2016:
                team = row["bowling_team"]
                extra_runs[team] = (
                    extra_runs.get(team, 0) + int(row["extra_runs"])
                )

    return extra_runs


result = extra_runs_conceded_2016(
    "../data/matches.csv",
    "../data/deliveries.csv",
)

# Sort teams by extra runs.
sorted_teams = sorted(
    result.items(),
    key=lambda item: item[1],
    reverse=True
)

# Print result.
for team, runs in sorted_teams:
    print(team, runs)

# Prepare data for plotting.
teams = [team for team, _ in sorted_teams]
runs = [runs for _, runs in sorted_teams]

# Plot result.
data_plotting(
    "Extra Runs Conceded per Team in IPL 2016",
    teams,
    runs,
    "Team",
    "Extra Runs Conceded",
)