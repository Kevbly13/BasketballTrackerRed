from tkinter import ttk, StringVar, IntVar


class IntroPage(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        from setUp import Fonts

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        label = ttk.Label(self, text="Welcome to the Game", font=Fonts.SCOREBOARD_TEAM_FONT)
        label.grid(row=0,column=0,columnspan=2,pady=10)

        label = ttk.Label(self, text="Home", font=Fonts.SCOREBOARD_BASE_FONT)
        label.grid(row=1, column=0)
        label = ttk.Label(self, text="Road", font=Fonts.SCOREBOARD_BASE_FONT)
        label.grid(row=1, column=1)

        self.var_home_selection = StringVar()
        self.var_road_selection = StringVar()
        self.var_game_number = IntVar()

        self.home_team_cb = ttk.Combobox(self,textvariable=self.var_home_selection,state='readonly')
        self.home_team_cb.grid(row=2,column=0,columnspan=1,padx=10)
        self.road_team_cb = ttk.Combobox(self,textvariable=self.var_road_selection, state='readonly')
        self.road_team_cb.grid(row=2, column=1, columnspan=1, padx=10)

        label = ttk.Label(self, text="Game Number: ",font=Fonts.SCOREBOARD_SMALL_FONT)
        label.grid(row=3, column=0, pady=5, sticky="e")
        self.game_number_entry = ttk.Entry(self,textvariable=self.var_game_number,width=10)
        self.game_number_entry.grid(row=3, column=1, padx=2, sticky="w")

        self.continue_btn  = ttk.Button(self, text="Continue")
        self.continue_btn.grid(row=4,column=0,columnspan=2,pady=10)