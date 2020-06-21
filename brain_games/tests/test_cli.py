from unittest import TestCase, main, mock
from brain_games.cli import welcome_user, ask_name


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


if __name__ == '__main__':
    main()
