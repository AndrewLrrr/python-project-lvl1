import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_round():
    question = random.randint(1, 150)
    answer = 'yes' if is_prime(question) else 'no'

    return question, answer
