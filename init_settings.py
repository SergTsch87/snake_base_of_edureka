import pygame, sound, config, barriers, food, main
import itertools


def cell_to_pixels(cell_coord, CELL_SIZE):
    return cell_coord * CELL_SIZE


def pixels_to_cell(cell_coord, CELL_SIZE):
    return cell_coord // CELL_SIZE


def init_game():
    target = None
    pygame.init()
    crunch, collision = sound.init_sound()
    
    CELL_SIZE = config.PARAMS['CELL_SIZE']
    barrier_list_coords_0 = barriers.create_barrier('cell', 5, 5, 0, 0, 0, 0, CELL_SIZE)
    barrier_list_coords_1 = barriers.create_barrier('line', 7, 7, 5, 0, 0, 0, CELL_SIZE)
    barrier_list_coords_2 = barriers.create_barrier('zigzag', 1, 1, 3, 2, 0, 0, CELL_SIZE)
    barrier_list_coords_3 = barriers.create_barrier('rectangle', 13, 13, 0, 0, 2, 3, CELL_SIZE)
    
    x1_change, y1_change, snake_coord_lists = config.PARAMS["x1_change"], config.PARAMS["y1_change"], config.PARAMS["snake_coord_lists"]
    key_direction_map = config.PARAMS["key_direction_map"]
    config.PARAMS["caption"]
    target = food.random_target(main.screen_width, main.snake_size_link, main.screen_height, main.snake, target)
    
    all_barriers = [barrier_list_coords_0, barrier_list_coords_1, barrier_list_coords_2, barrier_list_coords_3]
        # list_coords_all_cells_barriers = []
        # Після створення усіх перешкод, заповнюємо цей список, - 
        # задля перевірки неперетину координат кожної перешкоди
    all_coords_all_barriers = list(itertools.chain(*all_barriers))
    
    return target, x1_change, y1_change, crunch, collision, all_barriers, all_coords_all_barriers, CELL_SIZE