from models.Player import GamePlayer
from models.StatLine import TeamGameLog
from setUp.GameRules import FOULS_FOR_BONUS, FOULS_FOR_DOUBLE_BONUS, TIMEOUTS_PER_PERIOD, NUMBER_OF_PERIODS

class Team:
    def __init__(self, name, mascot):
        self.name = name
        self.mascot = mascot
        self.roster = []
        self.game_log = []

    def __str__(self):
        return f"{self.name} {self.mascot}"

    def __lt__(self, other):
        return self.name < other.name

    def set_roster(self, player_list):
        for hooper in player_list:
            self.roster.append(hooper)

class GameTeam:
    def __init__(self, team, game_number):
        self.team = team
        self.game_id = game_number
        self.active_roster = []
        self.score = []
        self.fouls = []
        self.timeouts = TIMEOUTS_PER_PERIOD
        self.has_possession = False

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

        self.set_stats_by_period()
        self.set_roster()

    ##### Get Functions #######################################################################
    def __str__(self):
        return f"{self.team.name} {self.team.mascot}"

    def total_fouls(self):
        _total_fouls = 0
        for n in range(NUMBER_OF_PERIODS):
            _total_fouls += self.fouls[n]
        return _total_fouls

    def total_score(self):
        _total_score = 0
        for n in range(NUMBER_OF_PERIODS):
            _total_score += self.score[n]
        return _total_score

    def is_in_penalty(self, current_period):
        return self.fouls[current_period - 1] >= FOULS_FOR_BONUS

    def is_in_double_penalty(self, current_period):
        return self.fouls[current_period - 1] >= FOULS_FOR_DOUBLE_BONUS

    def get_bench(self):
        return self.active_roster[5:]

    def get_starters(self):
        return self.active_roster[0:5]

    ##### Initialization Functions ################################################################
    def set_stats_by_period(self):
        self.score = [0] * NUMBER_OF_PERIODS
        self.fouls = [0] * NUMBER_OF_PERIODS

    def set_roster(self):
        for player in self.team.roster:
            _active_player = GamePlayer(player, self.game_id)
            self.active_roster.append(_active_player)

    ##### Game Functions ###########################################################################
    def sub(self, new_lineup):
        _shuffled_lineup = []
        for player_name in new_lineup:
            for rostered_player in self.active_roster:
                if player_name == rostered_player.full_name():
                    _shuffled_lineup.append(rostered_player)
        for rostered_player in self.active_roster:
            if rostered_player in _shuffled_lineup:
                pass
            else:
                _shuffled_lineup.append(rostered_player)
        self.active_roster = _shuffled_lineup

    ##### Logging Functions ########################################################################
    def create_statline_log(self):
        _box_score_line = [self.team.name, "-", "-",
                            self.fieldgoal_makes, self.fieldgoal_attempts,
                            self.threepoint_makes, self.threepoint_attempts,
                            self.freethrow_makes, self.freethrow_attempts,
                            self.offensive_rebounds, self.defensive_rebounds,
                            self.assists, self.turnovers, self.steals, self.blocks, self.total_fouls(),
                           "-", self.total_score()]
        return _box_score_line

    def create_game_statline(self, opponent, won_game):
        _shooting_splits = [self.fieldgoal_makes, self.fieldgoal_attempts,
                            self.freethrow_makes, self.freethrow_attempts,
                            self.threepoint_makes, self.threepoint_attempts]
        _floor_game_stats = [self.offensive_rebounds, self.defensive_rebounds,
                             self.assists, self.turnovers, self.steals, self.blocks, self.total_fouls]
        _box_score_line = TeamGameLog(self.game_id, opponent, won_game,
                                        _shooting_splits, _floor_game_stats)
        return _box_score_line





