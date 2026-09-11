"""IPL foreign umpire analysis."""

import csv
import matplotlib.pyplot as plt


def foreign_umpire_analysis():
    """Plot number of foreign IPL umpires by country."""

    umpires = set()

    with open("data/matches.csv", "r", newline="") as file:
        matches = csv.DictReader(file)

        for match in matches:
            for column in ["umpire1", "umpire2", "umpire3"]:
                umpire = match[column]

                if umpire:
                    umpires.add(umpire)

    umpire_country = {
        "CB Gaffaney": "New Zealand",
        "M Erasmus": "South Africa",
        "NJ Llong": "England",
        "Asad Rauf": "Pakistan",
        "MR Benson": "England",
        "Aleem Dar": "Pakistan",
        "SJ Davis": "Australia",
        "BF Bowden": "New Zealand",
        "IL Howell": "South Africa",
        "DJ Harper": "Australia",
        "RE Koertzen": "South Africa",
        "BR Doctrove": "West Indies",
        "BG Jerling": "South Africa",
        "HDPK Dharmasena": "Sri Lanka",
        "GAV Baxter": "New Zealand",
        "SJA Taufel": "Australia",
        "PR Reiffel": "Australia",
        "JD Cloete": "South Africa",
        "BNJ Oxenford": "Australia",
        "RK Illingworth": "England",
        "SD Fry": "Australia",
        "RB Tiffin": "Zimbabwe",
        "TH Wijewardene": "Sri Lanka",
        "AL Hill": "New Zealand",
        "RJ Tucker": "Australia"
    }

    country_count = {}

    for umpire in umpires:
        country = umpire_country.get(umpire)

        if country and country != "India":
            if country not in country_count:
                country_count[country] = 0

            country_count[country] += 1

    # Sort countries by number of umpires
    country_count = dict(
        sorted(
            country_count.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    print(country_count)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(country_count.keys(), country_count.values())

    plt.title("Number of Foreign IPL Umpires by Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Umpires")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


foreign_umpire_analysis()