from math import floor
import setUp.GameRules
from models.StatLine import PlayerGameLog


class Player:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.rest_first_half = 0
        self.rest_second_half = 0
        self.injury_rating = 0

    def __str__(self):
        return f"{self.last_name}, {self.first_name[0]}."

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def enter_rest(self, injury, first, second):
        self.rest_first_half = first * 3
        self.rest_second_half = second * 3
        self.injury_rating = injury


class GamePlayer:
    def __init__(self, player, game_number):
        self.first_name = player.first_name
        self.last_name = player.last_name
        self.rest_first_half = player.rest_first_half
        self.rest_second_half = player.rest_second_half
        self.injury_rating = player.injury_rating

        self.rest_this_half = 0

        self.seconds_played = 0
        self.fieldgoal_attempts = 0
        self.fieldgoal_makes = 0
        self.threepoint_attempts = 0
        self.threepoint_makes = 0
        self.freethrow_attempts = 0
        self.freethrow_makes = 0
        self.offensive_rebounds = 0
        self.defensive_rebounds = 0
        self.assists = 0
        self.turnovers = 0
        self.steals = 0
        self.blocks = 0
        self.fouls = 0
        self.plus_minus = 0

        self.started_game = False
        self.game_id = game_number

    def __str__(self):
        return f"{self.last_name}, {self.first_name[0]}."

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def points(self):
        _pts = self.fieldgoal_makes * 2 + self.threepoint_makes + self.freethrow_makes
        return _pts

    def rebounds(self):
        return self.offensive_rebounds + self.defensive_rebounds

    def has_player_fouled_out(self):
        return self.fouls >= setUp.GameRules.PERSONAL_FOULS_PER_GAME

    def is_player_fatigued(self, minutes_remaining: int, half) -> bool:
        if half == 2:
            if (self.rest_second_half - self.rest_this_half) > minutes_remaining:
                return True
            else:
                return False
        else:
            if (self.rest_first_half - self.rest_this_half) > minutes_remaining:
                return True
            else:
                return False

    def create_game_statline(self):
        _shooting_splits = [self.fieldgoal_makes, self.fieldgoal_attempts,
                            self.freethrow_makes, self.freethrow_attempts,
                            self.threepoint_makes, self.threepoint_attempts]
        _floor_game_stats = [self.offensive_rebounds, self.defensive_rebounds,
                             self.assists, self.turnovers, self.steals, self.blocks, self.fouls]
        _box_score_line = PlayerGameLog(self.game_id, self.minutes_played(), self.started_game,
                                        _shooting_splits, _floor_game_stats, self.plus_minus)
        return _box_score_line

    def create_statline_log(self, team_name):
        _box_score_line = [str(self), self.minutes_played(), self.started_game,
                            self.fieldgoal_makes, self.fieldgoal_attempts,
                            self.threepoint_makes, self.threepoint_attempts,
                            self.freethrow_makes, self.freethrow_attempts,
                            self.offensive_rebounds, self.defensive_rebounds,
                            self.assists, self.turnovers, self.steals, self.blocks, self.fouls,
                            self.plus_minus, self.points()]
        return _box_score_line

    def play_for(self, seconds):
        self.seconds_played += seconds

    def rest_for(self, seconds):
        self.rest_this_half += seconds

    def minutes_played(self):
        return floor(self.seconds_played / 60)

