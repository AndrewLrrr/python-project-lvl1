from unittest import TestCase, main, mock
from brain_games.cli import welcome_user, ask_name, game_handler
from brain_games.game_handlers import (
    EvenGame,
    CalcGame,
    GCDGame,
    ProgressionGame,
)


class CliTestCase(TestCase):
    @mock.patch('prompt.string')
    def test_ask_name(self, prompt):
        prompt.return_value = 'User'
        res = ask_name()
        self.assertEqual('User', res)

    @mock.patch('prompt.string')
    def test_ask_name_with_extra_spaces(self, prompt):
        prompt.return_value = ' User   '
        res = ask_name()
        self.assertEqual('User', res)

    def test_welcome_user(self):
        res = welcome_user('User')
        self.assertEqual('Hello, User!', res)

    def assert_success(self, questions, game):
        handler = game_handler(game, 'User')
        for q in questions:
            self.assertEqual(f'Question: {q}', next(handler))
            self.assertEqual('Correct!', next(handler))
        self.assertEqual('Congratulations, User!', next(handler))

    def assert_fail(self, question, game):
        handler = game_handler(game, 'User')
        self.assertEqual(f'Question: {question}', next(handler))
        self.assertEqual('Let\'s try again, User!', next(handler))

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_even_game_success(self, prompt, randint):
        questions = [10, 7, 2]
        answers = ['yes', 'no', 'yes']
        randint.side_effect = questions
        prompt.side_effect = answers
        game = EvenGame(3)
        self.assert_success(questions, game)

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_even_game_fail(self, prompt, randint):
        randint.return_value = 10
        prompt.return_value = 'no'
        game = EvenGame(3)
        self.assert_fail(10, game)

    @mock.patch('random.randint')
    @mock.patch('random.choice')
    @mock.patch('prompt.string')
    def test_calc_game_success(self, prompt, choice, randint):
        randint.side_effect = [10, 5, 5, 10, 10, 5]
        choice.side_effect = ['+', '-', '*']
        prompt.side_effect = ['15', '-5', '50']
        game = CalcGame(3)
        self.assert_success(['10 + 5', '5 - 10', '10 * 5'], game)

    @mock.patch('random.randint')
    @mock.patch('random.choice')
    @mock.patch('prompt.string')
    def test_calc_game_fail(self, prompt, choice, randint):
        randint.side_effect = [10, 5]
        choice.return_value = '+'
        prompt.return_value = '50'
        self.assert_fail('10 + 5', CalcGame(3))

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_gcd_game_success(self, prompt, randint):
        randint.side_effect = [25, 50, 20, 15, 30, 18]
        prompt.side_effect = ['25', '5', '6']
        self.assert_success(['25 50', '20 15', '30 18'], GCDGame(3))

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_gcd_game_fail(self, prompt, randint):
        randint.side_effect = [20, 15]
        prompt.return_value = '10'
        self.assert_fail('20 15', GCDGame(3))

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_progression_game_success(self, prompt, randint):
        randint.side_effect = [5, 2, 5]
        prompt.return_value = '15'
        self.assert_success(['5 7 9 11 13 .. 17 19 21 23'], ProgressionGame(1))

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_progression_game_fail(self, prompt, randint):
        randint.side_effect = [5, 2, 5]
        prompt.return_value = '16'
        self.assert_fail('5 7 9 11 13 .. 17 19 21 23', ProgressionGame(1))


if __name__ == '__main__':
    main()
