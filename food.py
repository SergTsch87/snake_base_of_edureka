#!usr/bin/env
import random

# import pygame

# Їжа
# food.py
#     get_coord_new_food
#         Щокроку змінює список available_positions згідно алгоритму, - щоб залишати тіко ті чарунки,
#         які вільні для створення їжі на них
#         Повертає int(food_x), int(food_y)


# Це для складнішої версії функції:
# def random_target(dis_width, snake_size_link, dis_height, snake_coord_lists):
def random_target(dis_width, snake_size_link, dis_height):
    x = random.randint(0, (dis_width // snake_size_link) - 1) * snake_size_link
    y = random.randint(0, (dis_height // snake_size_link) - 1) * snake_size_link
    return x, y

# # def get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y):
# # def get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists):
# def random_target(dis_width, snake_size_link, dis_height, snake_coord_lists):
#     # !!!
#     # Щоб перевірити, чи правильно створюються координати у списку available_positions, - достатньо перевіряти,
#     # чи збігаються усі координати поля, які поза ци списком, з усіма координатами Змійки, Їжі та перешкод
    
#     # Зберігаємо усі можливі координати у списку:
#     available_positions = {
#         # (x, y) for x in range(0, dis_width, snake_size_link) for y in range(0, dis_height, snake_size_link)
#         (x, y) for x in range(0, dis_width, snake_size_link) for y in range(0, dis_height, snake_size_link)
#     }
#     # Видаляємо з неї усі координати тіла Змійки:
#     # when available_positions is set
#     available_positions.difference_update(set(snake_coord_lists))
    
#     # print(f"available_positions before remove = {available_positions}")
#     # print(f"snake_coord_lists before remove = {snake_coord_lists}")
#     # when available_positions is set
    
#     # if snake_coord_lists in available_positions:
#     #     available_positions.remove(snake_coord_lists)                # when available_positions is list
#     #     # print(f"available_positions after remove = {available_positions}")
    
#     # Вибираємо нову їжу з решти доступних координат:
#     food_x, food_y = random.choice(list(available_positions))
#     # print(f"available_positions before IF = {len(available_positions)}")
#     # if food_x is not None and food_y is not None:
#     #     if ([food_x, food_y] in available_positions):
#     #     # if ((food_x, food_y) in available_positions):
#     #         # print(f"available_positions in nested IF, Before Remove = {len(available_positions)}")
#     #         # print(f"[food_x, food_y] in nested IF, Before Remove = {[food_x, food_y]}")
#     #         available_positions.remove([food_x, food_y])
#     #         # print(f"available_positions in nested IF, After Remove = {len(available_positions)}")
    
#     # if snake_head in available_positions:
#     #     # print(f"available_positions in IF, Before Remove = {len(available_positions)}")
#     #     # print(f"snake_head in nested IF, Before Remove = {snake_head}")
#     #     available_positions.remove(snake_head)
    
#     # print(f"available_positions, Before Append = {len(available_positions)}")
#     # print(f"snake_tail, Before Append = {snake_coord_lists[:-length_of_snake]}")
    
#     # # !!!
#     # # У коді ви додаєте всі координати хвоста до available_positions через:
#     # print(f"Before:   len(available_positions) == {len(available_positions)}")
#     # available_positions.append(snake_coord_lists[:-length_of_snake])   # + snake_tail
#     # print(f"After:   len(available_positions) == {len(available_positions)}")
#     # # Це може призвести до непередбачуваних результатів, оскільки ви додаєте список всередину списку доступних позицій. Правильніше було б додавати окремі координати
    
#     # print(f"Before: (food_x, food_y) == ({food_x}, {food_y})")
#     # food_x, food_y = random.choice(available_positions)
#     # available_positions.remove([food_x, food_y])
#     # print(f"After: (food_x, food_y) == ({food_x}, {food_y})")
    
#     # print(f"food_x = {food_x}")
#     # print(f"food_y = {food_y}")
#     # food_x = round(random.randrange(0, dis_width - snake_size_link) / 10.0) * 10.0
#     # food_y = round(random.randrange(0, dis_height - snake_size_link) / 10.0) * 10.0
#     # return food_x, food_y, available_positions
#     return int(food_x), int(food_y)