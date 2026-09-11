"""IPL data analysis project."""

import csv
import matplotlib.pyplot as plt


def matches_played_per_year():
    """Plot number of IPL matches played in each year."""

    matches_per_year = {}

    with open("data/matches.csv", "r", newline="") as file:
        matches = csv.DictReader(file)

        for match in matches:
            season = match["season"]

            if season not in matches_per_year:
                matches_per_year[season] = 0

            matches_per_year[season] += 1

    # Sort years
    matches_per_year = dict(sorted(matches_per_year.items()))

    print(matches_per_year)

    # Plot bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(
        matches_per_year.keys(),
        matches_per_year.values()
    )

    plt.title("Number of Matches Played Per Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Matches")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


matches_played_per_year()
