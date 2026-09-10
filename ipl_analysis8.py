"""IPL data analysis project."""

import pandas as pd
import matplotlib.pyplot as plt


def top_10_economical_bowlers():
    """Plot top 10 economical bowlers in IPL 2015."""

    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")

    # Get match IDs for 2015
    matches_2015 = matches[matches["season"] == 2015]

    # Get deliveries from 2015
    deliveries_2015 = deliveries[
        deliveries["match_id"].isin(matches_2015["id"])
    ]

    # Runs actually conceded by the bowler
    deliveries_2015["bowler_runs"] = (
        deliveries_2015["total_runs"]
        - deliveries_2015["bye_runs"]
        - deliveries_2015["legbye_runs"]
    )

    # Count legal balls bowled by each bowler
    legal_balls = deliveries_2015[
        (deliveries_2015["wide_runs"] == 0)
        & (deliveries_2015["noball_runs"] == 0)
    ]

    balls_bowled = legal_balls.groupby("bowler").size()

    # Total runs conceded by each bowler
    runs_conceded = deliveries_2015.groupby(
        "bowler"
    )["bowler_runs"].sum()

    # Calculate economy rate
    economy = runs_conceded / (balls_bowled / 6)

    # Top 10 economical bowlers
    top_10 = economy.sort_values().head(10)

    print(top_10)

    # Plot bar chart
    top_10.plot(
        kind="bar",
        figsize=(12, 6)
    )

    plt.title("Top 10 Economical Bowlers in IPL 2015")
    plt.xlabel("Bowler")
    plt.ylabel("Economy Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


top_10_economical_bowlers()