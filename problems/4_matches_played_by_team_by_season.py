"""Stacked chart of matches played by team by season."""

import csv
import matplotlib.pyplot as plt


def matches_played_by_team_per_season():
    """Plot matches played by each team in every season."""

    matches = {}

    with open("data/matches.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            season = row["season"]
            team1 = row["team1"]
            team2 = row["team2"]

            if season not in matches:
                matches[season] = {}

            # Count team1
            if team1 not in matches[season]:
                matches[season][team1] = 0

            matches[season][team1] += 1

            # Count team2
            if team2 not in matches[season]:
                matches[season][team2] = 0

            matches[season][team2] += 1

    # Get all seasons
    seasons = sorted(matches.keys())

    # Get all teams
    teams = set()

    for season in matches:
        for team in matches[season]:
            teams.add(team)

    teams = sorted(teams)

    # Create bottom values for stacking
    bottom = [0] * len(seasons)

    plt.figure(figsize=(14, 7))

    for team in teams:
        team_counts = []

        for season in seasons:
            count = matches[season].get(team, 0)
            team_counts.append(count)

        plt.bar(
            seasons,
            team_counts,
            bottom=bottom,
            label=team
        )

        # Update bottom for next team
        for i in range(len(bottom)):
            bottom[i] += team_counts[i]

    plt.xlabel("Season")
    plt.ylabel("Number of Matches Played")
    plt.title("Matches Played by Team per Season")

    plt.xticks(seasons, rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    matches_played_by_team_per_season()