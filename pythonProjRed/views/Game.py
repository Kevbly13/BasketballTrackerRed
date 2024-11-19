import tkinter as tk
from views.Frames import ScoreboardFrame, PlayerFrame

class GamePage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.scoreboard_frame = ScoreboardFrame(self)
        self.player_frame = PlayerFrame(self)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.scoreboard_frame.grid(column=1, row=0)
        self.player_frame.grid(column=1, row=1)




