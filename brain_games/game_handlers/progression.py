import random


DESCRIPTION = 'What number is missing in the progression?'
SKIP_ITEM = '..'
PROGRESSION_LENGTH = 10


def generate_round():
    start = random.randint(1, 100)
    step = random.randint(2, 10)
    skip_index = random.randint(0, PROGRESSION_LENGTH - 1)

    progression = []
    for i in range(PROGRESSION_LENGTH):
        progression.append(start + step * i)

    progression[skip_index] = SKIP_ITEM

    question = ' '.join(str(i) for i in progression)
    answer = start + step * skip_index

    return question, str(answer)
