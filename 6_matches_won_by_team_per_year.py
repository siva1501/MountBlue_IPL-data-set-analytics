"""Number of matches won per team per year in IPL."""

import csv
import matplotlib.pyplot as plt


def matches_won_per_team_per_year():
    """Plot matches won by each team per season."""

    wins = {}

    with open("data/matches.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            season = row["season"]
            winner = row["winner"]

            # Ignore matches with no winner
            if winner == "":
                continue

            if season not in wins:
                wins[season] = {}

            if winner not in wins[season]:
                wins[season][winner] = 0

            wins[season][winner] += 1

    # Get all seasons
    seasons = sorted(wins.keys())

    # Get all teams
    teams = set()

    for season in wins:
        for team in wins[season]:
            teams.add(team)

    teams = sorted(teams)

    # Bottom position for stacked bars
    bottom = [0] * len(seasons)

    plt.figure(figsize=(14, 7))

    for team in teams:
        team_wins = []

        for season in seasons:
            count = wins[season].get(team, 0)
            team_wins.append(count)

        plt.bar(
            seasons,
            team_wins,
            bottom=bottom,
            label=team
        )

        # Update bottom
        for i in range(len(bottom)):
            bottom[i] += team_wins[i]

    plt.xlabel("Season")
    plt.ylabel("Number of Matches Won")
    plt.title("Number of Matches Won per Team per Year in IPL")

    plt.xticks(seasons, rotation=45)

    plt.legend(
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    matches_won_per_team_per_year()