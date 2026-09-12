"""Number of matches played per year in IPL."""

import csv
import matplotlib.pyplot as plt


def matches_played_per_year():
    """Plot number of IPL matches played in each year."""

    matches_per_year = {}

    with open("data/matches.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            season = row["season"]

            if season not in matches_per_year:
                matches_per_year[season] = 0

            matches_per_year[season] += 1

    # Sort seasons
    sorted_seasons = sorted(matches_per_year)

    seasons = []
    match_counts = []

    for season in sorted_seasons:
        seasons.append(season)
        match_counts.append(matches_per_year[season])

        print(season, matches_per_year[season])

    # Plot bar chart
    plt.figure(figsize=(12, 6))

    plt.bar(seasons, match_counts)

    plt.xlabel("Year")
    plt.ylabel("Number of Matches")
    plt.title("Number of Matches Played per Year in IPL")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    matches_played_per_year()