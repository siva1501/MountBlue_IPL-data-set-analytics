"""IPL data analysis project."""

import pandas as pd
import matplotlib.pyplot as plt


def matches_played_per_year():
    """Plot number of IPL matches played in each year."""

    matches = pd.read_csv("data/matches.csv")

    # Count matches for each season
    matches_per_year = matches["season"].value_counts().sort_index()

    print(matches_per_year)

    # Plot bar chart
    matches_per_year.plot(kind="bar", figsize=(12, 6))

    plt.title("Number of Matches Played Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Matches")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


matches_played_per_year()
