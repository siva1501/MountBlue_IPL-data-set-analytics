import pandas as pd
import matplotlib.pyplot as plt


def extra_runs_conceded_2016():
    """Plot extra runs conceded by each team in IPL 2016."""

    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")

    # Get match IDs played in 2016
    matches_2016 = matches[matches["season"] == 2016]

    # Keep only deliveries from 2016 matches
    deliveries_2016 = deliveries[
        deliveries["match_id"].isin(matches_2016["id"])
    ]

    # Calculate total extra runs conceded by each bowling team
    extra_runs = (
        deliveries_2016.groupby("bowling_team")["extra_runs"]
        .sum()
        .sort_values(ascending=False)
    )

    # Plot bar chart
    extra_runs.plot(kind="bar")

    plt.title("Extra Runs Conceded per Team in IPL 2016")
    plt.xlabel("Team")
    plt.ylabel("Extra Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    extra_runs_conceded_2016()