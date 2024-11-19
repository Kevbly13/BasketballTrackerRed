from models.Team import GameTeam


class IntroController:
    def __init__(self, prime_controller, view):
        self.view = view
        self.main_control = prime_controller
        self.frame = self.view.frames["intro"]

    def bind(self):
        self.frame.continue_btn.config(command=self.start_game)
        self.init_comboboxes()

    def start_game(self):
        if self.frame.home_team_cb.current() == self.frame.road_team_cb.current():
            print("Can't select the same team twice")
            pass
        else:
            _home_team = None
            _road_team = None
            _game_num = self.frame.var_game_number.get()
            for team in self.main_control.league.teams:
                if self.frame.home_team_cb.get() == team.name:
                    _home_team = team
                if self.frame.road_team_cb.get() == team.name:
                    _road_team = team

            self.main_control.set_up_game(_game_num, _home_team, _road_team)
            self.main_control.starting_lineup()

    def init_comboboxes(self):
        _teams = []
        for team in self.main_control.league.teams:
            _teams.append(team.name)
        _teams.sort()

        self.frame.home_team_cb['values'] = _teams
        self.frame.home_team_cb.current(0)
        self.frame.home_team_cb.bind('<<ComboboxSelected>>')

        self.frame.road_team_cb['values'] = _teams
        self.frame.road_team_cb.current(1)
        self.frame.road_team_cb.bind('<<ComboboxSelected>>')


