"""Объекты игры."""

import pygame
from random import choice

from config import (
    Color,
    Direction,
    DEFAULT_LENGTH,
    GAME_FIELD,
    GRID_SIZE,
    screen,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    START_POSITION,
)
from protocol import AppleP, SnakeP


class GameObject:
    """Класс описывает объекты игры."""

    def __init__(self) -> None:
        """
        Конструктор класса GameObject.

        - body_color - цвет тела объекта,
        - line_color - цвет линий объекта.
        """
        self.body_color: tuple[int, int, int] = Color.GAME_OBJECT
        self.line_color: tuple[int, int, int] = Color.LINE

    def draw(self, surface):
        """Метод, определяющий отрисовку объекта GameObject."""
        raise NotImplementedError()


class Apple(GameObject):
    """Класс описывает объект игры - Яблоко."""

    def __init__(self) -> None:
        """
        Конструктор класса Apple.

        - position - координаты позиции Яблока в пикселях;
        - body_color - цвет Яблока.
        """
        super().__init__()
        self.position: tuple[int, int]
        self.randomize_position()
        self.body_color: tuple[int, int, int] = Color.APPLE

    def randomize_position(self, snake: SnakeP | None = None) -> None:
        """
        Метод, определяющий координаты объекта Apple.

        Может появится где угодно, кроме как в теле Змейки.
        """
        location_options: list[tuple[int, int]] = (
            [coordinate for coordinate in GAME_FIELD if coordinate != START_POSITION]
            if not snake
            else [coordinate for coordinate in GAME_FIELD if coordinate not in snake.positions]
        )
        self.position = choice(location_options)

    def draw(self, surface) -> None:
        """Метод, определяющий отрисовку объекта Apple."""
        rect = pygame.Rect(
            (self.position[0], self.position[1]),
            (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, self.line_color, rect, 1)


class Snake(GameObject):
    """Класс описывает объект игры - Змейку."""

    def __init__(self) -> None:
        """
        Конструктор класса Snake.

        - length - длина Змейки;
        - positions - список координат ячеек Змейки;
        - direction - направление движения Змейки;
        - body_color - цвет Змейки;
        - last - последний элемент Змейки (хвост), который нужно удалять для имитации движения;
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
        """Метод объекта класса Snake.

        Устанавливает Змейку в начальное состояние:
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
        """Метод объекта класса Snake.

        Обновит направление движения direction согласно next_direction.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Метод экземпляра класса Snake.

        Обновляет позицию Змейки,
        считывая её рост, проверяя столкновения.
        """
        # Блок для определения новых координат "головы" Змейки.
        # Деление с возвращением остатка имитирует замкнутую комнату.
        coordinates_old_head: tuple[int, int] = self.get_head_position()
        coordinates_new_head: tuple[int, int] = (
            (coordinates_old_head[0] + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH,
            (coordinates_old_head[1] + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT,
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

    def draw(self, surface):
        """Метод, определяющий отрисовку объекта Snake."""
        for position in self.positions[:-1]:
            rect = (
                pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            )
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, (93, 216, 228), rect, 1)

        # Отрисовка головы змейки.
        head = self.get_head_position()
        head_rect = pygame.Rect((head[0], head[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, (93, 216, 228), head_rect, 1)

        # Затирание последнего сегмента. Строго после отрисовки!
        if self.last:
            last_rect = pygame.Rect(
                (self.last[0], self.last[1]),
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, Color.BOARD_BACKGROUND, last_rect)

    def get_head_position(self):
        """Метод объекта класса Snake.

        Возвращает позицию головы Змейки.
        """
        return self.positions[0]

    def eating(self, apple: AppleP):
        """Метод объекта класса Snake.

        Проверяет позицию головы Змейки и Яблока.
        Если они совпадают, происходит процесс поедания:
        Змейка растет, Яблоко появляется в другом месте.
        """
        if self.get_head_position() == apple.position:
            self.length += 1
            apple.randomize_position(self)
