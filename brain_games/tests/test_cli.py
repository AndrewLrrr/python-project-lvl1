from unittest import TestCase, main, mock
from brain_games.cli import welcome_user, ask_name, game_handler
from brain_games.game_handlers import EvenGame


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

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_even_game_success(self, prompt, randint):
        prompt.return_value = 'yes'
        randint.return_value = 10
        game = EvenGame(3)
        handler = game_handler(game, 'User')
        for _ in range(3):
            self.assertEqual('Question: 10', next(handler))
            self.assertEqual('Correct!', next(handler))
        self.assertEqual('Congratulations, User!', next(handler))

    @mock.patch('random.randint')
    @mock.patch('prompt.string')
    def test_even_game_fail(self, prompt, randint):
        prompt.return_value = 'no'
        randint.return_value = 10
        game = EvenGame(3)
        handler = game_handler(game, 'User')
        self.assertEqual('Question: 10', next(handler))
        self.assertEqual('Let\'s try again, User!', next(handler))


if __name__ == '__main__':
    main()
