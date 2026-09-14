"""Find the number of foreign IPL umpires by country."""

import csv

from plot import data_plotting


def foreign_umpire_analysis(matches_file, umpires_file):
    """Count unique foreign umpires by country."""

    umpire_country = {}

    # Read umpire country data.
    with open(umpires_file, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            umpire_country[row["umpire"]] = row["country"]

    # Find unique umpires from matches.
    umpires = set()

    with open(matches_file, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            for column in ("umpire1", "umpire2", "umpire3"):
                umpire = row[column].strip()

                if umpire:
                    umpires.add(umpire)

    # Count foreign umpires by country.
    country_count = {}

    for umpire in umpires:
        country = umpire_country.get(umpire)

        if country and country != "India":
            country_count[country] = country_count.get(country, 0) + 1

    return country_count


result = foreign_umpire_analysis(
    "../data/matches.csv",
    "../data/umpires.csv",
)

# Sort countries by number of umpires.
sorted_countries = sorted(
    result.items(),
    key=lambda item: item[1],
    reverse=True
)

# Print the result.
for country, count in sorted_countries:
    print(country, count)

# Prepare data for plotting.
countries = [country for country, _ in sorted_countries]
counts = [count for _, count in sorted_countries]

# Plot the result.
data_plotting(
    "Number of Foreign Umpires in IPL",
    countries,
    counts,
    "Country",
    "Number of Umpires",
)