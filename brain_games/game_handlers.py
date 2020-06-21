import random

import prompt


class GameHandler:
    greeting = None
    success_message = None
    error_message = None

    def __init__(self, tries):
        self._tries = tries

    @classmethod
    def _get_question(cls):
        raise NotImplementedError

    @classmethod
    def _handle_answer(cls, question, answer):
        raise NotImplementedError

    def run(self):
        for _ in range(self._tries):
            question = self._get_question()
            yield f'Question: {question}'
            answer = prompt.string('Your answer: ')
            if not self._handle_answer(question, answer):
                return self.error_message
            yield 'Correct!'
        return self.success_message


class EvenGame(GameHandler):
    greeting = 'Answer "yes" if number even otherwise answer "no".'
    success_message = 'Congratulations'
    error_message = 'Let\'s try again'

    @classmethod
    def _get_question(cls):
        return random.randint(1, 100)

    @classmethod
    def _handle_answer(cls, question, answer):
        answer_map = {
            'yes': 0,
            'no': 1,
        }
        return bool(question % 2 == answer_map[answer])
