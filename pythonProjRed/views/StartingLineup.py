import tkinter as tk
from tkinter import ttk, StringVar

class StartingLineup(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        import setUp.Fonts as F

        ##### Grid Setup ############################################################
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        ##### Team Labels ############################################################
        self.lbl_home_team = ttk.Label(self, font=F.SCOREBOARD_TEAM_FONT)
        self.lbl_home_team.grid(row=0,column=0,pady=5)
        self.lbl_road_team = ttk.Label(self, font=F.SCOREBOARD_TEAM_FONT)
        self.lbl_road_team.grid(row=0,column=1,pady=5)

        ##### Combo Boxes ############################################################
        self.home_comboboxes = []
        self.road_comboboxes = []
        self.var_choice_home = []
        self.var_choice_road = []
        self.set_dropdowns()

        for n in range(5):
            self.home_comboboxes[n].grid(row=n+1, column=0, pady=5)
            self.road_comboboxes[n].grid(row=n+1, column=1, pady=5)

        self.btn_continue = ttk.Button(self,text="Continue")
        self.btn_continue.grid(row=6, column=0, columnspan=2, pady=10)

    def set_dropdowns(self) -> None:  # Loop to create combo_boxes and choices
        for j in range(5):
            _new_var1 = StringVar()
            _new_var2 = StringVar()
            self.var_choice_home.append(_new_var1)
            self.var_choice_road.append(_new_var2)

        for n in range(5):
            _new_combo1 = ttk.Combobox(self, textvariable=self.var_choice_home[n], state='readonly')
            _new_combo2 = ttk.Combobox(self, textvariable=self.var_choice_road[n], state='readonly')
            self.home_comboboxes.append(_new_combo1)
            self.road_comboboxes.append(_new_combo2)

