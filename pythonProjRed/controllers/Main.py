from tkinter import messagebox
import csv
import pickle

from controllers.EndPage import EndPageController
from controllers.Intro import IntroController
from controllers.Game import GameScreenController
from controllers.Shot import ShotDialogController
from controllers.Rebound import ReboundDialogController
from controllers.StartingLineup import StartingLineupController
from controllers.Substitution import SubstitutionDialogController
from controllers.Turnover import TurnoverDialogController
from models.BasketballGame import BasketballGame
from models.League import League
from tabulate import tabulate

class Controller:
    def __init__(self, view):
        self.view = view
        self.current_game = None
        self.league = League("EnterTeams/bigtenPlayers.pickle")
        self.intro_controller = IntroController(self, self.view)
        self.game_controller = None
        self.shot_controller = None
        self.rebound_controller = None
        self.turnover_controller = None
        self.substitution_controller = None
        self.starting_lineup_controller= None
        self.end_controller = None

    def start(self):  #Loads League, Opens with Intro Page
        with open("EnterTeams/bigtenPlayers.pickle", 'rb') as f:
            self.league = pickle.load(f)

        self.view.switch("intro")
        self.intro_controller.bind()
        self.intro_controller.frame.continue_btn.focus_set()
        self.view.start_mainloop()

    def set_up_game(self, game_num, home, away):
        self.current_game = BasketballGame(game_num, home, away)
        self.game_controller = GameScreenController(self, self.view, self.current_game)

    def start_game(self):
        self.view.switch("game")
        self.game_controller.jump_ball()
        self.current_game.mark_game_started()

    def end_game(self):
        self.end_controller = EndPageController(self, self.view, self.current_game)
        self.view.switch("end")
        self.end_controller.bind()

    def switch_to_shot(self, shot_type=2):
        self.shot_controller = ShotDialogController(self, self.view, self.current_game)
        self.view.switch("shot")
        self.shot_controller.bind()
        self.shot_controller.set_shot_type(shot_type)

    def switch_to_game(self):
        self.view.switch("game")
        self.game_controller.bind()
        self.game_controller.update_scoreboard_labels()
        self.game_controller.update_player_labels()

    def rebound(self):
        self.rebound_controller = ReboundDialogController(self, self.view, self.current_game)
        self.view.switch("rebound")
        self.rebound_controller.bind()

    def turnover(self):
        self.turnover_controller = TurnoverDialogController(self, self.view, self.current_game)

        self.view.switch("turnover")
        self.turnover_controller.bind()

    def substitution(self):
        self.substitution_controller = SubstitutionDialogController(self, self.view, self.current_game)
        self.view.switch("subs")
        self.substitution_controller.bind()

    def starting_lineup(self):
        self.starting_lineup_controller = StartingLineupController(self, self.view, self.current_game)
        self.view.switch("starters")
        self.starting_lineup_controller.bind()

    def shooting_free_throws(self, player, number_of_free_throws):
        self.switch_to_game()
        if number_of_free_throws > 1:
            _free_throw_made = messagebox.askyesno(
                "Free Throw", f"Does {player} make the free throw?")
            self.current_game.free_throw(player, _free_throw_made)
            free_throws_remaining = number_of_free_throws - 1
            self.shooting_free_throws(player, free_throws_remaining)
        else:
            _free_throw_made = messagebox.askyesno(
                "Free Throw", f"Does {player} make the free throw?")
            self.current_game.free_throw(player, _free_throw_made)
            self.game_controller.update_scoreboard_labels()
            self.game_controller.update_player_labels()

            if _free_throw_made:
                self.current_game.change_possession()
            else:
                self.rebound()

    def shooting_one_and_one(self, player):
        _free_throw_made = messagebox.askyesno(
            "Free Throw", f"Does {player} make the free throw?")
        self.current_game.free_throw(player, _free_throw_made)

        if _free_throw_made:
            self.shooting_free_throws(player,1)
        else:
            self.rebound()

    def save_game_log(self):
        _home = self.current_game.home_team
        _road = self.current_game.road_team

        with open('gamelog.csv', mode='w', newline='') as gamelog_file:
            gamelog_writer = csv.writer(gamelog_file, delimiter=',')
            gamelog_writer.writerow(["Player", "Team", "Game_ID", "Minutes", "Game Started",
                                     "FGM", "FGA", "TPM", "TPA", "FTM", "FTA",
                                     "OREB", "DREB", "Ast", "TO", "Stl", "Blk", "PF", "+/-" ])
            for player in self.current_game.home_team.active_roster:
                gamelog_writer.writerow(player.create_statline_log(self.current_game.home_team))
            for player in self.current_game.road_team.active_roster:
                gamelog_writer.writerow(player.create_statline_log(self.current_game.road_team))

            gamelog_writer.writerow("")
            gamelog_writer.writerow(["Team", "Game_ID",
                                     "FGM", "FGA", "TPM", "TPA", "FTM", "FTA",
                                     "OREB", "DREB", "Ast", "TO", "Stl", "Blk", "PF"])
            gamelog_writer.writerow(self.current_game.home_team.create_statline_log())
            gamelog_writer.writerow(self.current_game.road_team.create_statline_log())

    def save_txt_game_log(self):
        _home = self.current_game.home_team
        _road = self.current_game.road_team

        _headers = ["Player","Min","GS","FG","FGA","3P","3PA","FT","FTA","OR","DR","A","TO","ST","BL","PF","+/-","Pts"]
        _home_stats = []
        _road_stats = []
        for player in _home.active_roster:
            _home_stats.append(player.create_statline_log(_home))
        for player in _road.active_roster:
            _road_stats.append(player.create_statline_log(_home))

        _home_stats.append(_home.create_statline_log())
        _road_stats.append(_road.create_statline_log())

        print(f"Visitor: {_road}")
        print(tabulate(_road_stats, _headers))
        print("\n\n")
        print(f"Home: {_home}")
        print(tabulate(_home_stats,_headers))

