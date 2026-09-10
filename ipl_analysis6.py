"""IPL data analysis project."""

import pandas as pd
import matplotlib.pyplot as plt


def matches_won_by_team_per_year():
    """Plot number of matches won by each team per year."""

    matches = pd.read_csv("data/matches.csv")

    # Count matches won by each team in each season
    matches_won = matches.groupby(
        ["season", "winner"]
    ).size()

    # Convert into season x team format
    matches_won = matches_won.unstack(fill_value=0)

    print(matches_won)

    # Plot stacked bar chart
    matches_won.plot(
        kind="bar",
        stacked=True,
        figsize=(14, 7)
    )

    plt.title("Number of Matches Won by Each Team per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Matches Won")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


matches_won_by_team_per_year()