import main, init_settings

def get_list_coords_cell(x_start, y_start, CELL_SIZE):
    barrier_list_coords = [(x_start - 1 * CELL_SIZE, y_start - 1 * CELL_SIZE)]
    # print(f'\ncell: {barrier_list_coords}\n')
    return barrier_list_coords


def get_list_coords_line(x_start, y_start, length_line, CELL_SIZE):
    barrier_list_coords = []
    x_start -= 1 * CELL_SIZE
    y_start -= 1 * CELL_SIZE
    # print(f'\nlength_line == {length_line}')
    for _ in range(length_line):
        barrier_list_coords.append((x_start, y_start))
        y_start += 1 * CELL_SIZE
    # print(f'line: {barrier_list_coords}\n')
    return barrier_list_coords


def get_list_coords_zigzag(x_start, y_start, length_line_1, length_line_2, CELL_SIZE):
    barrier_list_coords = []
    x_start -= 1 * CELL_SIZE
    y_start -= 1 * CELL_SIZE
    # print(f'\nlength_line_1 == {length_line_1}\n')
    # print(f'\nlength_line_2 == {length_line_2}\n')
    for _ in range(length_line_1):
        barrier_list_coords.append((x_start, y_start))
        y_start += 1 * CELL_SIZE
        
    x_start += 1 * CELL_SIZE
    y_start += length_line_1 - 1 * CELL_SIZE
    for _ in range(length_line_2):
        barrier_list_coords.append((x_start, y_start))
        y_start += 1 * CELL_SIZE
    # print(f'zigzag: {barrier_list_coords}')
    return barrier_list_coords


def get_list_coords_rectangle(x_start, y_start, width, height, CELL_SIZE):
    # print(f'\nwidth == {width}\n')
    # print(f'\nheight == {height}\n')
    x_start -= 1 * CELL_SIZE
    y_start -= 1 * CELL_SIZE
    barrier_list_coords = []
    for _ in range(width):
        for _ in range(height):
            barrier_list_coords.append((x_start, y_start))
            y_start += 1 * CELL_SIZE
        x_start += 1 * CELL_SIZE
        y_start -= height * CELL_SIZE
    # print(f'rectangle: {barrier_list_coords}')
    return barrier_list_coords


def create_barrier(barrier_type, x_start, y_start, length_line_1, length_line_2, width, height, CELL_SIZE):
    nums = [x_start, y_start]
    nums_mul_20 = map(lambda x: init_settings.cell_to_pixels(x, CELL_SIZE), nums)
    x_start, y_start = nums_mul_20
    if barrier_type == 'cell':
        barrier_list_coords = get_list_coords_cell(x_start, y_start, CELL_SIZE)
        return barrier_list_coords
    
    elif barrier_type == 'line':
        barrier_list_coords = get_list_coords_line(x_start, y_start, length_line_1, CELL_SIZE)
        return barrier_list_coords
    
    elif barrier_type == 'zigzag':
        barrier_list_coords = get_list_coords_zigzag(x_start, y_start, length_line_1, length_line_2, CELL_SIZE)
        return barrier_list_coords
        
    elif barrier_type == 'rectangle':
        barrier_list_coords = get_list_coords_rectangle(x_start, y_start, width, height, CELL_SIZE)
        return barrier_list_coords