#!usr/bin/env
from config import PARAMS
import main


def check_target(target, snake):
    return snake[0] == target


def update_snake(x1_change, y1_change, snake):
    new_head = (snake[0][0] + x1_change, snake[0][1] + y1_change)
    snake.insert(0, new_head)
    snake.pop()


def grow_snake(snake):
    snake.append(snake[-1])