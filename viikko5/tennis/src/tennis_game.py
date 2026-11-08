class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3
    WINNING_SCORE = 4
    GAME_POINT_MARGIN = 2

    SCORE_NAMES = ("Love", "Fifteen", "Thirty", "Forty")
    TIED_SCORE_NAMES = ("Love-All", "Fifteen-All", "Thirty-All")

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_tied_score()
        if self.is_advantage_or_won():
            return self.get_advantage_or_winner_score()
        return self.get_regular_score()

    def get_tied_score(self):
        if self.player1_score < len(self.TIED_SCORE_NAMES):
            return self.TIED_SCORE_NAMES[self.player1_score]
        return "Deuce"

    def is_advantage_or_won(self):
        return max(self.player1_score, self.player2_score) >= self.WINNING_SCORE

    def get_advantage_or_winner_score(self):
        score_difference = self.player1_score - self.player2_score
        if abs(score_difference) == 1:
            advantaged_player = "player1" if score_difference > 0 else "player2"
            return "Advantage " + advantaged_player
        winning_player = "player1" if score_difference > 0 else "player2"
        return "Win for " + winning_player

    def get_regular_score(self):
        player1_points = self.SCORE_NAMES[self.player1_score]
        player2_points = self.SCORE_NAMES[self.player2_score]
        return player1_points + "-" + player2_points
