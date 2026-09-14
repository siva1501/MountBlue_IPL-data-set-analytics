"""Number of matches played per year in IPL."""

import csv

from plot import data_plotting


def matches_played_per_year(filepath):
    """Calculate number of matches played in each year."""

    matches = {}

    with open(filepath, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            season = row["season"]
            matches[season] = matches.get(season, 0) + 1

    return matches


result = matches_played_per_year("../data/matches.csv")

# Sort seasons and prepare data.
seasons = sorted(result)
counts = [result[season] for season in seasons]

# Print result.
for season in seasons:
    print(season, result[season])

# Plot result.
data_plotting(
    "Number of Matches Played per Year in IPL",
    seasons,
    counts,
    "Year",
    "Number of Matches",
)
