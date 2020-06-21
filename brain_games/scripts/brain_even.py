from brain_games.game_handlers import EvenGame
from brain_games.scripts.game_launcher import game_launcher


def main():
    game = EvenGame(3)
    try:
        game_launcher(game)
    except KeyError:
        print('Error! You can only use `yes` or `no` for your answers')


if __name__ == '__main__':
    main()
