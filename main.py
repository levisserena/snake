"""Для запуска игры."""

import pygame

from config import clock, screen, SPEED
from game_control import handle_keys
from objects_for_game import Apple, Snake

pygame.init()


def start_and_play_game() -> None:
    """Функция, запускающая игру со всей логикой."""
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
        snake.eating(apple)


if __name__ == '__main__':
    start_and_play_game()
