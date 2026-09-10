"""IPL foreign umpire analysis."""

import pandas as pd
import matplotlib.pyplot as plt


def foreign_umpire_analysis():
    """Plot number of foreign IPL umpires by country."""

    matches = pd.read_csv("data/matches.csv")

    # Get umpire names
    umpires = pd.concat([
        matches["umpire1"],
        matches["umpire2"],
        matches["umpire3"]
    ])

    # Remove empty values and duplicate names
    umpires = umpires.dropna().drop_duplicates()

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

    # Convert umpire names to countries
    countries = []

    for umpire in umpires:
        country = umpire_country.get(umpire)

        if country and country != "India":
            countries.append(country)

    # Count umpires by country
    country_count = pd.Series(countries).value_counts()

    print(country_count)

    # Plot
    country_count.plot(kind="bar", figsize=(10, 6))

    plt.title("Number of Foreign IPL Umpires by Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Umpires")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


foreign_umpire_analysis()