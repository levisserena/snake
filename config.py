"""Настройки игры."""
import pygame

# Константы для размеров.
SCREEN_WIDTH: int = 640
"""Ширина игрового окна в пикселях."""
SCREEN_HEIGHT: int = 480
"""Высота игрового окна в пикселях."""
GRID_SIZE: int = 15
"""Габарит ячейки, отображающий игровой элемент в пикселях."""
GRID_WIDTH: int = SCREEN_WIDTH // GRID_SIZE  # SCREEN_WIDTH_IN_GRID
"""Ширина игрового окна в ячейках."""
GRID_HEIGHT: int = SCREEN_HEIGHT // GRID_SIZE  # SCREEN_HEIGHT_IN_GRID
"""Ширина игрового окна в ячейках."""

UP: tuple[int, int] = (0, -1)
"""Определяет поведение изменения координат для движения вверх."""
DOWN: tuple[int, int] = (0, 1)
"""Определяет поведение изменения координат для движения вниз."""
LEFT: tuple[int, int] = (-1, 0)
"""Определяет поведение изменения координат для движения влево."""
RIGHT: tuple[int, int] = (1, 0)
"""Определяет поведение изменения координат для движения вправо."""

BOARD_BACKGROUND_COLOR: tuple[int, int, int] = (0, 0, 0)
"""Цвет фона игрового окна в RGB."""

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 320)
"""Настройки игрового окна."""

pygame.display.set_caption('Змейка')
"""Заголовок окна игрового поля."""

clock = pygame.time.Clock()
"""Запуск течения времени в игре."""

SPEED: int = 20
"""Скорость движения змейки."""
