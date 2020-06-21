from brain_games.cli import welcome_user, ask_name, game_handler
from brain_games.game_handlers import CalcGame, EvenGame

GREETING = 'Welcome to the Brain Games!'
DEFAULT_GAME_TRIES = 3


def main():
    print(GREETING)
    print()
    name = ask_name()
    print(welcome_user(name))


def game_launcher(game):
    print(GREETING)
    print(game.greeting)
    print()
    name = ask_name()
    print(welcome_user(name))
    print()
    for q in game_handler(game, name):
        print(q)


def brain_even():
    try:
        game_launcher(EvenGame(DEFAULT_GAME_TRIES))
    except ValueError:
        print('Error! You can use only integers for your answers')


def brain_calc():
    try:
        game_launcher(CalcGame(DEFAULT_GAME_TRIES))
    except ValueError:
        print('Error! You can use only integers for your answers')


if __name__ == '__main__':
    main()
