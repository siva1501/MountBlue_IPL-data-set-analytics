"""IPL data analysis project."""

import pandas as pd
import matplotlib.pyplot as plt


def extra_runs_2016():
    """Plot extra runs conceded by each team in IPL 2016."""

    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")

    # Get match IDs for the 2016 season
    matches_2016 = matches[matches["season"] == 2016]

    # Keep only deliveries from 2016
    deliveries_2016 = deliveries[
        deliveries["match_id"].isin(matches_2016["id"])
    ]

    # Calculate extra runs conceded by each bowling team
    extra_runs = deliveries_2016.groupby(
        "bowling_team"
    )["extra_runs"].sum()

    # Sort from highest to lowest
    extra_runs = extra_runs.sort_values(ascending=False)

    print(extra_runs)

    # Plot bar chart
    extra_runs.plot(
        kind="bar",
        figsize=(10, 6)
    )

    plt.title("Extra Runs Conceded by Each Team in 2016")
    plt.xlabel("Team")
    plt.ylabel("Extra Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


extra_runs_2016()