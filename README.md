# Проект: Игры разума

[![Build Status](https://travis-ci.org/AndrewLrrr/python-project-lvl1.svg?branch=master)](https://travis-ci.org/AndrewLrrr/python-project-lvl1)
<a href="https://codeclimate.com/github/AndrewLrrr/python-project-lvl1/maintainability"><img src="https://api.codeclimate.com/v1/badges/b67e88538d7386ddddaa/maintainability" /></a>

## Работа с проектом:
### Установка зависимостей:
```
poetry install
```
---
### Тесты:
```
make test
```
---
### Кодстайл:
```
make lint
```

## Сборка и публикация пакета:
### Установка репозитория:
```
poetry config repositories.avatara_brain_games https://test.pypi.org/legacy/
```
---
### Установка доступа к репозиторию:
```
poetry config http-basic.avatara_brain_games {login} {password}
```
---
### Сборка пакета:
```
make build
```
---
### Публикация пакета:
```
make publish
```

## Загрузка опубликованного пакета:
```
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple avatara_brain_games
```

## Запуск игр:
### Приветствие
```
brain-games
```
<a href="https://asciinema.org/a/rxvWkoD0z9seFHrz9NrVJ1OLA" target="_blank"><img src="https://asciinema.org/a/rxvWkoD0z9seFHrz9NrVJ1OLA.svg" /></a>
---
### Игра: "Проверка на четность"
```
brain-even
```
<a href="https://asciinema.org/a/56tLzftWiBPWRcrcBHJlcdQAN" target="_blank"><img src="https://asciinema.org/a/56tLzftWiBPWRcrcBHJlcdQAN.svg" /></a>
---
### Игра: "Калькулятор"
```
brain-calc
```
<a href="https://asciinema.org/a/ZNBvDRv6EvzHMVYCMMso6RwDk" target="_blank"><img src="https://asciinema.org/a/ZNBvDRv6EvzHMVYCMMso6RwDk.svg" /></a>
---
### Игра "НОД"
```
brain-gcd
```
<a href="https://asciinema.org/a/sZHb3R4JwgiFMyGG1EeWSwyXq" target="_blank"><img src="https://asciinema.org/a/sZHb3R4JwgiFMyGG1EeWSwyXq.svg" /></a>
---
### Игра "Арифметическая прогрессия"
```
brain-progression
```
<a href="https://asciinema.org/a/NWZz565AU5dbnRIhFY87ctDvL" target="_blank"><img src="https://asciinema.org/a/NWZz565AU5dbnRIhFY87ctDvL.svg" /></a>
---
### Игра "Простое ли число?"
```
brain-prime
```
<a href="https://asciinema.org/a/Xk9INmuZua0gyrXZTaI7xjhax" target="_blank"><img src="https://asciinema.org/a/Xk9INmuZua0gyrXZTaI7xjhax.svg" /></a>
