class PlayerGameLog:
    def __init__(self, game_id, minutes, started_game, shooting_stats, floor_game_stats, plus_minus):
        self.game_id = game_id
        self.started = started_game
        self.plus_minus = plus_minus
        self.minutes = minutes
        self.field_goal_makes = shooting_stats[0]
        self.field_goal_attempts = shooting_stats[1]
        self.free_throw_makes = shooting_stats[2]
        self.free_throw_attempts = shooting_stats[3]
        self.three_point_field_goal_makes = shooting_stats[4]
        self.three_point_field_goal_attempts = shooting_stats[5]
        self.offensive_rebounds = floor_game_stats[0]
        self.defensive_rebounds = floor_game_stats[1]
        self.assists = floor_game_stats[2]
        self.turnovers = floor_game_stats[3]
        self.steals = floor_game_stats[4]
        self.blocks = floor_game_stats[5]
        self.fouls = floor_game_stats[6]

class TeamGameLog:
    def __init__(self, game_id, opponent, result, shooting_stats, floor_game_stats):
        self.game_id = game_id
        self.opponent = opponent
        self.wins = result
        self.field_goal_makes = shooting_stats[0]
        self.field_goal_attempts = shooting_stats[1]
        self.free_throw_makes = shooting_stats[2]
        self.free_throw_attempts = shooting_stats[3]
        self.three_point_field_goal_makes = shooting_stats[4]
        self.three_point_field_goal_attempts = shooting_stats[5]
        self.offensive_rebounds = floor_game_stats[0]
        self.defensive_rebounds = floor_game_stats[1]
        self.assists = floor_game_stats[2]
        self.turnovers = floor_game_stats[3]
        self.steals = floor_game_stats[4]
        self.blocks = floor_game_stats[5]
        self.fouls = floor_game_stats[6]


