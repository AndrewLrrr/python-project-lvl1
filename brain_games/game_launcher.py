from brain_games.cli import ask_name, welcome_user, game_handler
from brain_games.game_handlers import AnswerKeyError, AnswerValueError

GREETING = 'Welcome to the Brain Games!'
QUESTIONS_COUNT = 3


def game_launcher(game):
    print(GREETING)
    if game:
        print(game.greeting)
    print()
    name = ask_name()
    print(welcome_user(name))
    if game:
        print()
        try:
            for q in game_handler(game, name):
                print(q)
        except AnswerKeyError:
            print('Error! You can only use `yes` or `no` for your answers')
        except AnswerValueError:
            print('Error! You can use only integers for your answers')
