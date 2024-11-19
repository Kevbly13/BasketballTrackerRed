from tkinter import messagebox
from models.Team import GameTeam
from models.TimeKeeper import TimeKeeper
from setUp.GameRules import MIN_MOMENTUM, MAX_MOMENTUM, CLOCK_INTERVAL

class BasketballGame:
    def __init__(self, game_number, home_team, road_team):
        self.game_number = game_number

        self.home_team = GameTeam(home_team, self.game_number)
        self.road_team = GameTeam(road_team, self.game_number)

        self.time = TimeKeeper()
        self.momentum_meter = MomentumMeter()
        self.possession_arrow_to_home = True

##### Display ####################################################################

    def display_current_possession(self):
        if self.home_team.has_possession:
            return f"{self.home_team.team.name} has the ball"
        else:
            return f"{self.road_team.team.name} has the ball"

    def display_possession_arrow(self):
        if self.possession_arrow_to_home:
            return "POS <-"
        else:
            return "POS ->"

    def team_on_offense(self):
        if self.home_team.has_possession:
            return self.home_team
        else:
            return self.road_team

    def team_on_defense(self):
        if self.home_team.has_possession:
            return self.road_team
        else:
            return self.home_team

##### Game Actions ##############################################################

    def timeout(self):
        if self.home_team.has_possession:
            if self.home_team.timeouts <= 0:
                messagebox.showinfo(title="Alert", message="No timeouts remaining")
            else:
                self.home_team.timeouts -= 1
                self.momentum_meter.momentum = 0
        else:
            if self.road_team.timeouts <= 0:
                messagebox.showinfo(title="Alert", message="No timeouts remaining")
            else:
                self.road_team.timeouts -= 1
                self.momentum_meter.momentum = 0

    def mark_game_started(self):
        for n in range(5):
            self.home_team.get_starters()[n].started_game = True
            self.road_team.get_starters()[n].started_game = True

    def change_possession(self):
        if self.home_team.has_possession:
            self.home_team.has_possession = False
            self.road_team.has_possession = True
        else:
            self.home_team.has_possession = True
            self.road_team.has_possession = False

    def turnover(self, player):
        self.change_possession()
        print(f"{player} turns it over")
        player.turnovers += 1
        self.team_on_offense().turnovers += 1

    def steal(self, off_player, def_player):
        self.change_possession()
        print(f"{def_player} steals the ball from {off_player}")
        off_player.turnovers += 1
        self.team_on_offense().turnovers += 1
        def_player.steals += 1
        self.team_on_defense().steals += 1

    def offensive_foul(self, player):
        self.change_possession()
        print(f"Offensive foul on {player}")
        player.fouls += 1
        player.turnovers += 1
        self.team_on_offense().turnovers += 1

    def jump_ball(self, home_wins_jump):
        self.home_team.has_possession = home_wins_jump
        self.time.has_game_started = True

        if self.home_team.has_possession:
            self.possession_arrow_to_home = False
            self.road_team.has_possession = False
        else:
            self.possession_arrow_to_home = True
            self.road_team.has_possession = True

    def jump_ball_arrow(self):
        if self.possession_arrow_to_home:
            self.possession_arrow_to_home = False
            self.home_team.has_possession = True
            self.road_team.has_possession = False
        else:
            self.possession_arrow_to_home = True
            self.home_team.has_possession = False
            self.road_team.has_possession = True

    def shot_made(self, shot_type, player, assist = None):
        self.score(shot_type)
        if assist is not None:
            print(f"{player.first_name} {player.last_name} scores a {shot_type}-point basket. Assist to {assist}")
            assist.assists += 1
            self.team_on_offense().assists += 1
        else:
            print(f"{player} score a {shot_type}-point basket")

        player.fieldgoal_attempts += 1
        player.fieldgoal_makes += 1
        self.team_on_offense().fieldgoal_attempts += 1
        self.team_on_offense().fieldgoal_makes += 1
        if shot_type == 3:
            player.threepoint_attempts += 1
            player.threepoint_makes += 1
            self.team_on_offense().threepoint_attempts += 1
            self.team_on_offense().threepoint_makes += 1

    def shot_missed(self, shot_type, player, block = None):
        if block is not None:
            print(f"{player} is blocked by {block}")
            block.blocks += 1
            self.team_on_defense().blocks += 1
        else:
            print(f"{player} misses a {shot_type}-point shot")

        player.fieldgoal_attempts += 1
        self.team_on_offense().fieldgoal_attempts += 1
        if shot_type == 3:
            player.threepoint_attempts += 1
            self.team_on_offense().threepoint_attempts += 1

    def rebound(self, team, player=None):
        if team == "off":
            self.team_on_offense().offensive_rebounds += 1
            if player is not None:
                print(f"{player.last_name} gets the rebound")
                player.offensive_rebounds += 1
        else:
            self.team_on_defense().defensive_rebounds +=1
            self.change_possession()
            if player is not None:
                print(f"{player.last_name} gets the rebound")
                player.defensive_rebounds += 1

    def free_throw(self, player, free_throw_made):
        player.freethrow_attempts += 1
        self.team_on_offense().freethrow_attempts += 1

        if free_throw_made:
            self.score(1)
            print(f"{player} makes a free throw")
            player.freethrow_makes += 1
            self.team_on_offense().freethrow_makes += 1
        else:
            print(f"{player} misses a free throw")

    def defensive_foul(self, player=None):
        _defensive_team = self.team_on_defense()
        _defensive_team.fouls[self.time.period - 1] += 1
        if player is not None:
            print(f"{player} fouls")
            player.fouls += 1
        else:
            print("Team foul")

    def rebounding_foul(self, team, player=None):
        if team == "off":
            self.change_possession()
            self.defensive_foul(player)
        else:
            self.defensive_foul(player)

    def score(self, points):
        _shooting_team = self.team_on_offense()
        _defending_team = self.team_on_defense()
        _shooting_team.score[self.time.period - 1] += points

        for n in range(5):
            _shooting_team.active_roster[n].plus_minus += points
            _defending_team.active_roster[n].plus_minus -= points

#### Time Functions ########################################################################
    def advance_time(self):
        self.time.advance_time()
        for player in self.home_team.get_starters():
            player.play_for(CLOCK_INTERVAL)
        for player in self.road_team.get_starters():
            player.play_for(CLOCK_INTERVAL)
        for player in self.home_team.get_bench():
            player.rest_for(CLOCK_INTERVAL)
        for player in self.road_team.get_bench():
            player.rest_for(CLOCK_INTERVAL)

    def halftime(self):
        self.momentum_meter.momentum = 0
        for player in self.home_team.active_roster:
            player.rest_this_half = 0
        for player in self.road_team.active_roster:
            player.rest_this_half = 0

        self.time.is_it_halftime = False
        self.jump_ball_arrow()

    def is_tied(self):
        return self.home_team.total_score() == self.road_team.total_score()


class MomentumMeter:
    def __init__(self, momentum=0):
        self.momentum = momentum

    def display_scoreboard(self):
        if self.momentum == 0:
            return 0
        elif self.momentum > 0:
            return f"<- {abs(self.momentum)}"
        else:
            return f"{abs(self.momentum)} ->"

    def change_momentum(self,magnitude):
        self.momentum += magnitude
        if self.momentum > MAX_MOMENTUM:
            self.momentum = MAX_MOMENTUM
        elif self.momentum < MIN_MOMENTUM:
            self.momentum = MIN_MOMENTUM






