"""Для запуска игры."""

import pygame

from app.config import clock, screen, SPEED
from app.game_control import handle_keys
from app.objects_for_game import Apple, Snake
from app.logic_object_interaction import snake_ate_apple

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
        snake_ate_apple(apple=apple, snake=snake)


if __name__ == '__main__':
    start_and_play_game()
