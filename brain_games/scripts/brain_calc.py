from brain_games.game_handlers import CalcGame
from brain_games.scripts.game_launcher import game_launcher


def main():
    game = CalcGame(3)
    try:
        game_launcher(game)
    except ValueError:
        print('Error! You can use only integers for your answers')


if __name__ == '__main__':
    main()
