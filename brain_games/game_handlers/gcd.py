import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    x = random.randint(2, 100)
    y = random.randint(2, 100)

    question = f'{x} {y}'
    answer = math.gcd(x, y)

    return question, str(answer)
