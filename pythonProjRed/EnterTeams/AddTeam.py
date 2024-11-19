from models import Team, Player
import pickle


def save():
    with open("team.pkl", mode="w") as write_file:
        # noinspection PyTypeChecker
        pickle.dump(team_list, write_file)

def print_menu():
    print("1 - Add Team")
    print("2 - Edit Team")
    print("3 - Remove Team")
    print("4 - Save/Exit")

def add_team():
    team_name = input("Team: ")
    mascot = input("Mascot: ")
    team_list.append(Team.Team(team_name, mascot))

def remove_team():
    try:
        team_choice = int(input("Choose Team to Remove: "))
        team_list.pop(team_choice)
    except (IndexError, ValueError):
        print("Could not complete task")


game_exit = False
team_list = []
with open("team.pkl", 'rb') as read_file:
    # noinspection PyTypeChecker
     team_list = pickle.load(read_file)
print(team_list)

while not game_exit:
    print_menu()
    choice = int(input("Choose Menu Option: "))
    if choice == 1:
        add_team()
    elif choice == 3:
        remove_team()
    elif choice == 4:
        save()
        game_exit = True
