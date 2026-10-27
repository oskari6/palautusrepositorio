import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player_by_full_name(self):
        player = self.stats.search("Kurri")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 90)

    def test_search_finds_player_by_partial_name(self):
        player = self.stats.search("mieux")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_returns_none_when_player_is_missing(self):
        self.assertIsNone(self.stats.search("Unknown"))

    def test_team_returns_only_players_of_requested_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"],
        )

    def test_team_returns_empty_list_when_team_is_missing(self):
        self.assertEqual(self.stats.team("PHI"), [])

    def test_top_returns_players_in_descending_points_order(self):
        # Nykyinen rajapinta palauttaa how_many + 1 pelaajaa.
        players = self.stats.top(2)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"],
        )

    def test_top_zero_returns_best_player(self):
        players = self.stats.top(0)

        self.assertEqual([player.name for player in players], ["Gretzky"])

    def test_top_sorts_by_points_when_requested(self):
        players = self.stats.top(2, SortBy.POINTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"],
        )
        self.assertEqual(players, self.stats.top(2))

    def test_top_sorts_by_goals_when_requested(self):
        players = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"],
        )

    def test_top_sorts_by_assists_when_requested(self):
        players = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"],
        )

    def test_top_can_return_all_players_in_points_order(self):
        players = self.stats.top(4)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"],
        )
