"""IPL data analysis project."""
import csv
import matplotlib.pyplot as plt


def total_runs_by_team():
    """Calculate and plot total runs scored by each IPL team."""

    team_runs = {}
    with open("data/deliveries.csv", "r", newline="") as file:
        deliveries = csv.DictReader(file)

        for delivery in deliveries:
            team = delivery["batting_team"]
            runs = int(delivery["total_runs"])

            if team not in team_runs:
                team_runs[team] = 0

            team_runs[team] += runs

    team_runs = dict(
        sorted(
            team_runs.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    print(team_runs)

    plt.figure(figsize=(12, 6))
    plt.bar(team_runs.keys(), team_runs.values())

    plt.title("Total Runs Scored by Each IPL Team")
    plt.xlabel("Team")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


total_runs_by_team()