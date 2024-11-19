import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
from tkinter.constants import NORMAL, DISABLED

from setUp.GameRules import Positions

class ShotDialog(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)

        self.var_foul = IntVar(self, 0)
        self.var_shooter = IntVar(self, 0)
        self.var_shot_type = IntVar(self, 2)
        self.var_shot_result = IntVar(self, 0)
        self.var_assist_pos = IntVar(self, 5)
        self.var_block_pos = IntVar(self, 5)
        self.var_fouler = IntVar(self, 0)

        self.assist_choices = []
        self.block_choices = []
        self.foul_choices = []

        self.insert_row_labels()
        self.insert_shooter_radiobuttons()
        self.insert_shot_type_radiobuttons()
        self.insert_shot_result_radiobuttons()
        self.insert_assist_radiobuttons()
        self.insert_block_radiobuttons()
        self.insert_foul_radiobuttons()

        #####  Check Button ########################################################################
        self.foul_checkbox = ttk.Checkbutton(self, text="Foul?", variable=self.var_foul,
                                             command=self.toggle_fouls, state=NORMAL)
        self.foul_checkbox.grid(row=5, column=0, padx=5, pady=10)

        ##### Buttons ##############################################################################
        button_panel = ttk.Frame(self)
        self.btn_cancel = ttk.Button(button_panel, text="Cancel")
        self.btn_ok = ttk.Button(button_panel, text="OK")

        self.btn_cancel.pack(side="left", padx=15)
        self.btn_ok.pack(side="left", padx=15)
        button_panel.grid(row=6, column=1, sticky="ew")

    ## Screen Set-up ####################################################################################
    def insert_row_labels(self):
        ttk.Label(self, text="Shooter:").grid(row=0, column=0, padx=5, pady=10)
        ttk.Label(self, text="Shot Type:").grid(row=1, column=0, padx=5, pady=10)
        ttk.Label(self, text="Result:").grid(row=2, column=0, padx=5, pady=10)
        ttk.Label(self, text="Assist:").grid(row=3, column=0, padx=5, pady=10)
        ttk.Label(self, text="Block:").grid(row=4, column=0, padx=5, pady=10)

    def insert_shooter_radiobuttons(self):
        shooter_choices = []
        shooter_panel = ttk.Frame(self)
        for n in range(len(Positions)):
            position = Positions[n]
            shooter_choices.append(ttk.Radiobutton(shooter_panel, text=position, variable=self.var_shooter, value=n,
                                                   command=self.shooter_cant_assist))

        for n in range(len(shooter_choices)):
            shooter_choices[n].pack(side="left", padx=10)
        shooter_panel.grid(row=0, column=1, sticky="ew")

    def insert_shot_type_radiobuttons(self):
        shot_type_choices = []
        shot_type_panel = ttk.Frame(self)
        shot_type_choices.append(ttk.Radiobutton(shot_type_panel, text="2-pt", variable=self.var_shot_type,
                                             value=2))
        shot_type_choices.append(ttk.Radiobutton(shot_type_panel, text="3-pt", variable=self.var_shot_type,
                                             value=3))
        for rb in shot_type_choices:
            rb.pack(side="left", padx=15)
        shot_type_panel.grid(row=1, column=1, sticky="ew")

    def insert_shot_result_radiobuttons(self):
        shot_result_choices = []
        shot_result_panel = ttk.Frame(self)
        shot_result_choices.append(ttk.Radiobutton(shot_result_panel, text="Miss", variable=self.var_shot_result,
                                               value=0, command=self.disable_assist))
        shot_result_choices.append(ttk.Radiobutton(shot_result_panel, text="Make", variable=self.var_shot_result,
                                               value=1, command=self.enable_assist))
        for rb in shot_result_choices:
            rb.pack(side="left", padx=15)
        shot_result_panel.grid(row=2, column=1, sticky="ew")

    def insert_assist_radiobuttons(self):
        assist_panel = ttk.Frame(self)
        self.assist_choices.append(ttk.Radiobutton(assist_panel, text="None", variable=self.var_assist_pos,
                                                   value=5, state=tk.DISABLED))
        for n in range(len(Positions)):
            position = Positions[n]
            self.assist_choices.append(ttk.Radiobutton(assist_panel, text=position, variable=self.var_assist_pos,
                                                       value=n, state=tk.DISABLED))

        for n in range(len(self.assist_choices)):
            self.assist_choices[n].pack(side="left", padx=10)
        assist_panel.grid(row=3, column=1, sticky="ew")

    def insert_block_radiobuttons(self):
        block_panel = ttk.Frame(self)
        self.block_choices.append(ttk.Radiobutton(block_panel, text="None", variable=self.var_block_pos,
                                                  value=5, state=tk.NORMAL))
        for n in range(len(Positions)):
            position = Positions[n]
            self.block_choices.append(ttk.Radiobutton(block_panel, text=position, variable=self.var_block_pos,
                                                      value=n, state=tk.NORMAL))

        for n in range(len(self.block_choices)):
            self.block_choices[n].pack(side="left", padx=10)
        block_panel.grid(row=4, column=1, sticky="ew")

    def insert_foul_radiobuttons(self):
        foul_panel = ttk.Frame(self)
        for n in range(len(Positions)):
            position = Positions[n]
            self.foul_choices.append(ttk.Radiobutton(foul_panel, text=position, variable=self.var_fouler,
                                                     value=n, state=tk.DISABLED))

        for n in range(len(self.foul_choices)):
            self.foul_choices[n].pack(side="left", padx=10)
        foul_panel.grid(row=5, column=1, sticky="ew")

    ######################################################################################################
    def disable_assist(self):
        for rb in self.assist_choices:
            rb.config(state=tk.DISABLED)
        for rb in self.block_choices:
            rb.config(state=tk.NORMAL)
        self.var_foul.set(0)
        for rb in self.foul_choices:
            rb.config(state=tk.DISABLED)

    def enable_assist(self):
        for rb in self.assist_choices:
            rb.config(state=tk.NORMAL)

        shooter = self.var_shooter.get()
        self.assist_choices[shooter].config(state=tk.DISABLED)

        for rb in self.block_choices:
            rb.config(state=tk.DISABLED)

    def toggle_fouls(self):
        if self.var_foul.get():
            for rb in self.block_choices:
                rb.config(state=tk.DISABLED)
            for rb in self.foul_choices:
                rb.config(state=tk.NORMAL)
        else:
            for rb in self.block_choices:
                rb.config(state=tk.NORMAL)
            for rb in self.foul_choices:
                rb.config(state=tk.DISABLED)

    def shooter_cant_assist(self):
        if self.var_shot_result.get() == 1:
            for rb in self.assist_choices:
                rb.config(state=NORMAL)
            shooter = self.var_shooter.get() + 1
            self.assist_choices[shooter].config(state=tk.DISABLED)




