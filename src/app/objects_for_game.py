"""Объекты игры."""

import pygame
from random import choice

from app.config import (
    Color,
    Direction,
    DEFAULT_LENGTH,
    GAME_FIELD,
    GRID_SIZE,
    LINE_THICKNESS,
    screen,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    START_POSITION,
    X,
    Y,
)
from app.protocol import AppleP, SnakeP


class GameObject:
    """Класс описывает объекты игры."""

    def __init__(self) -> None:
        """
        Атрибуты класса:
        - body_color - цвет тела объекта,
        - line_color - цвет линий объекта.
        - line_thickness - толщина линии.
        """
        self.body_color: tuple[int, int, int] = Color.GAME_OBJECT
        self.line_color: tuple[int, int, int] = Color.LINE
        self.line_thickness: int = LINE_THICKNESS

    def draw(self, surface: pygame.Surface):
        """Метод, определяющий отрисовку объекта GameObject."""
        raise NotImplementedError()

    def _draw(self, surface: pygame.Surface, rect: pygame.Rect):
        """Отобразит переданный объект Rect."""
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(
            surface, self.line_color, rect, self.line_thickness,
        )


class Apple(GameObject, AppleP):
    """Класс описывает объект игры - Яблоко."""

    def __init__(self) -> None:
        """
        Атрибуты класса:
        - position - координаты позиции Яблока в пикселях;
        - body_color - цвет Яблока.
        """
        super().__init__()
        self.position: tuple[int, int]
        self.randomize_position()
        self.body_color: tuple[int, int, int] = Color.APPLE

    def randomize_position(
        self,
        not_here: list[tuple[int, int]] = [START_POSITION],
    ) -> None:
        """
        Метод, определяющий координаты объекта Apple.

        Параметры:
        - not_here: список с кортежами, содержащие координаты,
          где яблоко не может появится.
        """
        location_options: list[tuple[int, int]] = [
            coordinate for coordinate in GAME_FIELD
            if coordinate not in not_here
        ]
        self.position = choice(location_options)

    def draw(self, surface: pygame.Surface) -> None:
        """Метод, определяющий отрисовку объекта Apple."""
        rect = pygame.Rect(
            (self.position[X], self.position[Y]),
            (GRID_SIZE, GRID_SIZE)
        )
        self._draw(surface, rect)


class Snake(GameObject, SnakeP):
    """Класс описывает объект игры - Змейку."""

    def __init__(self) -> None:
        """
        Атрибуты класса:
        - length - длина Змейки;
        - positions - список координат ячеек Змейки;
        - direction - направление движения Змейки;
        - body_color - цвет Змейки;
        - last - последний элемент Змейки (хвост), который нужно удалять для
          имитации движения;
        - next_direction - новое направление движения Змейки.
        """
        super().__init__()
        self.length: int
        self.positions: list[tuple[int, int]]
        self.direction: tuple[int, int]
        self.reset()
        self.body_color: tuple[int, int, int] = Color.SNAKE
        self.last: tuple[int, int] | None = None
        self.next_direction: tuple[int, int] | None = None

    def reset(self) -> None:
        """Устанавливает Змейку в начальное состояние.

        Атрибуты класса:
        - length - длину,
        - positions - список координат ячеек,
        - direction - направление движения.
        """
        self.length = DEFAULT_LENGTH
        self.positions = [START_POSITION]
        self.direction = Direction.RIGHT
        screen.fill(Color.BOARD_BACKGROUND)
        pygame.display.update()

    def update_direction(self) -> None:
        """Обновит направление движения direction согласно next_direction."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """
        Имитация движения змейки.

        Добавляет в список координат сегментов змейки новую голову,
        удаляет последний элемент.
        В случае столкновения головы с телом змейки сбросит змейку к начальным
        настройкам.
        """
        # Блок для определения новых координат "головы" Змейки.
        # Деление с возвращением остатка имитирует замкнутую комнату.
        coordinates_old_head: tuple[int, int] = self.get_head_position()
        coordinates_new_head: tuple[int, int] = (
            (
                coordinates_old_head[X] + self.direction[X] * GRID_SIZE
            ) % SCREEN_WIDTH,
            (
                coordinates_old_head[Y] + self.direction[Y] * GRID_SIZE
            ) % SCREEN_HEIGHT,
        )

        if self.length == len(self.positions):
            # Обозначим где у нее хвост. Иначе не сотрется.
            # Удаляем в конце списка кончик хвоста, для имитации движения.
            self.last = self.positions.pop()
        # Добавим в начало списка новую голову, для имитации движения.
        # Строго после удаления хвоста!
        self.positions.insert(0, coordinates_new_head)

        # Проверка на столкновения головы Змейки с телом Змейки
        if coordinates_new_head in self.positions[2:]:
            self.reset()

    def draw(self, surface: pygame.Surface):
        """Метод, определяющий отрисовку объекта Snake."""
        for position in self.positions[:-1]:
            rect = (
                pygame.Rect((position[X], position[Y]), (GRID_SIZE, GRID_SIZE))
            )
            self._draw(surface, rect)

        # Отрисовка головы змейки.
        head = self.get_head_position()
        head_rect = pygame.Rect((head[X], head[Y]), (GRID_SIZE, GRID_SIZE))
        self._draw(surface, head_rect)

        # Затирание последнего сегмента. Строго после отрисовки!
        if self.last:
            last_rect = pygame.Rect(
                (self.last[X], self.last[Y]),
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, Color.BOARD_BACKGROUND, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы Змейки."""
        return self.positions[0]

    def eating(self):
        """Увеличит длину змейки."""
        self.length += 1
