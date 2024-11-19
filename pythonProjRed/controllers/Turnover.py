class TurnoverDialogController:
    def __init__(self, prime_control, view, game):
        self.view = view
        self.current_game = game
        self.main_controller = prime_control
        self.frame = self.view.frames["turnover"]

    def bind(self):
        self.view.root.bind("<Key>", self.turnover_key_handler)
        self.frame.btn_cancel.config(command=self.click_cancel)
        self.frame.btn_ok.config(command=self.click_turnover)

        self.frame.btn_ok.focus_set()

    def turnover_key_handler(self, event):
        if event.keysym == '1':
            self.frame.var_offender.set(0)
            self.frame.var_defender.set(0)
        elif event.keysym == '2':
            self.frame.var_offender.set(1)
            self.frame.var_defender.set(1)
        elif event.keysym == '3':
            self.frame.var_offender.set(2)
            self.frame.var_defender.set(2)
        elif event.keysym == '4':
            self.frame.var_offender.set(3)
            self.frame.var_defender.set(3)
        elif event.keysym == '5':
            self.frame.var_offender.set(4)
            self.frame.var_defender.set(4)
        elif event.keysym == 'a':
            self.frame.var_turnover_type.set(0)
            self.frame.disable_defender_choices()
        elif event.keysym == 's':
            self.frame.var_turnover_type.set(1)
            self.frame.enable_defender_choices()
        elif event.keysym == 'd':
            self.frame.var_turnover_type.set(2)
            self.frame.enable_defender_choices()
        elif event.keysym == 'f':
            self.frame.var_turnover_type.set(3)
            self.frame.disable_defender_choices()

    def click_cancel(self):
        self.main_controller.switch_to_game()

    def click_turnover(self):
        _offensive_team = self.current_game.team_on_offense()
        _defensive_team = self.current_game.team_on_defense()
        _turnover_type = self.frame.var_turnover_type.get()
        _offender = _offensive_team.active_roster[self.frame.var_offender.get()]
        _defender = _defensive_team.active_roster[self.frame.var_defender.get()]

        if _turnover_type == 0:
            self.current_game.turnover(_offender)
            self.main_controller.switch_to_game()
        elif _turnover_type == 1:
            self.current_game.steal(_offender, _defender)
            self.main_controller.switch_to_game()
        elif _turnover_type == 2:
            self.foul(_offender, _defender)
        elif _turnover_type == 3:
            self.current_game.offensive_foul(_offender)
            self.main_controller.switch_to_game()


    def foul(self, offensive_player, defensive_player):
        self.current_game.defensive_foul(defensive_player)
        if self.current_game.team_on_defense().is_in_double_penalty(self.current_game.time.period):
            self.main_controller.shooting_free_throws(offensive_player,2)
        elif self.current_game.team_on_defense().is_in_penalty(self.current_game.time.period):
            self.main_controller.shooting_one_and_one(offensive_player)
        else:
            self.main_controller.switch_to_game()

