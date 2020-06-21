from brain_games.cli import GREETING, welcome_user, game_handler, ask_name
from brain_games.game_handlers import EvenGame


def main():
    game = EvenGame(3)
    print(GREETING)
    print(game.greeting)
    print()
    name = ask_name()
    print(welcome_user(name))
    print()
    try:
        for q in game_handler(game, name):
            print(q)
    except KeyError:
        print('Error! You can only use `yes` or `no` for your answers')


if __name__ == '__main__':
    main()
