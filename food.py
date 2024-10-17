#!usr/bin/env
import random, main

# Їжа
# food.py
#     get_coord_new_food
#         Щокроку змінює список available_positions згідно алгоритму, - щоб залишати тіко ті чарунки,
#         які вільні для створення їжі на них
#         Повертає int(food_x), int(food_y)


def next_random_target(snake, dis_width, snake_size_link, dis_height, target):
    target = random_target(dis_width, snake_size_link, dis_height, snake, target)
    return target


def random_target(dis_width, snake_size_link, dis_height, snake, target):
    # # other code:
    # x = random.randint(0, (dis_width // snake_size_link) - 1) * snake_size_link
    # y = random.randint(0, (dis_height // snake_size_link) - 1) * snake_size_link

#     # Щоб перевірити, чи правильно створюються координати у списку available_positions, - достатньо перевіряти,
#     # чи збігаються усі координати поля, які поза ци списком, з усіма координатами Змійки, Їжі та перешкод
    available_positions = {
        (x, y) for x in range(0, dis_width, snake_size_link) for y in range(0, dis_height, snake_size_link)
    }

    not_available_positions = set(snake)
    not_available_positions.add(target)
    # print(f'\nNOT check_target(target): not_available_positions = {not_available_positions}')
    # print(f'Їжа: {target}\n')

    # Видаляємо з неї усі координати тіла Змійки та Їжі:
    available_positions.difference_update(not_available_positions)

    # Вибираємо нову їжу з решти доступних координат:
    x, y = random.choice(list(available_positions))

    return int(x), int(y)