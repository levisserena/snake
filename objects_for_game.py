"""Объекты игры."""
import pygame
from random import randint

from config import (
    BOARD_BACKGROUND_COLOR,
    GRID_HEIGHT,
    GRID_SIZE,
    GRID_WIDTH,
    RIGHT,
    screen,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class GameObject:
    """Класс описывает объекты игры."""

    def __init__(self) -> None:
        """Конструктор класса GameObject."""
        self.position: tuple[int, int] = (
            GRID_WIDTH // 2 * GRID_SIZE,
            GRID_HEIGHT // 2 * GRID_SIZE
        )
        # Цвет объекта. По умолчанию будет черный.
        self.body_color: tuple[int, int, int] = (0, 0, 0)

    def draw(self, surface):
        """Метод, определяющий отрисовку объекта GameObject."""
        raise NotImplementedError()


class Apple(GameObject):
    """Класс описывает объект игры - Яблоко."""

    def __init__(self) -> None:
        """Конструктор класса Apple."""
        super().__init__()
        self.position: tuple[int, int] = self.randomize_position()
        self.body_color: tuple[int, int, int] = (255, 0, 0)

    def randomize_position(self) -> tuple[int, int]:
        """Метод, определяющий координаты объекта Apple."""
        random_coord_width: int = randint(0, (GRID_WIDTH - 1))
        random_coord_height: int = randint(0, (GRID_HEIGHT - 1))
        apple_coord_width: int = random_coord_width * GRID_SIZE
        apple_coord_height: int = random_coord_height * GRID_SIZE
        return apple_coord_width, apple_coord_height

    def draw(self, surface):
        """Метод, определяющий отрисовку объекта Apple."""
        rect = pygame.Rect(
            (self.position[0], self.position[1]),
            (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, (93, 216, 228), rect, 1)


class Snake(GameObject):
    """Класс описывает объект игры - Змейку."""

    # Длина змейки.
    length: int = 1

    def __init__(self) -> None:
        """Конструктор класса Snake."""
        super().__init__()
        # При создании змейки будет всегда уместно
        # сбрасывать ее к начальному состоянию.
        self.reset()
        self.body_color: tuple[int, int, int] = (0, 255, 0)
        # Змейка описывается списком координат.
        self.positions: list[tuple[int, int]] = [(
            GRID_WIDTH // 2 * GRID_SIZE,
            GRID_HEIGHT // 2 * GRID_SIZE
        )]
        # Кончик хвоста змейки,
        # который нужно удалять для имитации движения.
        self.last: tuple[int, int] | None = None
        # Направление движения змейки.
        self.direction: tuple[int, int] = RIGHT
        # Новое направление движения змейки, полученное от игрока.
        self.next_direction: tuple[int, int] | None = None

    def update_direction(self) -> None:
        """Метод объекта класса Snake.

        Обновляет направления движения после нажатия на кнопку.
        """
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Метод экземпляра класса Snake.

        Обновляет позицию змейки,
        считывая её рост, проверяя столкновения.
        """
        # Блок для определения новых координат "головы" змейки.
        coordinates_old_head: tuple[int, int] = self.get_head_position()
        coordinates_new_head: tuple[int, int] = (
            coordinates_old_head[0] + self.direction[0] * GRID_SIZE,
            coordinates_old_head[1] + self.direction[1] * GRID_SIZE
        )

        # Блок контролирующий "замкнутую комнату",
        # чтобы змейка "не убегала за экран".
        if coordinates_new_head[0] < 0:
            coordinates_new_head = (
                SCREEN_WIDTH - GRID_SIZE,
                coordinates_old_head[1] + self.direction[1] * GRID_SIZE
            )
        elif coordinates_new_head[0] > SCREEN_WIDTH - GRID_SIZE:
            coordinates_new_head = (
                0, coordinates_old_head[1] + self.direction[1] * GRID_SIZE
            )
        elif coordinates_new_head[1] < 0:
            coordinates_new_head = (
                coordinates_old_head[0] + self.direction[0] * GRID_SIZE,
                SCREEN_HEIGHT - GRID_SIZE
            )
        elif coordinates_new_head[1] > SCREEN_HEIGHT - GRID_SIZE:
            coordinates_new_head = (
                coordinates_old_head[0] + self.direction[0] * GRID_SIZE, 0
            )

        # Проверка на поедание яблока.
        if self.length == len(self.positions):
            # Добавим в начало списка новую голову, для имитации движения.
            self.positions.insert(0, coordinates_new_head)
            # Обозначим где у нее хвост. Иначе не сотрется.
            # Удаляем в конце списка кончик хвоста, для имитации движения.
            self.last = self.positions.pop()
        else:
            self.positions.insert(0, coordinates_new_head)

        # Проверка на столкновения. Кусать себя за хвост нельзя!
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
        head = self.positions[0]
        head_rect = pygame.Rect((head[0], head[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, (93, 216, 228), head_rect, 1)

        # Затирание последнего сегмента.
        if self.last:
            last_rect = pygame.Rect(
                (self.last[0], self.last[1]),
                (GRID_SIZE, GRID_SIZE)
            )
            pygame.draw.rect(surface, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Метод объекта класса Snake.

        Возвращает позицию головы змейки.
        """
        return self.positions[0]

    def reset(self):
        """Метод объекта класса Snake.

        Сбрасывает змейку в начальное состояние
        после столкновения с собой.
        """
        self.length = 1
        self.positions = [(GRID_WIDTH // 2 * GRID_SIZE,
                           GRID_HEIGHT // 2 * GRID_SIZE)]
        self.direction = RIGHT
        screen.fill(BOARD_BACKGROUND_COLOR)
        pygame.display.update()
