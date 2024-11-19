from tkinter import Tk

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Scoreboard App")
        self.geometry("650x450")
        self.resizable(True, False)


        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)