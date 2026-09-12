"""Foreign umpire analysis."""

import csv
import matplotlib.pyplot as plt


def foreign_umpire_analysis():
    """Plot number of foreign IPL umpires by country."""

    # Umpire name -> country
    umpire_country = {
        "Asad Rauf": "Pakistan",
        "RE Koertzen": "South Africa",
        "MR Benson": "England",
        "SJ Davis": "Australia",
        "DJ Harper": "Australia",
        "BF Bowden": "New Zealand",
        "IL Howell": "South Africa",
        "BR Doctrove": "West Indies",
        "RB Tiffin": "Zimbabwe",
        "BG Jerling": "South Africa",
        "SJA Taufel": "Australia",
        "M Erasmus": "South Africa",
        "TH Wijewardene": "Sri Lanka",
        "HDPK Dharmasena": "Sri Lanka",
        "GAV Baxter": "Australia",
        "NJ Llong": "England",
        "CB Gaffaney": "New Zealand",

        # Indian umpires
        "SL Shastri": "India",
        "GA Pratapkumar": "India",
        "K Hariharan": "India",
        "AM Saheba": "India",
        "AV Jayaprakash": "India",
        "I Shivram": "India",
        "SD Ranade": "India",
        "SK Tarapore": "India",
        "S Asnani": "India",
        "SS Hazare": "India",
        "AY Dandekar": "India",
        "A Nand Kishore": "India",
        "Nitin Menon": "India",
        "CK Nandan": "India",
        "AK Chaudhary": "India",
        "C Shamshuddin": "India",
        "KN Ananthapadmanabhan": "India",
        "A Deshmukh": "India",
        "YC Barde": "India",
        "VK Sharma": "India",
        "S Ravi": "India",
    }

    # Store unique umpires
    umpires = set()

    with open(
        "data/matches.csv",
        "r",
        encoding="utf-8"
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Check umpire 1
            if row["umpire1"].strip():
                umpires.add(row["umpire1"].strip())

            # Check umpire 2
            if row["umpire2"].strip():
                umpires.add(row["umpire2"].strip())

            # Check umpire 3
            if row["umpire3"].strip():
                umpires.add(row["umpire3"].strip())

    # Count foreign umpires by country
    country_count = {}

    for umpire in umpires:
        if umpire in umpire_country:
            country = umpire_country[umpire]

            # Ignore Indian umpires
            if country != "India":
                if country not in country_count:
                    country_count[country] = 0

                country_count[country] += 1

    # Sort countries by number of umpires
    sorted_countries = sorted(
        country_count.items(),
        key=lambda item: item[1],
        reverse=True
    )

    countries = []
    counts = []

    for country, count in sorted_countries:
        countries.append(country)
        counts.append(count)

        print(country, count)

    # Plot
    plt.figure(figsize=(10, 6))

    plt.bar(countries, counts)

    plt.xlabel("Country")
    plt.ylabel("Number of Umpires")
    plt.title("Number of Foreign Umpires in IPL")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    foreign_umpire_analysis()