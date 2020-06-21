from brain_games.cli import welcome_user, ask_name, game_handler
from brain_games.game_handlers import (
    CalcGame,
    EvenGame,
    GCDGame,
    ProgressionGame,
    AnswerKeyError,
    AnswerValueError,
    PrimeGame)

GREETING = 'Welcome to the Brain Games!'
QUESTIONS_COUNT = 3


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
    try:
        for q in game_handler(game, name):
            print(q)
    except AnswerKeyError:
        print('Error! You can only use `yes` or `no` for your answers')
    except AnswerValueError:
        print('Error! You can use only integers for your answers')


def brain_even():
    game_launcher(EvenGame(QUESTIONS_COUNT))


def brain_calc():
    game_launcher(CalcGame(QUESTIONS_COUNT))


def brain_gcd():
    game_launcher(GCDGame(QUESTIONS_COUNT))


def brain_progression():
    game_launcher(ProgressionGame(QUESTIONS_COUNT))


def brain_prime():
    game_launcher(PrimeGame(QUESTIONS_COUNT))


if __name__ == '__main__':
    main()
