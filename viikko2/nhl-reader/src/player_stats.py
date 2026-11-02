class PlayerStats:  # pylint: disable=too-few-public-methods
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = [
            player for player in self.players if player.nationality == nationality
        ]
        return sorted(
            players, key=lambda player: player.goals + player.assists, reverse=True
        )

    def top_goal_scorers(self, how_many):
        """Palauttaa maalintekijät maalien mukaan laskevassa järjestyksessä."""
        players = sorted(self.players, key=lambda player: player.goals, reverse=True)
        return players[:how_many]

    def top_scorers_by_team(self, team):
        """Palauttaa joukkueen pelaajat pisteiden mukaan laskevassa järjestyksessä."""
        players = [player for player in self.players if player.team == team]
        return sorted(
            players, key=lambda player: player.goals + player.assists, reverse=True
        )
