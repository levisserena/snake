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


class AppleP(Protocol):
    """Протокол Яблоко для типизации."""

    position: tuple[int, int]

    def randomize_position(self, snake: SnakeP | None = None) -> None:
        """
        Метод, определяющий координаты объекта Apple.

        Может появится где угодно, кроме как в теле Змейки.
        """
        ...
