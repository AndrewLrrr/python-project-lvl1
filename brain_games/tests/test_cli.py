from unittest import TestCase, main, mock
from brain_games.cli import welcome_user


class CliTestCase(TestCase):
    @mock.patch('prompt.string')
    def test_welcome_user(self, prompt):
        prompt.return_value = 'User'
        res = welcome_user()
        self.assertEqual('Hello, User!', res)


if __name__ == '__main__':
    main()
