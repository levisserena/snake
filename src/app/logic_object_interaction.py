"""Логика взаимодействия объектов игры."""
from app.protocol import AppleP, SnakeP


def snake_ate_apple(apple: AppleP, snake: SnakeP) -> None:
    """Процесс поедания змейкой яблока."""
    if snake.get_head_position() == apple.position:
        snake.eating()
        apple.randomize_position(snake.positions)
