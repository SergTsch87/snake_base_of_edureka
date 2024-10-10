#!usr/bin/env
import pygame

# зіткнення
# collisions.py
    # self_collision
    # check_collision_with_walls
    # stop_snake

#     self_collision
#         Перевірка на зіткнення Змійки з собою (голови з тулубом)

#     check_collision_with_walls
#         Перевірка на зіткнення Змійки (її голови) зі стіною

#     stop_snake
#         Функція зупинки змійки у момент зіткнення.
#         Ще треба буде її створити

# логіка
def self_collision(snake_coord_lists, snake_head, game_lost_state):
    for x in snake_coord_lists[:-1]:
        if x == snake_head:
            game_lost_state = True
            # print(f"Intro def self_collision():  Is True?..  game_lost_state == {game_lost_state}")
            # pygame.time.delay(2000)
    return game_lost_state


# логіка
def check_collision_with_walls(x1, y1, dis_width, dis_height):
    return not(0 <= x1 < dis_width and 0 <= y1 < dis_height)



# Функція зупинки змійки у момент зіткнення
# def stop_snake():
#     x1_change = y1_change = 0
#     game_lost_state = True
#     return True