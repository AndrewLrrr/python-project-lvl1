import prompt


ROUNDS_COUNT = 3


def game_launcher(game, rounds_count=ROUNDS_COUNT):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    print()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print()
    for _ in range(rounds_count):
        question, answer = game.generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
