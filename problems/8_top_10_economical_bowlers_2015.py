"""Top 10 economical bowlers in IPL 2015."""

import csv

from plot import data_plotting


def top_10_economical_bowlers(matches_file, deliveries_file):
    """Calculate the top 10 economical bowlers in 2015."""

    matches_2015 = set()

    # Get match IDs from 2015.
    with open(matches_file, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row["season"] == "2015":
                matches_2015.add(row["id"])

    bowlers = {}

    # Calculate runs and balls for each bowler.
    with open(deliveries_file, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            if row["match_id"] not in matches_2015:
                continue

            bowler = row["bowler"]
            runs = (
                int(row["total_runs"])
                - int(row["bye_runs"])
                - int(row["legbye_runs"])
            )

            if bowler not in bowlers:
                bowlers[bowler] = [0, 0]

            bowlers[bowler][0] += runs
            bowlers[bowler][1] += 1

    # Calculate economy rate.
    economy_rates = {
        bowler: runs / (balls / 6)
        for bowler, (runs, balls) in bowlers.items()
        if balls > 0
    }

    # Select the top 10 economical bowlers.
    top_10 = sorted(
        economy_rates.items(),
        key=lambda item: item[1]
    )[:10]

    return top_10


result = top_10_economical_bowlers(
    "../data/matches.csv",
    "../data/deliveries.csv",
)

# Print result.
for bowler, rate in result:
    print(bowler, round(rate, 2))

# Prepare data for plotting.
bowlers = [bowler for bowler, _ in result]
economy = [rate for _, rate in result]

# Plot result.
data_plotting(
    "Top 10 Economical Bowlers in IPL 2015",
    bowlers,
    economy,
    "Bowler",
    "Economy Rate",
)