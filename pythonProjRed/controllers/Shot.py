from tkinter import IntVar, messagebox

class ShotDialogController:
    def __init__(self, prime_control, view, game):
        self.view = view
        self.current_game = game
        self.main_controller = prime_control
        self.frame = self.view.frames["shot"]

    def bind(self):
        self.view.root.bind("<Key>", self.shot_key_handler)
        self.frame.btn_cancel.config(command=self.main_controller.switch_to_game)
        self.frame.btn_ok.config(command=self.ok_clicked)
        self.frame.btn_ok.focus_set()

    def shot_key_handler(self, event):
        if event.keysym == '1':
            self.frame.var_shooter.set(0)
            self.frame.shooter_cant_assist()
        elif event.keysym == '2':
            self.frame.var_shooter.set(1)
            self.frame.shooter_cant_assist()
        elif event.keysym == '3':
            self.frame.var_shooter.set(2)
            self.frame.shooter_cant_assist()
        elif event.keysym == '4':
            self.frame.var_shooter.set(3)
            self.frame.shooter_cant_assist()
        elif event.keysym == '5':
            self.frame.var_shooter.set(4)
            self.frame.shooter_cant_assist()
        elif event.keysym == 'a':
            self.frame.var_shot_result.set(0)
            self.frame.disable_assist()
        elif event.keysym == 's':
            self.frame.var_shot_result.set(1)
            self.frame.enable_assist()
            self.frame.shooter_cant_assist()
        elif event.keysym == 'q':
            self.frame.var_shot_type.set(2)
        elif event.keysym == 'w':
            self.frame.var_shot_type.set(3)
        elif event.keysym == 'z':
            if self.frame.var_shot_result.get():
                self.frame.var_assist_pos.set(0)
            else:
                self.frame.var_block_pos.set(0)
        elif event.keysym == 'x':
            if self.frame.var_shot_result.get():
                self.frame.var_assist_pos.set(1)
            else:
                self.frame.var_block_pos.set(1)
        elif event.keysym == 'c':
            if self.frame.var_shot_result.get():
                self.frame.var_assist_pos.set(2)
            else:
                self.frame.var_block_pos.set(2)
        elif event.keysym == 'v':
            if self.frame.var_shot_result.get():
                self.frame.var_assist_pos.set(3)
            else:
                self.frame.var_block_pos.set(3)
        elif event.keysym == 'b':
            if self.frame.var_shot_result.get():
                self.frame.var_assist_pos.set(4)
            else:
                self.frame.var_block_pos.set(4)

    def ok_clicked(self):
        shot_made = self.frame.var_shot_result.get()
        shot_type = self.frame.var_shot_type.get()
        shooter = self.current_game.team_on_offense().active_roster[self.frame.var_shooter.get()]
        fouled = self.frame.var_foul.get()
        assister = blocker = None

        _assist_pos = self.frame.var_assist_pos.get()
        if _assist_pos != 5:
            assister = self.current_game.team_on_offense().active_roster[_assist_pos]

        _block_pos = self.frame.var_block_pos.get()
        if _block_pos != 5:
            blocker = self.current_game.team_on_defense().active_roster[_block_pos]

        _foul_pos = self.frame.var_fouler.get()
        fouler = self.current_game.team_on_defense().active_roster[_foul_pos]

        if shot_made and not fouled:
            self.current_game.shot_made(shot_type, shooter, assister)
            self.current_game.change_possession()
            self.reset()
            self.main_controller.switch_to_game()
        elif shot_made and fouled:
            self.current_game.shot_made(shot_type, shooter, assister)
            self.current_game.defensive_foul(fouler)
            self.main_controller.shooting_free_throws(shooter,1)
            self.reset()
        elif not shot_made and not fouled:
            self.current_game.shot_missed(shot_type, shooter, blocker)
            self.main_controller.rebound()
            self.reset()
        elif not shot_made and fouled:
            self.current_game.defensive_foul(fouler)
            self.main_controller.shooting_free_throws(shooter, shot_type)
            self.reset()

    def reset(self):
        self.frame.var_foul.set(0)
        self.frame.var_shooter.set(0)
        self.frame.var_shot_type.set(2)
        self.frame.var_shot_result.set(0)
        self.frame.var_assist_pos.set(5)
        self.frame.var_block_pos.set(5)
        self.frame.var_fouler.set(0)
        self.frame.toggle_fouls()
        self.frame.disable_assist()

    def set_shot_type(self, shot_type):
        self.frame.var_shot_type.set(shot_type)


