import tkinter as tk
from tkinter import ttk
from tkinter import IntVar

from setUp.GameRules import Positions

class TurnoverDialog(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.var_turnover_type = IntVar(self,0)
        self.var_offender = IntVar(self,0)
        self.var_defender = IntVar(self, 0)

        self.offender_choices = []
        self.defender_choices = []

        self.offender_panel = ttk.Frame(self)
        self.defender_panel = ttk.Frame(self)
        self.insert_turnover_radiobuttons()
        self.insert_position_radiobuttons()

        self.btn_cancel = ttk.Button(self,text="Cancel")
        self.btn_cancel.grid(row=5,column=0,columnspan=2, pady=10)
        self.btn_ok = ttk.Button(self, text="OK")
        self.btn_ok.grid(row=6,column=0,columnspan=2, pady=10)

    def insert_turnover_radiobuttons(self):
        import setUp.Fonts as F
        ttk.Label(self, text="Turnover Type", font=F.SCOREBOARD_TEAM_FONT).grid(row=0, column=0)
        ttk.Radiobutton(self, text="Turnover", variable=self.var_turnover_type,
                        value=0, command=self.disable_defender_choices).grid(row=1, column=0, padx=10, pady=10)
        ttk.Radiobutton(self, text="Steal", variable=self.var_turnover_type,
                        value=1, command=self.enable_defender_choices).grid(row=2, column=0, padx=10, pady=10)
        ttk.Radiobutton(self, text="Defensive Foul", variable=self.var_turnover_type,
                        value=2, command=self.enable_defender_choices).grid(row=3, column=0, padx=10, pady=10)
        ttk.Radiobutton(self, text="Offensive Foul", variable=self.var_turnover_type,
                        value=3, command=self.disable_defender_choices).grid(row=4, column=0, padx=10, pady=10)

    def insert_position_radiobuttons(self):
        import setUp.Fonts as F
        ttk.Label(self,text="Offensive Player", font=F.SCOREBOARD_TEAM_FONT).grid(row=0, column=1)
        ttk.Label(self, text="Defensive Player", font=F.SCOREBOARD_TEAM_FONT).grid(row=2, column=1)

        for n in range(len(Positions)):
            self.offender_choices.append(ttk.Radiobutton(self.offender_panel, variable=self.var_offender,
                                                    text=f"{Positions[n]}", value=n))
            self.defender_choices.append(ttk.Radiobutton(self.defender_panel, variable=self.var_defender,
                                                         text=f"{Positions[n]}", value=n, state=tk.DISABLED))
        for rb in self.offender_choices:
            rb.pack(side=tk.LEFT)
        for rb in self.defender_choices:
            rb.pack(side=tk.LEFT)

        self.offender_panel.grid(row=1, column=1, padx=10, pady=10)
        self.defender_panel.grid(row=3, column=1, padx=10, pady=10)

    def disable_defender_choices(self):
        for rb in self.defender_choices:
            rb.config(state = tk.DISABLED)

    def enable_defender_choices(self):
        for rb in self.defender_choices:
            rb.config(state = tk.NORMAL)


