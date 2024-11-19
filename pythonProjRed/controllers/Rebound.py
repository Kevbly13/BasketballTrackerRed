class ReboundDialogController:
    def __init__(self, prime_control, view, game):
        self.view = view
        self.current_game = game
        self.main_controller = prime_control
        self.frame = self.view.frames["rebound"]

    def bind(self):
        self.view.root.bind("<Key>", self.rebound_key_handler)
        self.frame.btn_foul.config(command=self.foul_click)
        self.frame.btn_jump_ball.config(command=self.jumpball)
        self.frame.btn_rebound.config(command=self.rebound)
        self.frame.btn_rebound.focus_set()

    def rebound_key_handler(self, event):
        if event.keysym == '1':
            self.frame.var_rebounder.set(0)
        elif event.keysym == '2':
            self.frame.var_rebounder.set(1)
        elif event.keysym == '3':
            self.frame.var_rebounder.set(2)
        elif event.keysym == '4':
            self.frame.var_rebounder.set(3)
        elif event.keysym == '5':
            self.frame.var_rebounder.set(4)
        elif event.keysym == '6':
            self.frame.var_rebounder.set(5)

        elif event.keysym == 'q':
            self.frame.var_rebounder.set(6)
        elif event.keysym == 'w':
            self.frame.var_rebounder.set(7)
        elif event.keysym == 'e':
            self.frame.var_rebounder.set(8)
        elif event.keysym == 'r':
            self.frame.var_rebounder.set(9)
        elif event.keysym == 't':
            self.frame.var_rebounder.set(10)
        elif event.keysym == 'y':
            self.frame.var_rebounder.set(11)

    def jumpball(self):
        self.current_game.jump_ball_arrow()
        self.main_controller.switch_to_game()

    def rebound(self):
        _rebounding_team = ""
        if self.frame.var_rebounder.get() <=5:
            _rebounding_team = "def"
        else:
            _rebounding_team = "off"

        self.current_game.rebound(_rebounding_team, self.convert_choice_to_player())
        self.main_controller.switch_to_game()

    def foul_click(self):
        _fouling_team = ""
        if self.frame.var_rebounder.get() <= 5:
            _fouling_team = "def"
        else:
            _fouling_team = "off"

        self.current_game.rebounding_foul(_fouling_team, self.convert_choice_to_player())

        if self.current_game.team_on_defense().is_in_double_penalty(self.current_game.time.period):
            self.main_controller.shooting_free_throws(self.get_opposing_player(), 2)
        elif self.current_game.team_on_defense().is_in_penalty(self.current_game.time.period):
            self.main_controller.shooting_one_and_one(self.get_opposing_player())
        else:
            self.main_controller.switch_to_game()

    def convert_choice_to_player(self):
        if self.frame.var_rebounder.get() == 0:
            return self.current_game.team_on_defense().active_roster[0]
        elif self.frame.var_rebounder.get() == 1:
            return self.current_game.team_on_defense().active_roster[1]
        elif self.frame.var_rebounder.get() == 2:
            return self.current_game.team_on_defense().active_roster[2]
        elif self.frame.var_rebounder.get() == 3:
            return self.current_game.team_on_defense().active_roster[3]
        elif self.frame.var_rebounder.get() == 4:
            return self.current_game.team_on_defense().active_roster[4]
        elif self.frame.var_rebounder.get() == 6:
            return self.current_game.team_on_offense().active_roster[0]
        elif self.frame.var_rebounder.get() == 7:
            return self.current_game.team_on_offense().active_roster[1]
        elif self.frame.var_rebounder.get() == 8:
            return self.current_game.team_on_offense().active_roster[2]
        elif self.frame.var_rebounder.get() == 9:
            return self.current_game.team_on_offense().active_roster[3]
        elif self.frame.var_rebounder.get() == 10:
            return self.current_game.team_on_offense().active_roster[4]
        else:
            return None

    def get_opposing_player(self):
        if self.frame.var_rebounder.get() == 0:
            return self.current_game.team_on_offense().active_roster[0]
        elif self.frame.var_rebounder.get() == 1:
            return self.current_game.team_on_offense().active_roster[1]
        elif self.frame.var_rebounder.get() == 2:
            return self.current_game.team_on_offense().active_roster[2]
        elif self.frame.var_rebounder.get() == 3:
            return self.current_game.team_on_offense().active_roster[3]
        elif self.frame.var_rebounder.get() == 4:
            return self.current_game.team_on_offense().active_roster[4]
        elif self.frame.var_rebounder.get() == 6:
            return self.current_game.team_on_defense().active_roster[0]
        elif self.frame.var_rebounder.get() == 7:
            return self.current_game.team_on_defense().active_roster[1]
        elif self.frame.var_rebounder.get() == 8:
            return self.current_game.team_on_defense().active_roster[2]
        elif self.frame.var_rebounder.get() == 9:
            return self.current_game.team_on_defense().active_roster[3]
        elif self.frame.var_rebounder.get() == 10:
            return self.current_game.team_on_defense().active_roster[4]
        else:
            return None
