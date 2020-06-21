from brain_games.game_handlers import CalcGame
from brain_games.game_launcher import game_launcher, QUESTIONS_COUNT


def main():
    game_launcher(CalcGame(QUESTIONS_COUNT))


if __name__ == '__main__':
    main()
