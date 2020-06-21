import prompt


def ask_name():
    name = prompt.string('May I have your name? ')
    return name.strip()


def welcome_user(name):
    return f'Hello, {name}!'


def game_handler(game, name):
    game = game.run()
    try:
        yield next(game)
        while True:
            answer = prompt.string('Your answer: ')
            yield game.send(answer)
            yield next(game)
    except StopIteration as e:
        yield f'{e.value}, {name}!'
