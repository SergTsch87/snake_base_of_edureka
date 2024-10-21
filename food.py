#!usr/bin/env
import random, main

# Їжа
# food.py


def next_random_target(snake, dis_width, CELL_SIZE, dis_height, target, all_coords_all_barriers):
    target = random_target(dis_width, CELL_SIZE, dis_height, snake, target, all_coords_all_barriers)
    return target


def random_target(dis_width, CELL_SIZE, dis_height, snake, target, all_coords_all_barriers):
#     # Щоб перевірити, чи правильно створюються координати у списку available_positions, - достатньо перевіряти,
#     # чи збігаються усі координати поля, які поза ци списком, з усіма координатами Змійки, Їжі та перешкод
    available_positions = {
        (x, y) for x in range(0, dis_width, CELL_SIZE) for y in range(0, dis_height, CELL_SIZE)
    }

    not_available_positions = set(snake)
    # print(f'not_available_positions == {not_available_positions}')
    print(f'snake == {snake}')
    not_available_positions.add(target)
    # print(f'not_available_positions == {not_available_positions}')
    print(f'target == {target}')
    print(f'all_coords_all_barriers == {all_coords_all_barriers}')
    not_available_positions.update(all_coords_all_barriers)
    # print(f'not_available_positions == {not_available_positions}')
    
    # Видаляємо з неї усі координати тіла Змійки та Їжі:
    available_positions.difference_update(not_available_positions)

    # Вибираємо нову їжу з решти доступних координат:
    x, y = random.choice(list(available_positions))

    return int(x), int(y)