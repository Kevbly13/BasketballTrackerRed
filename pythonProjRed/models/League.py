import  pickle

class League:
    def __init__(self, file_string):
        self.teams = []
        self.file_name = file_string

    def load_league(self):
        with open(self.file_name, 'rb') as f:
            self.teams = pickle.load(f)


    def save_league(self):
        with open(self.file_name, 'wb') as f:
            pickle.dump(self.teams, f)
