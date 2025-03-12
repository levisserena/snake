"""
Настройки игры.

Поле отрисовывается в пиксилях.
Поле абстрактно делится на квадратики с длиной стороны GRID_SIZE.
Левый верхний угол таких квадратиков считается точкой координат.
"""

import pygame
from dataclasses import dataclass

# Константы для размеров.
GRID_SIZE: int = 16
"""Габарит ячейки, отображающий игровой элемент в пикселях."""
SCREEN_WIDTH_IN_GRID: int = 42
"""Ширина игрового окна в ячейках."""
SCREEN_HEIGHT_IN_GRID: int = 32
"""Ширина игрового окна в ячейках."""
SCREEN_WIDTH: int = SCREEN_WIDTH_IN_GRID * GRID_SIZE
"""Ширина игрового окна в пикселях."""
SCREEN_HEIGHT: int = SCREEN_HEIGHT_IN_GRID * GRID_SIZE
"""Высота игрового окна в пикселях."""
GAME_FIELD: list[tuple[int, int]] = [
    (x * GRID_SIZE, y * GRID_SIZE)
    for x in range(SCREEN_WIDTH_IN_GRID) for y in range(SCREEN_HEIGHT_IN_GRID)
]
"""Генератор для определения всех координат игрового поля."""

START_POSITION: tuple[int, int] = (
    SCREEN_WIDTH_IN_GRID // 2 * GRID_SIZE,
    SCREEN_HEIGHT_IN_GRID // 2 * GRID_SIZE,
)
"""Стартовая позиция игровых объектов по умолчанию."""
DEFAULT_LENGTH: int = 1
"""Длина Змейки по умолчанию."""


@dataclass
class Direction:
    """Определяет поведение изменения координат для движения Змейки."""

    UP: tuple[int, int] = (0, -1)
    DOWN: tuple[int, int] = (0, 1)
    LEFT: tuple[int, int] = (-1, 0)
    RIGHT: tuple[int, int] = (1, 0)


@dataclass
class Color:
    """Цвета, используемые в игре."""

    BOARD_BACKGROUND: tuple[int, int, int] = (0, 0, 0)
    """Цвет фона игрового окна в RGB."""
    GAME_OBJECT: tuple[int, int, int] = (0, 0, 0)
    """Цвет игровых объектов по умолчанию в RGB."""
    APPLE: tuple[int, int, int] = (255, 0, 0)
    """Цвет Яблока в RGB."""
    SNAKE: tuple[int, int, int] = (0, 255, 0)
    """Цвет Змейки в RGB."""
    LINE: tuple[int, int, int] = (93, 216, 228)
    """Цвет линий в RGB."""


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 320)
"""Настройки игрового окна."""

pygame.display.set_caption('Змейка')
"""Заголовок окна игрового поля."""

clock = pygame.time.Clock()
"""Запуск течения времени в игре."""

SPEED: int = 20
"""Скорость движения Змейки."""
