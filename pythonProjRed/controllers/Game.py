from tkinter import messagebox

class GameScreenController:
    def __init__(self, prime_control, view, game):
        self.view = view
        self.current_game = game
        self.main_controller = prime_control
        self.frame = self.view.frames["game"]
        self.scoreboard_frame = self.frame.scoreboard_frame
        self.player_frame = self.frame.player_frame
        self.bind()
        self.update_player_labels()
        self.update_scoreboard_labels()

    def bind(self):
        self.view.root.bind("<Key>", self.key_handler)

    def key_handler(self, event):
        if event.keysym == 'space':
            self.current_game.advance_time()
            self.check_half_time()
            self.check_game_over()
        elif event.keysym == "1":
            self.main_controller.turnover()
        elif event.keysym == "2":
            self.view.switch("shot")
            self.main_controller.switch_to_shot(2)
        elif event.keysym == "3":
            self.view.switch("shot")
            self.main_controller.switch_to_shot(3)
        elif event.keysym == "s":
            self.main_controller.substitution()
        elif event.keysym == "t":
            self.current_game.timeout()
        elif event.keysym == "Return":
            self.current_game.change_possession()
        elif event.keysym == 'comma':
            self.current_game.momentum_meter.change_momentum(1)
        elif event.keysym == 'period':
            self.current_game.momentum_meter.change_momentum(-1)
        elif event.keysym == 'P':
            self.main_controller.save_txt_game_log()

        self.update_scoreboard_labels()
        self.update_player_labels()

    def update_player_labels(self):
        _home_lineup = self.current_game.home_team.active_roster
        _road_lineup = self.current_game.road_team.active_roster

        for i in range(5):
            self.player_frame.home_labels[i][5].config(text=f"{_home_lineup[i]}")
            self.player_frame.road_labels[i][0].config(text=f"{_road_lineup[i]}")

            self.player_frame.home_labels[i][0].config(text=f"{_home_lineup[i].minutes_played()}")
            self.player_frame.road_labels[i][1].config(text=f"{_road_lineup[i].minutes_played()}")
            self.player_frame.home_labels[i][1].config(text=f"{_home_lineup[i].points()}")
            self.player_frame.road_labels[i][2].config(text=f"{_road_lineup[i].points()}")
            self.player_frame.home_labels[i][2].config(text=f"{_home_lineup[i].rebounds()}")
            self.player_frame.road_labels[i][3].config(text=f"{_road_lineup[i].rebounds()}")
            self.player_frame.home_labels[i][3].config(text=f"{_home_lineup[i].assists}")
            self.player_frame.road_labels[i][4].config(text=f"{_road_lineup[i].assists}")
            self.player_frame.home_labels[i][4].config(text=f"{_home_lineup[i].fouls}")
            self.player_frame.road_labels[i][5].config(text=f"{_road_lineup[i].fouls}")

        self.rest_checks()

    def update_scoreboard_labels(self):
        self.scoreboard_frame.lbl_home_name.config(text=f"{self.current_game.home_team.team.name}")
        self.scoreboard_frame.lbl_road_name.config(text=f"{self.current_game.road_team.team.name}")
        self.scoreboard_frame.lbl_time.config(text=f"{self.current_game.time.display_time()}")
        self.scoreboard_frame.lbl_period.config(text=f"{self.current_game.time.period}")
        self.scoreboard_frame.lbl_current_possession.config(text=f"{self.current_game.display_current_possession()}")
        self.scoreboard_frame.lbl_home_score.config(text=f"{self.current_game.home_team.total_score()}")
        self.scoreboard_frame.lbl_road_score.config(text=f"{self.current_game.road_team.total_score()}")
        self.scoreboard_frame.lbl_home_fouls.config(text=f"Fouls: {self.current_game.home_team.fouls
        [self.current_game.time.period - 1]}")
        self.scoreboard_frame.lbl_road_fouls.config(text=f"Fouls: {self.current_game.road_team.fouls
        [self.current_game.time.period - 1]}")
        self.scoreboard_frame.lbl_home_timeouts.config(text=f"{self.current_game.home_team.timeouts}")
        self.scoreboard_frame.lbl_road_timeouts.config(text=f"{self.current_game.road_team.timeouts}")
        self.scoreboard_frame.lbl_possession_arrow.config(text=f"{self.current_game.display_possession_arrow()}")
        self.scoreboard_frame.lbl_momentum.config(text=f"{self.current_game.momentum_meter.display_scoreboard()}")

        self.foul_checks()

    def foul_checks(self):
        import setUp.Fonts as F
        if self.current_game.home_team.is_in_penalty(self.current_game.time.period):
            self.scoreboard_frame.lbl_home_fouls.config(foreground="red")
        if self.current_game.home_team.is_in_double_penalty(self.current_game.time.period):
            self.scoreboard_frame.lbl_home_fouls.config(font=F.SCOREBOARD_DOUBLE_BONUS_FONT)
        if self.current_game.road_team.is_in_penalty(self.current_game.time.period):
            self.scoreboard_frame.lbl_road_fouls.config(foreground="red")
        if self.current_game.road_team.is_in_double_penalty(self.current_game.time.period):
            self.scoreboard_frame.lbl_road_fouls.config(font=F.SCOREBOARD_DOUBLE_BONUS_FONT)

        for n in range(len(self.current_game.home_team.get_starters())):
            if self.current_game.home_team.get_starters()[n].has_player_fouled_out():
                self.player_frame.home_labels[n][4].config(foreground="red")
        for n in range(len(self.current_game.road_team.get_starters())):
            if self.current_game.road_team.get_starters()[n].has_player_fouled_out():
                self.player_frame.road_labels[n][5].config(foreground="red")

    def rest_checks(self):
        _time_remaining = self.current_game.time.get_time_remaining()
        _period = self.current_game.time.period

        for n in range(len(self.current_game.home_team.get_starters())):
            if self.current_game.home_team.get_starters()[n].is_player_fatigued(_time_remaining,_period):
                self.player_frame.home_labels[n][0].config(foreground="red")
            else:
                self.player_frame.home_labels[n][0].config(foreground="black")
        for n in range(len(self.current_game.road_team.get_starters())):
            if self.current_game.road_team.get_starters()[n].is_player_fatigued(_time_remaining,_period):
                self.player_frame.road_labels[n][1].config(foreground="red")
            else:
                self.player_frame.road_labels[n][1].config(foreground="black")

    def jump_ball(self):
        self.update_scoreboard_labels()
        self.update_player_labels()

        _home_wins_jump = messagebox.askyesno(
            "Jump Ball", "Does the home team win the jump ball?")
        self.current_game.jump_ball(_home_wins_jump)

        self.update_scoreboard_labels()
        self.scoreboard_frame.render()

    def check_half_time(self):
        if self.current_game.time.is_it_halftime:
            self.current_game.halftime()
            self.main_controller.substitution()

    def check_game_over(self):
        if self.current_game.time.is_game_over:
            if self.current_game.is_tied():
                self.current_game.time.start_overtime()
            else:
                self.main_controller.end_game()




