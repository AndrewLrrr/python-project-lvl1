import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate_round():
    question = random.randint(1, 100)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
