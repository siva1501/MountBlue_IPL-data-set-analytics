"""Stacked chart of matches played by team by season."""

import csv

from plot import data_plotting


def matches_played_by_team_per_season(filepath: str) -> dict:
    """Calculate matches played by each team in every season."""

    matches = {}

    with open(filepath, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            season = row["season"]
            team1 = row["team1"]
            team2 = row["team2"]

            # Create season dictionary.
            matches.setdefault(season, {})

            # Count both teams for each match.
            matches[season][team1] = matches[season].get(team1, 0) + 1
            matches[season][team2] = matches[season].get(team2, 0) + 1

    return matches


result = matches_played_by_team_per_season("../data/matches.csv")

seasons = sorted(result)
teams = sorted({
    team
    for season in result.values()
    for team in season
})

# Print the result.
for season in seasons:
    print(f"\nSeason: {season}")

    for team in teams:
        print(team, result[season].get(team, 0))

# Prepare data for stacked plotting.
plot_data = {
    team: [result[season].get(team, 0) for season in seasons]
    for team in teams
}

# Plot the stacked chart.
data_plotting(
    "Matches Played by Team per Season",
    seasons,
    plot_data,
    "Season",
    "Number of Matches Played",
    stacked=True,
)