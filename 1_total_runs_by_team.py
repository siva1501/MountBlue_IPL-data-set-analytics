import csv


# CHANGE: renamed parameter from generic "s" to "value" and narrowed except to ValueError for clarity.
def to_int(value: str, default: int = 0) -> int:
    """
    Safely convert a string to integer.

    Args:
        value (str): Input string to convert.
        default (int): Value to return if conversion fails.

    Returns:
        int: Converted integer or default if conversion fails.
    """
    try:
        return int((value or "").strip())
    except ValueError:
        return default


def calculate_total_runs_by_team(filepath: str) -> dict[str, int]:
    """
    Calculate total runs scored by each team.

    Args:
        filepath (str): Path to the CSV file containing deliveries data.

    Returns:
        dict[str, int]: Mapping team name -> total runs.
    """
    team_runs: dict[str, int] = {}

    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for delivery in reader:
            batting_team = (delivery.get("batting_team") or "").strip()
            if not batting_team:
                continue

            runs = to_int(delivery.get("total_runs"), default=0)

            team_runs[batting_team] = team_runs.get(batting_team, 0) + runs

    return team_runs
