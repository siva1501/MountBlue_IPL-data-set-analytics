"""Extra runs conceded per team in IPL 2016."""

import csv
import matplotlib.pyplot as plt


def extra_runs_conceded_2016():
    """Plot extra runs conceded by each team in 2016."""

    # Store match IDs for the 2016 season
    matches_2016 = set()

    with open("data/matches.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["season"] == "2016":
                matches_2016.add(row["id"])

    # Store extra runs for each bowling team
    extra_runs = {}

    with open("data/deliveries.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["match_id"] in matches_2016:
                team = row["bowling_team"]
                runs = int(row["extra_runs"])

                if team not in extra_runs:
                    extra_runs[team] = 0

                extra_runs[team] += runs

    # Sort teams by extra runs
    sorted_teams = sorted(
        extra_runs.items(),
        key=lambda item: item[1],
        reverse=True
    )

    teams = []
    runs = []

    for team, total in sorted_teams:
        teams.append(team)
        runs.append(total)

        print(team, total)

    # Plot bar chart
    plt.figure(figsize=(12, 6))

    plt.bar(teams, runs)

    plt.xlabel("Team")
    plt.ylabel("Extra Runs Conceded")
    plt.title("Extra Runs Conceded per Team in IPL 2016")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    extra_runs_conceded_2016()