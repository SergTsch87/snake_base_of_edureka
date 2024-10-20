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

#     stop_snake
#         Функція зупинки змійки у момент зіткнення.
#         Ще треба буде її створити

def self_collision(snake_coord_lists, snake_head, game_lost_state):
    for x in snake_coord_lists[:-1]:
        if x == snake_head:
            game_lost_state = True
            # print(f"Intro def self_collision():  Is True?..  game_lost_state == {game_lost_state}")
            # pygame.time.delay(2000)
    return game_lost_state


# def check_collision_with_walls(x1, y1, dis_width, dis_height):
#     return not(0 <= x1 < dis_width and 0 <= y1 < dis_height)



# Функція зупинки змійки у момент зіткнення
# def stop_snake():
#     x1_change = y1_change = 0
#     game_lost_state = True
#     return True


# !!!
# Саме після передачі цих 3-х ф-цій до цього файлу, обробка зіткнень зникла...
def check_collision_with_walls(snake):
    return not(0 <= snake[0][0] < main.screen_width and 0 <= snake[0][1] < main.screen_height)


def self_collision(snake):
    head = snake[0]
    if head in snake[1:]:
        return True
    return False


def check_collisions(snake):
    return check_collision_with_walls(snake) or self_collision(snake)