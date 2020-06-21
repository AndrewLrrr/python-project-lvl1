from unittest import TestCase, main, mock
from brain_games.game_handlers import (
    even,
    calc,
    gcd,
    progression,
    prime,
)
from brain_games.game_handlers.progression import PROGRESSION_LENGTH


class GamesTestCase(TestCase):
    def assert_success(self, questions, answers, game):
        for question, answer in zip(questions, answers):
            q, a = game.generate_round()
            self.assertEqual(question, q)
            self.assertEqual(answer, a)

    def assert_fail(self, question, answer, game):
        q, a = game.generate_round()
        self.assertEqual(question, q)
        self.assertNotEqual(answer, a)

    @mock.patch('random.randint')
    def test_even_game_success(self, randint):
        questions = [10, 7, 2]
        answers = ['yes', 'no', 'yes']
        randint.side_effect = questions
        self.assert_success(questions.copy(), answers, even)

    @mock.patch('random.randint')
    def test_even_game_fail(self, randint):
        randint.return_value = 10
        self.assert_fail(10, 'no', even)

    @mock.patch('random.randint')
    @mock.patch('random.choice')
    def test_calc_game_success(self, choice, randint):
        randint.side_effect = [10, 5, 5, 10, 10, 5]
        choice.side_effect = ['+', '-', '*']
        self.assert_success(
            ['10 + 5', '5 - 10', '10 * 5'], ['15', '-5', '50'], calc)

    @mock.patch('random.randint')
    @mock.patch('random.choice')
    def test_calc_game_fail(self, choice, randint):
        randint.side_effect = [10, 5]
        choice.return_value = '+'
        self.assert_fail('10 + 5', '50', calc)

    @mock.patch('random.randint')
    def test_gcd_game_success(self, randint):
        randint.side_effect = [25, 50, 20, 15, 30, 18]
        self.assert_success(
            ['25 50', '20 15', '30 18'], ['25', '5', '6'], gcd)

    @mock.patch('random.randint')
    def test_gcd_game_fail(self, randint):
        randint.side_effect = [20, 15]
        self.assert_fail('20 15', '10', gcd)

    @mock.patch('random.randint')
    def test_progression_game_success(self, randint):
        randint.side_effect = [5, 2, PROGRESSION_LENGTH - 1]
        self.assert_success(
            ['5 7 9 11 13 15 17 19 21 ..'], ['23'], progression)

    @mock.patch('random.randint')
    def test_progression_game_fail(self, randint):
        randint.side_effect = [5, 2, 5]
        self.assert_fail('5 7 9 11 13 .. 17 19 21 23', '16', progression)

    @mock.patch('random.randint')
    def test_prime_game_success(self, randint):
        questions = [3, 7, 9, 121, 113]
        randint.side_effect = questions
        self.assert_success(
            questions.copy(), ['yes', 'yes', 'no', 'no', 'yes'], prime
        )

    @mock.patch('random.randint')
    def test_prime_game_fail(self, randint):
        randint.return_value = 5
        self.assert_fail(5, 'no', prime)


if __name__ == '__main__':
    main()
