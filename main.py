"""Для запуска игры."""
import pygame

from config import clock, SPEED, screen
from game_control import handle_keys
from objects_for_game import Apple, Snake


pygame.init()


def start_game() -> None:
    """Функция, запускающая игру."""
    apple: Apple = Apple()
    snake: Snake = Snake()

    while True:
        clock.tick(SPEED)
        apple.draw(screen)
        snake.draw(screen)
        snake.move()
        handle_keys(snake)
        snake.update_direction()
        pygame.display.flip()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple = Apple()


if __name__ == '__main__':
    start_game()
