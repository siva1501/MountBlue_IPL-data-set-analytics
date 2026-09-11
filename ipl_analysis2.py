"""IPL data analysis project."""

import csv
import matplotlib.pyplot as plt


def top_10_rcb_batsmen():
    """Calculate and plot the top 10 RCB batsmen by runs."""

    batsman_runs = {}

    with open("data/deliveries.csv", "r", newline="") as file:
        deliveries = csv.DictReader(file)

        for delivery in deliveries:
            if delivery["batting_team"] == "Royal Challengers Bangalore":
                batsman = delivery["batsman"]
                runs = int(delivery["batsman_runs"])

                if batsman not in batsman_runs:
                    batsman_runs[batsman] = 0

                batsman_runs[batsman] += runs

    # Sort batsmen by runs
    sorted_batsmen = sorted(
        batsman_runs.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Take top 10
    top_10 = sorted_batsmen[:10]

    print(top_10)

    batsmen = [item[0] for item in top_10]
    runs = [item[1] for item in top_10]

    # Plot
    plt.figure(figsize=(12, 6))
    plt.bar(batsmen, runs)

    plt.title("Top 10 Batsmen for Royal Challengers Bangalore")
    plt.xlabel("Batsman")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


top_10_rcb_batsmen()