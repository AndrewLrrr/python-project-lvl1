from brain_games.game_handlers import GCDGame
from brain_games.game_launcher import game_launcher, QUESTIONS_COUNT


def main():
    game_launcher(GCDGame(QUESTIONS_COUNT))


if __name__ == '__main__':
    main()
