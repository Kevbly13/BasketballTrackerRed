from tkinter import ttk


class EndPage(ttk.Frame):
    def __init__(self, parent):
        import setUp.Fonts as F
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Game Over", font=F.SCOREBOARD_SCORE_FONT)
        label.grid(row=0,column=0,columnspan=2, pady=10)

        self.lbl_home_team = ttk.Label(self, font=F.SCOREBOARD_TEAM_FONT)
        self.lbl_home_team.grid(row=1, column=0, padx=10, pady=5)
        self.lbl_road_team = ttk.Label(self, font=F.SCOREBOARD_TEAM_FONT)
        self.lbl_road_team.grid(row=1, column=1, padx=10, pady=5)
        self.lbl_home_team_mascot = ttk.Label(self, font=F.SCOREBOARD_TEAM_FONT)
        self.lbl_home_team_mascot.grid(row=2, column=0, pady=5)
        self.lbl_road_team_mascot = ttk.Label(self, font=F.SCOREBOARD_TEAM_FONT)
        self.lbl_road_team_mascot.grid(row=2, column=1, pady=5)
        self.lbl_home_team_score = ttk.Label(self, font=F.SCOREBOARD_SCORE_FONT)
        self.lbl_home_team_score.grid(row=3, column=0, pady=5)
        self.lbl_road_team_score = ttk.Label(self, font=F.SCOREBOARD_SCORE_FONT)
        self.lbl_road_team_score.grid(row=3, column=1, pady=5)


        self.button  = ttk.Button(self, text="Continue",)
        self.button.grid(row=4,column=0,columnspan=2, pady=10)