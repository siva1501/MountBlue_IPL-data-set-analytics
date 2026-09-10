"""IPL data analysis project."""

import pandas as pd
import matplotlib.pyplot as plt


def matches_played_by_team_by_season():
    """Plot stacked chart of matches played by team by season."""

    matches = pd.read_csv("data/matches.csv")

    # Get team1 matches
    team1 = matches[["season", "team1"]].rename(columns={"team1": "team"})

    # Get team2 matches
    team2 = matches[["season", "team2"]].rename(columns={"team2": "team"})

    # Combine both teams
    team_matches = pd.concat([team1, team2])

    # Count matches played by each team in each season
    matches_played = team_matches.groupby(["season", "team"]).size()
    # Convert to table format
    matches_played = matches_played.unstack(fill_value=0)
    print(matches_played)
    # Plot stacked bar chart
    matches_played.plot(kind="bar", stacked=True, figsize=(14, 7))

    plt.title("Matches Played by Team by Season")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
matches_played_by_team_by_season()
