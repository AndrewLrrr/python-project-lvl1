import prompt


GREETING = 'Welcome to the Brain Games!'
EVEN_GAME_TRIES = 3


def ask_name():
    name = prompt.string('May I have your name? ')
    return name.strip()


def welcome_user(name):
    return f'Hello, {name}!'


def game_handler(game, name):
    game = game.run()
    try:
        while True:
            yield next(game)
    except StopIteration as e:
        yield f'{e.value}, {name}!'
