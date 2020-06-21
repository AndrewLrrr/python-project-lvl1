import random

import prompt


class AnswerKeyError(Exception):
    pass


class AnswerValueError(Exception):
    pass


class GameHandler:
    greeting = None
    success_message = 'Congratulations'
    error_message = 'Let\'s try again'

    def __init__(self, tries):
        self._tries = tries

    @classmethod
    def _gen_question(cls):
        raise NotImplementedError

    @classmethod
    def _handle_answer(cls, question, answer):
        raise NotImplementedError

    def run(self):
        for _ in range(self._tries):
            question = self._gen_question()
            yield f'Question: {question}'
            answer = prompt.string('Your answer: ')
            try:
                if not self._handle_answer(question, answer):
                    return self.error_message
            except KeyError:
                raise AnswerKeyError
            except ValueError:
                raise AnswerValueError
            yield 'Correct!'
        return self.success_message


class EvenGame(GameHandler):
    greeting = 'Answer "yes" if number even otherwise answer "no".'

    @classmethod
    def _gen_question(cls):
        return random.randint(1, 100)

    @classmethod
    def _handle_answer(cls, question, answer):
        answer_map = {
            'yes': 0,
            'no': 1,
        }
        return question % 2 == answer_map[answer]


class CalcGame(GameHandler):
    greeting = 'What is the result of the expression?'
    allowed_operations = ('*', '+', '-')

    @classmethod
    def _mul(cls, left, right):
        return left * right

    @classmethod
    def _add(cls, left, right):
        return left + right

    @classmethod
    def _sub(cls, left, right):
        return left - right

    def _calc_str(self, val):
        op_map = {
            '+': '_add',
            '-': '_sub',
            '*': '_mul',
        }
        left, op, right = val.split()
        return getattr(self, op_map[op])(int(left), int(right))

    def _gen_question(self):
        left = str(random.randint(1, 10))
        right = str(random.randint(1, 10))
        op = random.choice(self.allowed_operations)
        return f'{left} {op} {right}'

    def _handle_answer(self, question, answer):
        return self._calc_str(question) == int(answer)


class GCDGame(GameHandler):
    greeting = 'Find the greatest common divisor of given numbers.'

    @classmethod
    def _gen_question(cls):
        x = random.randint(2, 100)
        y = random.randint(2, 100)
        return f'{x} {y}'

    @classmethod
    def _handle_answer(cls, question, answer):
        x, y = [int(v) for v in question.split()]

        def gcb(a, b):
            if a == 0:
                return b
            if b == 0:
                return a
            return gcb(a % b, b) if a > b else gcb(a, b % a)

        return gcb(x, y) == int(answer)


class ProgressionGame(GameHandler):
    greeting = 'What number is missing in the progression?'
    progression_length = 10
    skip_item = '..'

    def __init__(self, tries):
        super().__init__(tries)
        self._num = None
        self._step = None
        self._skip_index = None

    def _gen_question(self):
        self._num = random.randint(1, 100)
        self._step = random.randint(2, 100)
        self._skip_index = random.randint(0, 9)
        num = self._num
        progression = []
        for i in range(self.progression_length):
            if i == self._skip_index:
                progression.append(self.skip_item)
            else:
                progression.append(str(num))
            num += self._step
        return ' '.join(progression)

    def _handle_answer(self, question, answer):
        num = self._num
        for _ in range(self._skip_index):
            num += self._step
        return num == int(answer)


class PrimeGame(GameHandler):
    greeting = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    def _gen_question(self):
        return random.randint(1, 150)

    def _handle_answer(self, question, answer):
        answer_map = {
            'yes': True,
            'no': False,
        }
        n = question // 2
        is_prime = True
        while n > 1:
            if question % n == 0:
                is_prime = False
                break
            n -= 1
        return is_prime == answer_map[answer]
