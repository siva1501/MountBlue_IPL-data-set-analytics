"""Find the top 10 batsmen for Royal Challengers Bangalore."""

import csv

from plot import data_plotting


RCB = "Royal Challengers Bangalore"


def top_rcb_batsman_by_runs(filepath: str, top_n: int = 10) -> list:
    """Calculate the top RCB batsmen based on total runs."""

    runs_by_batsman = {}

    # Read deliveries and calculate runs for each RCB batsman.
    with open(filepath, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):

            if row["batting_team"] != RCB:
                continue

            batsman = row["batsman"]
            runs = int(row["batsman_runs"])

            runs_by_batsman[batsman] = (
                runs_by_batsman.get(batsman, 0) + runs
            )

    # Sort batsmen by runs and select the top 10.
    top_batsmen = sorted(
        runs_by_batsman.items(),
        key=lambda item: item[1],
        reverse=True
    )[:top_n]

    return top_batsmen


result = top_rcb_batsman_by_runs("../data/deliveries.csv")

# Print the top 10 batsmen.
for batsman, total_runs in result:
    print(batsman, total_runs)

# Prepare data for the common plotting function.
batsmen = [batsman for batsman, _ in result]
runs = [total_runs for _, total_runs in result]

# Plot the result.
data_plotting(
    "Top 10 Batsmen for Royal Challengers Bangalore",
    batsmen,
    runs,
    "Batsmen",
    "Total Runs",
)