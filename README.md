# Snake
### О проекте.
Игра Змейка.
___
### Правила игры
- Змейка состоит из сегментов.
- Змейка движется в одном из четырёх направлений — вверх, вниз, влево или вправо.
- Игрок управляет направлением движения, но змейка не может остановиться или двигаться назад.
- Каждый раз, когда змейка съедает яблоко, она увеличивается в длину на один сегмент.
- В классической версии игры столкновение змейки с границей игрового поля приводит к проигрышу. Однако в некоторых вариациях змейка может проходить сквозь одну стену и появляться с противоположной стороны поля. Реализованно именно так.
- Если змейка столкнётся сама с собой — игра начинается с начала.
___
### Информация об авторах.
Акчурин Лев Ливатович.<br>
[Страничка GitHub](https://github.com/levisserena)
___
### При создании проекта использовалось:
- язык программирования [Python 3](https://www.python.org/);
- библиотека [pygame](https://github.com/pygame/pygame).
___
### Реализовано:
- простейший графический интерфейс с помощью библиотеки `pygame`;
- управление игрой с помощью библиотеки `pygame`;
- логика игры (ООП): всё описанное в `Правила игры`.
___
### Чтобы развернуть проект необходимо следующие:
- Клонировать репозиторий со своего GitHub и перейти в него в командной строке:

```
git clone git@github.com:levisserena/snake.git
```
>*Активная ссылка на репозиторий под этой кнопкой* -> [КНОПКА](https://github.com/levisserena/snake)
- Перейдите в папку с проектом:
```
cd snake
```
- Создать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux
```
python3 -m venv venv
source3 venv/bin/activate
```
- Установить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Запустите игру:

```
python main.py
```
___
### Управление.
Управление осуществляется клавишами управления курсором (срелочками).

___
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


*Каждый разработчик хотя бы раз должен написать змейку!*<br>
*Так мне сказали.*
