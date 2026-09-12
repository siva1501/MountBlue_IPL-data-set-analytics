"""Main entry point for IPL data analysis project."""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DELIVERIES_FILE = DATA_DIR / "deliveries.csv"
MATCHES_FILE = DATA_DIR / "matches.csv"


class Main:
    """Run the IPL analysis dashboard in CLI mode."""

    def user_ui(self) -> None:
        """Display menu and run selected analysis."""

        print("=" * 52)
        print("IPL ANALYSIS DASHBOARD : 2008 - 2017".center(52, "="))
        print(" Range: 2008–2017 ".center(52, " "))
        print("=" * 52)

        while True:
            self.show_menu()

            try:
                option = int(
                    input("Enter your choice [0-9]: ").strip()
                )
            except ValueError:
                print("INVALID input. Try again.")
                continue

            print()

            match option:
                case 0:
                    print("Exiting. Come soon..")
                    break

                case 1:
                    self.total_runs_by_team()

                case 2:
                    self.top_10_rcb_batsmen()

                case 3:
                    self.foreign_umpire_analysis()

                case 4:
                    self.matches_played_by_team_per_season()

                case 5:
                    self.matches_played_per_year()

                case 6:
                    self.matches_played_per_year_program6()

                case 7:
                    self.extra_runs_conceded_2016()

                case 8:
                    self.top_10_economical_bowlers()

                case 9:
                    self.run_all_programs()

                case _:
                    print(
                        "Invalid choice. "
                        "Please select between 0 and 9."
                    )

    def show_menu(self) -> None:
        """Display the menu options."""

        print()
        print("   0) Enter 0 to EXIT")
        print("   1) Total runs scored by each team")
        print("   2) Top 10 RCB batsmen by total runs")
        print("   3) Distinct Foreign Umpires by Country")
        print("   4) Matches played by team per season")
        print("   5) Number of matches played per year")
        print("   6) Number of matches played per year - Program 6")
        print("   7) Extra runs conceded per team in 2016")
        print("   8) Top 10 economical bowlers in 2015")
        print("   9) Run ALL programs")
        print()

    def total_runs_by_team(self) -> None:
        """Program 1: Total runs scored by each team."""

        team_runs = {}

        with open(
            DELIVERIES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                team = row["batting_team"]
                runs = int(row["total_runs"])

                if team not in team_runs:
                    team_runs[team] = 0

                team_runs[team] += runs

        sorted_teams = sorted(
            team_runs.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        teams = []
        runs = []

        print("\nProgram 1 - Total Runs by Team")

        for team, total in sorted_teams:
            teams.append(team)
            runs.append(total)
            print(team, total)

        plt.figure(figsize=(12, 6))
        plt.bar(teams, runs)
        plt.xlabel("Teams")
        plt.ylabel("Total Runs")
        plt.title("Total Runs Scored by Each Team in IPL")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def top_10_rcb_batsmen(self) -> None:
        """Program 2: Top 10 RCB batsmen."""

        batsman_runs = {}

        with open(
            DELIVERIES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["batting_team"] == (
                    "Royal Challengers Bangalore"
                ):
                    batsman = row["batsman"]
                    runs = int(row["batsman_runs"])

                    if batsman not in batsman_runs:
                        batsman_runs[batsman] = 0

                    batsman_runs[batsman] += runs

        sorted_batsmen = sorted(
            batsman_runs.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        top_10 = sorted_batsmen[:10]

        batsmen = []
        runs = []

        print("\nProgram 2 - Top 10 RCB Batsmen")

        for batsman, total_runs in top_10:
            batsmen.append(batsman)
            runs.append(total_runs)
            print(batsman, total_runs)

        plt.figure(figsize=(12, 6))
        plt.bar(batsmen, runs)
        plt.xlabel("Batsmen")
        plt.ylabel("Total Runs")
        plt.title(
            "Top 10 Batsmen for "
            "Royal Challengers Bangalore"
        )
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def foreign_umpire_analysis(self) -> None:
        """Program 3: Foreign umpires by country."""

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

        umpires = set()

        with open(
            MATCHES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["umpire1"].strip():
                    umpires.add(row["umpire1"].strip())

                if row["umpire2"].strip():
                    umpires.add(row["umpire2"].strip())

                if row["umpire3"].strip():
                    umpires.add(row["umpire3"].strip())

        country_count = {}

        for umpire in umpires:
            if umpire in umpire_country:
                country = umpire_country[umpire]

                if country != "India":
                    if country not in country_count:
                        country_count[country] = 0

                    country_count[country] += 1

        sorted_countries = sorted(
            country_count.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        countries = []
        counts = []

        print("\nProgram 3 - Foreign Umpires")

        for country, count in sorted_countries:
            countries.append(country)
            counts.append(count)
            print(country, count)

        plt.figure(figsize=(10, 6))
        plt.bar(countries, counts)
        plt.xlabel("Country")
        plt.ylabel("Number of Umpires")
        plt.title("Number of Foreign Umpires in IPL")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def matches_played_by_team_per_season(self) -> None:
        """Program 4: Matches played by team per season."""

        matches = {}

        with open(
            MATCHES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                season = row["season"]
                team1 = row["team1"]
                team2 = row["team2"]

                if season not in matches:
                    matches[season] = {}

                if team1 not in matches[season]:
                    matches[season][team1] = 0

                matches[season][team1] += 1

                if team2 not in matches[season]:
                    matches[season][team2] = 0

                matches[season][team2] += 1

        seasons = sorted(matches.keys())

        teams = set()

        for season in matches:
            for team in matches[season]:
                teams.add(team)

        teams = sorted(teams)

        bottom = [0] * len(seasons)

        plt.figure(figsize=(14, 7))

        for team in teams:
            team_counts = []

            for season in seasons:
                count = matches[season].get(team, 0)
                team_counts.append(count)

            plt.bar(
                seasons,
                team_counts,
                bottom=bottom,
                label=team,
            )

            for i in range(len(bottom)):
                bottom[i] += team_counts[i]

        plt.xlabel("Season")
        plt.ylabel("Number of Matches Played")
        plt.title("Matches Played by Team per Season")
        plt.xticks(seasons, rotation=45)
        plt.legend(
            bbox_to_anchor=(1.05, 1),
            loc="upper left",
        )
        plt.tight_layout()
        plt.show()

    def matches_played_per_year(self) -> None:
        """Program 5: Number of matches played per year."""

        matches_per_year = {}

        with open(
            MATCHES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                season = row["season"]

                if season not in matches_per_year:
                    matches_per_year[season] = 0

                matches_per_year[season] += 1

        sorted_seasons = sorted(matches_per_year)

        seasons = []
        match_counts = []

        print("\nProgram 5 - Matches Played per Year")

        for season in sorted_seasons:
            seasons.append(season)
            match_counts.append(matches_per_year[season])
            print(season, matches_per_year[season])

        plt.figure(figsize=(12, 6))
        plt.bar(seasons, match_counts)
        plt.xlabel("Year")
        plt.ylabel("Number of Matches")
        plt.title(
            "Number of Matches Played per Year in IPL"
        )
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def matches_played_per_year_program6(self) -> None:
        """Program 6: Same analysis as program 5."""

        self.matches_played_per_year()

    def extra_runs_conceded_2016(self) -> None:
        """Program 7: Extra runs conceded per team in 2016."""

        matches_2016 = set()

        with open(
            MATCHES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["season"] == "2016":
                    matches_2016.add(row["id"])

        extra_runs = {}

        with open(
            DELIVERIES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["match_id"] in matches_2016:
                    team = row["bowling_team"]
                    runs = int(row["extra_runs"])

                    if team not in extra_runs:
                        extra_runs[team] = 0

                    extra_runs[team] += runs

        sorted_teams = sorted(
            extra_runs.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        teams = []
        runs = []

        print(
            "\nProgram 7 - "
            "Extra Runs Conceded in 2016"
        )

        for team, total in sorted_teams:
            teams.append(team)
            runs.append(total)
            print(team, total)

        plt.figure(figsize=(12, 6))
        plt.bar(teams, runs)
        plt.xlabel("Team")
        plt.ylabel("Extra Runs Conceded")
        plt.title(
            "Extra Runs Conceded per Team in IPL 2016"
        )
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def top_10_economical_bowlers(self) -> None:
        """Program 8: Top 10 economical bowlers in 2015."""

        matches_2015 = set()

        with open(
            MATCHES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["season"] == "2015":
                    matches_2015.add(row["id"])

        bowler_runs = {}
        bowler_balls = {}

        with open(
            DELIVERIES_FILE,
            "r",
            encoding="utf-8",
        ) as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["match_id"] not in matches_2015:
                    continue

                bowler = row["bowler"]

                total_runs = int(row["total_runs"])
                bye_runs = int(row["bye_runs"])
                legbye_runs = int(row["legbye_runs"])

                runs_conceded = (
                    total_runs
                    - bye_runs
                    - legbye_runs
                )

                if bowler not in bowler_runs:
                    bowler_runs[bowler] = 0
                    bowler_balls[bowler] = 0

                bowler_runs[bowler] += runs_conceded
                bowler_balls[bowler] += 1

        economy_rates = {}

        for bowler in bowler_runs:
            runs = bowler_runs[bowler]
            balls = bowler_balls[bowler]

            if balls > 0:
                overs = balls / 6
                economy = runs / overs
                economy_rates[bowler] = economy

        sorted_bowlers = sorted(
            economy_rates.items(),
            key=lambda item: item[1],
        )

        top_10 = sorted_bowlers[:10]

        bowlers = []
        economy = []

        print(
            "\nProgram 8 - "
            "Top 10 Economical Bowlers in 2015"
        )

        for bowler, rate in top_10:
            bowlers.append(bowler)
            economy.append(rate)
            print(bowler, round(rate, 2))

        plt.figure(figsize=(12, 6))
        plt.bar(bowlers, economy)
        plt.xlabel("Bowler")
        plt.ylabel("Economy Rate")
        plt.title(
            "Top 10 Economical Bowlers in IPL 2015"
        )
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    def run_all_programs(self) -> None:
        """Run all 8 programs."""

        print("\n========== PROGRAM 1 ==========")
        self.total_runs_by_team()

        print("\n========== PROGRAM 2 ==========")
        self.top_10_rcb_batsmen()

        print("\n========== PROGRAM 3 ==========")
        self.foreign_umpire_analysis()

        print("\n========== PROGRAM 4 ==========")
        self.matches_played_by_team_per_season()

        print("\n========== PROGRAM 5 ==========")
        self.matches_played_per_year()

        print("\n========== PROGRAM 6 ==========")
        self.matches_played_per_year_program6()

        print("\n========== PROGRAM 7 ==========")
        self.extra_runs_conceded_2016()

        print("\n========== PROGRAM 8 ==========")
        self.top_10_economical_bowlers()

        print("\n========== ALL PROGRAMS COMPLETED ==========")


if __name__ == "__main__":
    main = Main()
    main.user_ui()