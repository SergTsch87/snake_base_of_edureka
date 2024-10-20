#!usr/bin/env
from config import PARAMS
import main
# import pygame


# рух Змійки
# move.py
    # add_head_to_body
    # trim_snake_tail
    # move_snake_head
    # increm_len_snake

#     add_head_to_body
#         Додає нові координати (x1, y1) (і повертає їх) голови Змійки до snake_coord_lists.
#         Спершу то координати центру поля.
#         А в процесі руху Змійки, на кожному наступному кроці, вони стають координатами нового поля,
#         на яке перемістилась голова Змійки

#     trim_snake_tail
#         Скорочує хвіст Змійки, - прибирає останній елемент зі списку snake_coord_lists

#     move_snake_head
#         Щокроку змінює координати (x1, y1) (і повертає їх) голови Змійки.
#         На кожному наступному кроці, вони стають координатами нового поля,
#         на яке перемістилась голова Змійки

#     increm_len_snake
#         Збільшуємо довжину Змійки на 1


# # Змінюємо довжину змійки під час споживання шматка їжі
# # Збільшуємо довжину змійки
# # І тут же можна додати перевірку на зіткнення Змійки зі своїм тілом, або зі стіною
# def add_head_to_body(x1, y1, snake_coord_lists):
#     print(f"snake_head Before assign: {PARAMS['snake_head']}")
#     snake_head = (int(x1), int(y1))
#     print(f"snake_head After assign: {PARAMS['snake_head']}")
#     print(f"snake_coord_lists Before append(snake_head): {snake_coord_lists}")
#     snake_coord_lists.append(snake_head)
#     print(f"snake_coord_lists After append(snake_head): {snake_coord_lists}")
#     return snake_head


# # Скорочуємо хвіст Змійки
# def trim_snake_tail(snake_coord_lists, length_of_snake):
#     del snake_coord_lists[:-length_of_snake]


# def move_snake_head(x1, y1, x1_change, y1_change):
#     x1 += x1_change
#     y1 += y1_change
#     return x1, y1


# def increm_len_snake(length_of_snake):
#     length_of_snake += 1
#     return length_of_snake


# list1 = [1, 2, 3]
# print(f'list1[-1] = {list1[-1]}')




def check_target(target, snake):
    return snake[0] == target


def update_snake(x1_change, y1_change, snake):
    new_head = (snake[0][0] + x1_change, snake[0][1] + y1_change)
    snake.insert(0, new_head)
    snake.pop()


def grow_snake(snake):
    snake.append(snake[-1])