"""Управление игровым процессом."""

import pygame

from app.config import Direction
from app.protocol import SnakeP


def handle_keys(snake: SnakeP):
    """Функция обработки действий пользователя."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Direction.DOWN:
                snake.next_direction = Direction.UP
            elif event.key == pygame.K_DOWN and snake.direction != Direction.UP:
                snake.next_direction = Direction.DOWN
            elif event.key == pygame.K_LEFT and snake.direction != Direction.RIGHT:
                snake.next_direction = Direction.LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != Direction.LEFT:
                snake.next_direction = Direction.RIGHT
