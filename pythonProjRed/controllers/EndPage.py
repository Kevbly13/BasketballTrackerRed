
class EndPageController:
    def __init__(self, prime_control, view, game):
        self.view = view
        self.current_game = game
        self.main_controller = prime_control
        self.frame = self.view.frames["end"]

    def bind(self):
        self.set_labels()
        self.frame.button.config(command=self.finish_game)

    def set_labels(self):
        self.frame.lbl_home_team.config(text=self.current_game.home_team.team.name)
        self.frame.lbl_road_team.config(text=self.current_game.road_team.team.name)
        self.frame.lbl_home_team_mascot.config(text=self.current_game.home_team.team.mascot)
        self.frame.lbl_road_team_mascot.config(text=self.current_game.road_team.team.mascot)
        self.frame.lbl_home_team_score.config(text=self.current_game.home_team.score)
        self.frame.lbl_road_team_score.config(text=self.current_game.road_team.score)

    def finish_game(self):
        self.main_controller.save_game_log()
        self.main_controller.start()

