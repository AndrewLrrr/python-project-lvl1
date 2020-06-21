import operator
import random


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    left = random.randint(1, 10)
    right = random.randint(1, 10)
    operation__action = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    operation = random.choice(list(operation__action.keys()))
    question = f'{left} {operation} {right}'
    answer = operation__action[operation](left, right)

    return question, str(answer)
