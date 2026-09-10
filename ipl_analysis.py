"""IPL data analysis project."""

import pandas as pd
import matplotlib.pyplot as plt


def total_runs_by_team():
    """Calculate and plot total runs scored by each IPL team."""
    deliveries = pd.read_csv("data/deliveries.csv")

    team_runs = deliveries.groupby("batting_team")["total_runs"].sum()
    team_runs = team_runs.sort_values(ascending=False)

    print(team_runs)

    team_runs.plot(kind="bar", figsize=(12, 6))

    plt.title("Total Runs Scored by Each IPL Team")
    plt.xlabel("Team")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


total_runs_by_team()
