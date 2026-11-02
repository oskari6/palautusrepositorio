from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


SEASONS = [
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26",
]
NATIONALITIES = [
    "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR",
    "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB",
    "LAT", "AUS",
]


def print_players(players, season, selection):
    console = Console()
    console.print(f"\nSeason {season} players from {selection}\n")

    table = Table(show_header=True, header_style="bold")
    table.add_column("Released")
    table.add_column("teams")
    table.add_column("goals", justify="right")
    table.add_column("assists", justify="right")
    table.add_column("points", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team or "",
            str(player.goals or 0),
            str(player.assists or 0),
            str((player.goals or 0) + (player.assists or 0)),
        )

    if players:
        console.print(table)
    else:
        console.print("No players found.")


def main():
    default_season = "2024-25"
    season_prompt = "/".join(SEASONS)
    season = input(f"Season [{season_prompt}] ({default_season}): ").strip()
    if not season:
        season = default_season
    if season not in SEASONS:
        print(f"Unknown season: {season}")
        return

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    nationality_prompt = "/".join(NATIONALITIES)
    while True:
        nationality = input(f"Nationality [{nationality_prompt}] (): ").strip().upper()
        if not nationality:
            break
        if nationality not in NATIONALITIES:
            print("Unknown nationality.")
            continue

        players = stats.top_scorers_by_nationality(nationality)
        print_players(players, season, nationality)

    team = input("Team (leave empty to quit): ").strip().upper()
    if team:
        players = stats.top_scorers_by_team(team)
        print_players(players, season, team)


if __name__ == "__main__":
    main()
