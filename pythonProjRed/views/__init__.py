from views.Shot import ShotDialog
from views.Frames import ScoreboardFrame, PlayerFrame
from views.Root import Root
from views.Intro import IntroPage
from views.Game import GamePage
from views.EndPage import EndPage
from views.Rebound import ReboundDialog
from views.StartingLineup import StartingLineup
from views.Substitution import SubstitutionDialog
from views.Turnover import TurnoverDialog


class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}

        self.add_frame(IntroPage, "intro")
        self.add_frame(GamePage, "game")
        self.add_frame(EndPage, "end")
        self.add_frame(ShotDialog, "shot")
        self.add_frame(ReboundDialog, "rebound")
        self.add_frame(TurnoverDialog, "turnover")
        self.add_frame(SubstitutionDialog, "subs")
        self.add_frame(StartingLineup, "starters")


    def add_frame(self, frame, name):
        self.frames[name] = frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        frame = self.frames[name]
        frame.tkraise()
        self.root.focus()

    def start_mainloop(self):
        self.root.mainloop()


