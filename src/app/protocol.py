"""Протоколы для типизации."""

from typing import Protocol


class SnakeP(Protocol):
    """Протокол Змейки для типизации."""

    positions: list[tuple[int, int]]
    """Список координат ячеек Змейки."""
    direction: tuple[int, int]
    """Направление движения Змейки."""
    next_direction: tuple[int, int] | None
    """Новое направление движения Змейки."""

    def get_head_position(self):
        """Метод объекта класса Snake.

        Возвращает позицию головы Змейки.
        """
        ...

    def eating(self):
        """Метод объекта класса Snake.

        Увеличит длину змейки.
        """
        ...


class AppleP(Protocol):
    """Протокол Яблоко для типизации."""

    position: tuple[int, int]

    def randomize_position(
        self,
        not_here: list[tuple[int, int]],
    ) -> None:
        """
        Метод, определяющий координаты объекта Apple.

        Может появится где угодно, кроме как в теле Змейки.
        """
        ...
