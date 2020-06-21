from brain_games.game_handlers import EvenGame
from brain_games.game_launcher import game_launcher, QUESTIONS_COUNT


def main():
    game_launcher(EvenGame(QUESTIONS_COUNT))


if __name__ == '__main__':
    main()
