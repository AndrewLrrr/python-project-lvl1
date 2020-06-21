from brain_games.cli import GREETING, welcome_user, game_handler, ask_name


def game_launcher(game):
    print(GREETING)
    print(game.greeting)
    print()
    name = ask_name()
    print(welcome_user(name))
    print()
    for q in game_handler(game, name):
        print(q)
