"""Total runs scored by each team."""

import csv
import matplotlib.pyplot as plt


def total_runs_by_team():
    """Calculate total runs scored by each team."""

    team_runs = {}

    with open("data/deliveries.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            team = row["batting_team"]
            runs = int(row["total_runs"])

            if team not in team_runs:
                team_runs[team] = 0

            team_runs[team] += runs

    # Sort teams by total runs
    sorted_teams = sorted(
        team_runs.items(),
        key=lambda item: item[1],
        reverse=True
    )

    teams = []
    runs = []

    for team, total in sorted_teams:
        teams.append(team)
        runs.append(total)
        print(team, total)

    # Bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(teams, runs)

    plt.xlabel("Teams")
    plt.ylabel("Total Runs")
    plt.title("Total Runs Scored by Each Team in IPL")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    total_runs_by_team()