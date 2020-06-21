from brain_games.cli import GREETING, welcome_user, ask_name


def main():
    print(GREETING)
    print()
    name = ask_name()
    print(welcome_user(name))


if __name__ == '__main__':
    main()
