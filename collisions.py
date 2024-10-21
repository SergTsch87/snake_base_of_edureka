#!usr/bin/env
import pygame, main

# зіткнення
# collisions.py
    # self_collision
    # check_collision_with_walls
    # stop_snake

#     self_collision
#         Перевірка на зіткнення Змійки з собою (голови з тулубом)

#     check_collision_with_walls
#         Перевірка на зіткнення Змійки (її голови) зі стіною


def check_collision_with_barriers(snake, all_coords_all_barriers):
    head = snake[0]
    if head in all_coords_all_barriers:
        return True
    return False


def check_collision_with_walls(snake):
    return not(0 <= snake[0][0] < main.screen_width and 0 <= snake[0][1] < main.screen_height)


def self_collision(snake):
    head = snake[0]
    if head in snake[1:]:
        return True
    return False


def check_collisions(snake, all_coords_all_barriers):
    return check_collision_with_walls(snake) or self_collision(snake) or check_collision_with_barriers(snake, all_coords_all_barriers)