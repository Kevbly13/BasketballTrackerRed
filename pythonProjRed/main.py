from models.BasketballGame import BasketballGame
from controllers.Main import Controller
from views import View

def main():
    view = View()
    game_controller = Controller(view)
    game_controller.start()

if __name__ == '__main__':
    main()
