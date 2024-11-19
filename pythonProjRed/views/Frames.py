import tkinter as tk
from tkinter import ttk, Label
from tkinter.constants import SOLID

from setUp.GameRules import Positions


class ScoreboardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        import setUp.Fonts as F


        self.lbl_home_name = Label(self, text=f"team", font=F.SCOREBOARD_TEAM_FONT,
                                   padx=10)
        self.lbl_time = Label(self, font=F.SCOREBOARD_TIME_FONT, borderwidth=2, relief=SOLID, padx=15)
        self.lbl_road_name = Label(self, text=f"team", font=F.SCOREBOARD_TEAM_FONT,
                                   padx=10)

        self.lbl_home_score = Label(self, font=F.SCOREBOARD_SCORE_FONT, fg="Red")
        self.lbl_home_timeouts = Label(self)
        self.lbl_period = Label(self, font=F.SCOREBOARD_BASE_FONT)
        self.lbl_road_timeouts = Label(self)
        self.lbl_road_score = Label(self, font=F.SCOREBOARD_SCORE_FONT, fg="Red")

        self.lbl_home_fouls = Label(self, font=F.SCOREBOARD_FOUL_FONT)
        self.lbl_momentum = Label(self, font=F.SCOREBOARD_BASE_FONT)
        self.lbl_road_fouls = Label(self, font=F.SCOREBOARD_FOUL_FONT)

        self.lbl_current_possession = Label(self,font=F.SCOREBOARD_FOUL_FONT)
        self.lbl_possession_arrow = Label(self)

        self.render()

    def render(self):
        self.lbl_home_name.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.lbl_time.grid(row=0, column=2, sticky="nsew")
        self.lbl_road_name.grid(row=0, column=3, columnspan=2, sticky="nsew")

        self.lbl_home_score.grid(row=1, column=0, sticky="ew")
        self.lbl_home_timeouts.grid(row=1, column=1, sticky="nsew")
        self.lbl_period.grid(row=1, column=2, sticky="ew")
        self.lbl_road_timeouts.grid(row=1, column=3, sticky="nsew")
        self.lbl_road_score.grid(row=1, column=4, sticky="ew")

        self.lbl_home_fouls.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.lbl_momentum.grid(row=2, column=2, sticky="ew")
        self.lbl_road_fouls.grid(row=2, column=3, columnspan=2, sticky="ew")

        self.lbl_current_possession.grid(row=3, column=0, columnspan=3, sticky="ew")
        self.lbl_possession_arrow.grid(row=3, column=3, columnspan=2, sticky="ew")




class PlayerFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.home_players_panel = ttk.Frame(self)
        self.road_players_panel = ttk.Frame(self)
        self.positions_panel = ttk.Frame(self)

        self.stat_categories = 6
        self.number_of_players = 5
        self.home_labels = []
        self.road_labels = []

        self.set_position_labels()
        self.set_player_grids()

        self.home_players_panel.grid(column=0, row=0)
        self.positions_panel.grid(column=1, row=0)
        self.road_players_panel.grid(column=2, row=0)

    def set_position_labels(self):
        import setUp.Fonts as F
        position_labels = []

        for n in range(len(Positions)):
            _new_label = ttk.Label(self.positions_panel, text=f"{Positions[n]}", font=F.PLAYER_POSITION_FONT)
            position_labels.append(_new_label)

        for n in range(len(position_labels)):
            position_labels[n].grid(row=n, column=0, padx=5, pady=5)

    def set_player_grids(self):
        import setUp.Fonts as F
        for n in range(self.number_of_players):
            home_row = []
            road_row = []
            for m in range(self.stat_categories):
                _home_label = ttk.Label(self.home_players_panel, text="0", font=F.PLAYER_BASE_FONT)
                _home_label.grid(row=n, column=m, padx=3, pady=5, sticky="e")
                home_row.append(_home_label)

                _road_label = ttk.Label(self.road_players_panel, text="0", font=F.PLAYER_BASE_FONT)
                _road_label.grid(row=n, column=m, padx=3, pady=5, sticky="w")
                road_row.append(_road_label)

            self.home_labels.append(home_row)
            self.road_labels.append(road_row)



