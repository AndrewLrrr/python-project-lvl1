lint:
	poetry run flake8 brain_games

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish -r avatara_brain_games
