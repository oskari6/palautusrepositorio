from types import SimpleNamespace

from player_stats import PlayerStats


class StubPlayerReader:  # pylint: disable=too-few-public-methods
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def make_player(name, nationality, team, goals, assists):
    return SimpleNamespace(
        name=name,
        nationality=nationality,
        team=team,
        goals=goals,
        assists=assists,
    )


def make_stats():
    players = [
        make_player("A", "FIN", "AAA", 10, 5),
        make_player("B", "FIN", "BBB", 8, 10),
        make_player("C", "CAN", "AAA", 12, 1),
        make_player("D", "FIN", "AAA", 3, 4),
    ]
    return PlayerStats(StubPlayerReader(players))


def test_top_scorers_by_nationality_orders_by_points():
    stats = make_stats()

    result = stats.top_scorers_by_nationality("FIN")

    assert [player.name for player in result] == ["B", "A", "D"]


def test_top_goal_scorers_returns_requested_number_in_order():
    stats = make_stats()

    result = stats.top_goal_scorers(2)

    assert [player.name for player in result] == ["C", "A"]


def test_top_scorers_by_team_filters_team_and_orders_by_points():
    stats = make_stats()

    result = stats.top_scorers_by_team("AAA")

    assert [player.name for player in result] == ["A", "C", "D"]
