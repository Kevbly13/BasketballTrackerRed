import tkinter as tk
from tkinter import ttk, Label
from tkinter import IntVar
from tkinter.constants import NORMAL, DISABLED

from setUp.GameRules import Positions

class ReboundDialog(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        import setUp.Fonts as F

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.var_rebounder = IntVar(self,0)


        ttk.Label(self, text="Defense", font=F.SCOREBOARD_TEAM_FONT).grid(row=0,column=0,padx=10,pady=10)
        ttk.Label(self, text="Offense", font=F.SCOREBOARD_TEAM_FONT).grid(row=0, column=1, padx=10, pady=10)

        self.offensive_panel = ttk.Frame(self)
        self.defensive_panel = ttk.Frame(self)
        self.insert_rebound_radiobuttons()

        self.btn_foul = ttk.Button(self,text="Foul")
        self.btn_jump_ball = ttk.Button(self,text="Jump Ball")
        self.btn_rebound = ttk.Button(self, text="Rebound")
        self.btn_foul.grid(row=2,column=0,columnspan=2)
        self.btn_jump_ball.grid(row=3, column=0, columnspan=2)
        self.btn_rebound.grid(row=4,column=0,columnspan=2)


    def insert_rebound_radiobuttons(self):
        def_rebound_choices = []
        off_rebound_choices = []

        for n in range(len(Positions)):
            position = Positions[n]
            def_rebound_choices.append(ttk.Radiobutton(self.defensive_panel, text=position,
                                                        variable=self.var_rebounder, value=n))
            off_rebound_choices.append(ttk.Radiobutton(self.offensive_panel, text=position,
                                                        variable=self.var_rebounder, value=n+6))
        def_rebound_choices.append(ttk.Radiobutton(self.defensive_panel, text="Team",
                                                   variable=self.var_rebounder, value=5))
        off_rebound_choices.append(ttk.Radiobutton(self.offensive_panel, text="Team",
                                                   variable=self.var_rebounder, value=11))

        for rb in def_rebound_choices:
            rb.pack()
        for rb in off_rebound_choices:
            rb.pack()

        self.defensive_panel.grid(row=1,column=0)
        self.offensive_panel.grid(row=1,column=1)








