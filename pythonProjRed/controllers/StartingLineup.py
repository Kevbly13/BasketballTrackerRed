import random

class StartingLineupController:
    def __init__(self, prime_control, view, game):
        self.view = view
        self.current_game = game
        self.main_controller = prime_control
        self.frame = self.view.frames["starters"]

    def bind(self):
        self.set_team_labels()
        self.run_injury_checks()
        self.update_home_dropdowns()
        self.update_road_dropdowns()
        self.frame.btn_continue.config(command=self.main_controller.start_game)
        self.frame.btn_continue.focus_set()

    def update_home_dropdowns(self):
        _home_team = self.current_game.home_team
        _home_bench = []

        for player in _home_team.get_bench():
            _home_bench.append(player.full_name())

        for n in range(5):
            _home_bench.insert(0,_home_team.get_starters()[n].full_name())
            self.frame.home_comboboxes[n]['values'] = _home_bench
            _home_bench.pop(0)
            self.frame.home_comboboxes[n].current(0)
            self.frame.home_comboboxes[n].bind('<<ComboboxSelected>>', self.make_sub)

    def update_road_dropdowns(self):
        _road_team = self.current_game.road_team
        _road_bench = []

        for player in _road_team.get_bench():
            _road_bench.append(player.full_name())

        for n in range(5):
            _road_bench.insert(0,_road_team.get_starters()[n].full_name())
            self.frame.road_comboboxes[n]['values'] = _road_bench
            _road_bench.pop(0)
            self.frame.road_comboboxes[n].current(0)
            self.frame.road_comboboxes[n].bind('<<ComboboxSelected>>', self.make_sub)

    def set_team_labels(self):
        self.frame.lbl_home_team.config(text= self.current_game.home_team)
        self.frame.lbl_road_team.config(text=self.current_game.road_team)

    def make_sub(self, event):
        _new_home_lineup = []
        for var in self.frame.var_choice_home:
            _new_home_lineup.append(var.get())
        self.current_game.home_team.sub(_new_home_lineup)

        _new_road_lineup = []
        for var in self.frame.var_choice_road:
            _new_road_lineup.append(var.get())
        self.current_game.road_team.sub(_new_road_lineup)

        self.update_home_dropdowns()
        self.update_road_dropdowns()

    def run_injury_checks(self):
        _home_team = self.current_game.home_team

        for player in _home_team.active_roster:
            random_number = random.randint(1, 40)
            if len(_home_team.active_roster) >= 9 and player.injury_rating > random_number:
                _home_team.active_roster.remove(player)
                print (f"{player} ({_home_team}) not available for game")

        _road_team = self.current_game.road_team
        for player in _road_team.active_roster:
            random_number = random.randint(1,40)
            if len(_road_team.active_roster) >= 9 and player.injury_rating > random_number:
                _road_team.active_roster.remove(player)
                print(f"{player} ({_road_team}) not available for game")
