from models import Team, Player
import csv
import pickle

from models.League import League

big_ten_teams = []
big_ten_players = []

with open("bigten.pickle", 'rb') as f:
    big_ten_teams = pickle.load(f)


with open("Rosters/bigten.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        _new_player = Player.Player(row[0],row[1])
        _injury = int(row[2])
        _first = int(row[3])
        _second = int(row[4])
        _new_player.enter_rest(_injury, _first, _second)
        for team in big_ten_teams:
            if row[5] == team.name:
                team.roster.append(_new_player)





for team in big_ten_teams:
    print(f"{team.name} {team.mascot}")
    for player in team.roster:
        print(f"--{player}")

new_league = League("bigtenPlayers.pickle")
new_league.teams = big_ten_teams

with open("bigtenPlayers.pickle", 'wb') as f:
    pickle.dump(new_league, f)




