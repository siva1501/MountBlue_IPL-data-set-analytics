"""Top 10 economical bowlers in IPL 2015."""

import csv
import matplotlib.pyplot as plt


def top_10_economical_bowlers():
    """Plot the top 10 economical bowlers in 2015."""

    # Find all match IDs from 2015
    matches_2015 = set()

    with open("data/matches.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["season"] == "2015":
                matches_2015.add(row["id"])

    # Store runs and balls for each bowler
    bowler_runs = {}
    bowler_balls = {}

    with open("data/deliveries.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["match_id"] not in matches_2015:
                continue

            bowler = row["bowler"]

            # Runs conceded by the bowler
            total_runs = int(row["total_runs"])

            # Do not count byes and leg-byes as bowler runs
            bye_runs = int(row["bye_runs"])
            legbye_runs = int(row["legbye_runs"])

            runs_conceded = total_runs - bye_runs - legbye_runs

            if bowler not in bowler_runs:
                bowler_runs[bowler] = 0
                bowler_balls[bowler] = 0

            bowler_runs[bowler] += runs_conceded

            # One delivery = one ball
            bowler_balls[bowler] += 1

    # Calculate economy rate
    economy_rates = {}

    for bowler in bowler_runs:
        runs = bowler_runs[bowler]
        balls = bowler_balls[bowler]

        if balls > 0:
            overs = balls / 6
            economy = runs / overs
            economy_rates[bowler] = economy

    # Sort by economy rate
    sorted_bowlers = sorted(
        economy_rates.items(),
        key=lambda item: item[1]
    )

    # Top 10 economical bowlers
    top_10 = sorted_bowlers[:10]

    bowlers = []
    economy = []

    for bowler, rate in top_10:
        bowlers.append(bowler)
        economy.append(rate)

        print(bowler, round(rate, 2))

    # Plot bar chart
    plt.figure(figsize=(12, 6))

    plt.bar(bowlers, economy)

    plt.xlabel("Bowler")
    plt.ylabel("Economy Rate")
    plt.title("Top 10 Economical Bowlers in IPL 2015")

    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    top_10_economical_bowlers()