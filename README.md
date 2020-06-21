# Проект: Игры разума

[![Build Status](https://travis-ci.org/AndrewLrrr/python-project-lvl1.svg?branch=master)](https://travis-ci.org/AndrewLrrr/python-project-lvl1)
<a href="https://codeclimate.com/github/AndrewLrrr/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/b67e88538d7386ddddaa/maintainability" /></a>

## Установка пакета:
```
poetry install
```

## Тесты:
```
make test
```

## Кодстайл:
```
make lint
```

## Установка репозитория:
```
poetry config repositories.avatara_brain_games https://test.pypi.org/legacy/
```

## Установка доступа к репозиторию:
```
poetry config http-basic.avatara_brain_games {login} {password}
```

## Сборка пакета:
```
make build
```

## Публикация пакета:
```
make publish
```

## Запуск игр:
### Приветствие
```
poetry run brain-games
```
### Игра: "Проверка на четность"
```
poetry run brain-even
```
### Игра: "Калькулятор"
```
poetry run brain-calc
```
### Игра "НОД"
```
poetry run brain-gcd
```
### Игра "Арифметическая прогрессия"
```
poetry run brain-progression
```
### Игра "Простое ли число?"
```
poetry run brain-prime
```
