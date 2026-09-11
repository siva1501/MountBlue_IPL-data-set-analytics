"""IPL data analysis project."""

import csv
import matplotlib.pyplot as plt


def matches_played_by_team_by_season():
    """Plot stacked chart of matches played by team by season."""

    matches_played = {}

    with open("data/matches.csv", "r", newline="") as file:
        matches = csv.DictReader(file)

        for match in matches:
            season = match["season"]
            team1 = match["team1"]
            team2 = match["team2"]

            if season not in matches_played:
                matches_played[season] = {}

            if team1 not in matches_played[season]:
                matches_played[season][team1] = 0

            if team2 not in matches_played[season]:
                matches_played[season][team2] = 0

            matches_played[season][team1] += 1
            matches_played[season][team2] += 1

    print(matches_played)

    # Get all teams
    teams = set()

    for season in matches_played:
        teams.update(matches_played[season].keys())

    teams = sorted(teams)
    seasons = sorted(matches_played.keys())

    # Plot stacked bar chart
    bottom = [0] * len(seasons)

    for team in teams:
        values = []

        for season in seasons:
            values.append(matches_played[season].get(team, 0))

        plt.bar(seasons, values, bottom=bottom, label=team)

        bottom = [bottom[i] + values[i] for i in range(len(seasons))]

    plt.title("Matches Played by Team by Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


matches_played_by_team_by_season()
