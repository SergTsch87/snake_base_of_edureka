import main, init_settings


def init_line(x_start, y_start, CELL_SIZE):
    barrier_list_coords = []
    x_start -= 1 * CELL_SIZE
    y_start -= 1 * CELL_SIZE
    return barrier_list_coords, x_start, y_start


def create_line(x_start, y_start, CELL_SIZE, length_line, barrier_list_coords):
    for _ in range(length_line):
        barrier_list_coords.append((x_start, y_start))
        y_start += 1 * CELL_SIZE
    return barrier_list_coords, y_start


def init_and_loop_barrier(x_start, y_start, length_line, CELL_SIZE):
    barrier_list_coords, x_start, y_start = init_line(x_start, y_start, CELL_SIZE)
    barrier_list_coords, y_start = create_line(x_start, y_start, CELL_SIZE, length_line, barrier_list_coords)
    return barrier_list_coords, x_start, y_start


def transfered_coords(x_start, k, y_start, CELL_SIZE):
    x_start += 1 * CELL_SIZE
    y_start -= k * CELL_SIZE
    return x_start, y_start


def get_list_coords_cell(x_start, y_start, CELL_SIZE):
    return [(x_start - 1 * CELL_SIZE, y_start - 1 * CELL_SIZE)] # barrier_list_coords


def get_list_coords_line(x_start, y_start, length_line, CELL_SIZE):
    barrier_list_coords, x_start, y_start = init_and_loop_barrier(x_start, y_start, length_line, CELL_SIZE)
    return barrier_list_coords


def get_list_coords_zigzag(x_start, y_start, length_line_1, length_line_2, CELL_SIZE):
    barrier_list_coords, x_start, y_start = init_and_loop_barrier(x_start, y_start, length_line_1, CELL_SIZE)
    x_start, y_start = transfered_coords(x_start, 1, y_start, CELL_SIZE)
    barrier_list_coords, y_start = create_line(x_start, y_start, CELL_SIZE, length_line_2, barrier_list_coords)
    return barrier_list_coords


def get_list_coords_rectangle(x_start, y_start, width, height, CELL_SIZE):
    barrier_list_coords, x_start, y_start = init_line(x_start, y_start, CELL_SIZE)
    for _ in range(width):
        barrier_list_coords, y_start = create_line(x_start, y_start, CELL_SIZE, height, barrier_list_coords)
        x_start, y_start = transfered_coords(x_start, height, y_start, CELL_SIZE)
    return barrier_list_coords


def create_barrier(barrier_type, x_start, y_start, length_line_1, length_line_2, width, height, CELL_SIZE):
    # Перетворення координат в пікселі
    x_start, y_start = map(lambda x: init_settings.cell_to_pixels(x, CELL_SIZE), [x_start, y_start])
    
    # Словник для підстановки типів бар'єрів до функцій
    barrier_functions = {
        'cell': lambda: get_list_coords_cell(x_start, y_start, CELL_SIZE),
        'line': lambda: get_list_coords_line(x_start, y_start, length_line_1, CELL_SIZE),
        'zigzag': lambda: get_list_coords_zigzag(x_start, y_start, length_line_1, length_line_2, CELL_SIZE),
        'rectangle': lambda: get_list_coords_rectangle(x_start, y_start, width, height, CELL_SIZE),
    }
    
    # Виклик відповідної функції
    return barrier_functions.get(barrier_type, lambda: [])()
            # для невідомого типу бар'єру, повертає порожній список як значення за замовчуванням