#!usr/bin/env
import pygame
import time
import random
import config
import graphic

    # Порада:
    # Створіть окремі файли для логіки гри, рендерингу, обробки подій тощо.
# Спершу розділи функції за групами, а ті - розкинь по відповідним файлам.
# Тоді у головному файлі буде менше коду, - відповідно, стане легше та швидше працювати з кодом

# Функції, які потребують об'єднання:
#     init_params_for_game_loop()
#     init_params_for_main()

#     snake_score
#     display_info

# Перевір, або об'єднай їх!
    # update_snake
    # update_snake_position


# Функції з розділу "Графіка":
#     create_grid_surface
#     snake_score
#     display_info
#     draw_snake
#     draw_food
#     msg_lost
#     gameover_anim
#     fade_to_black

# Функції з розділу "Логіка":
#     update_snake
#     trim_snake_tail
#     self_collision
#     get_coord_new_food
#     check_collision_with_walls
#     update_snake_position
#     coords_center_rect


# Пояснення до функцій:
#     create_grid_surface
#         Використання pygame.Surface для збереження сітки ігрового поля
#         Це зменшить кількість малювань і збільшить продуктивність.

#     snake_score
#         Показує на ігровому полі к-сть балів
#     display_info
#         Показує на ігровому полі к-сть балів та швидкість Змійки
    
#     draw_snake
#         Малює Змійку, дістаючи координати кожного її елемента

#     draw_food
#         Малює квадратик їжі за заданими координатами (food_x, food_y)

#     msg_lost
#         Відображає повідомлення наприкінці гри

#     gameover_anim
#     fade_to_black
#         Функції завершення гри.
#         Кожна з них має цикл for, та часові павзи: time.sleep та time.delay
    

#     update_snake
#         Додає нові координати (x1, y1) (і повертає їх) голови Змійки до snake_coord_lists.
#         Спершу то координати центру поля.
#         А в процесі руху Змійки, на кожному наступному кроці, вони стають координатами нового поля,
#         на яке перемістилась голова Змійки

#     trim_snake_tail
#         Скорочує хвіст Змійки, - прибирає останній елемент зі списку snake_coord_lists

#     self_collision
#         Перевірка на зіткнення Змійки з собою (голови з тулубом)

#     get_coord_new_food
#         Щокроку змінює список available_positions згідно алгоритму, - щоб залишати тіко ті чарунки,
#         які вільні для створення їжі на них
#         Повертає int(food_x), int(food_y)

#     check_collision_with_walls
#         Перевірка на зіткнення Змійки (її голови) зі стіною

#     update_snake_position
#         Щокроку змінює координати (x1, y1) (і повертає їх) голови Змійки.
#         На кожному наступному кроці, вони стають координатами нового поля,
#         на яке перемістилась голова Змійки

#     coords_center_rect
#         Буде використовуватись для повернення координат центру прямокутника, -
#         для полегшення переходу до іншої системи координат
    
#     increm_len_snake
#         Збільшуємо довжину Змійки на 1

#     stop_snake
#         Функція зупинки змійки у момент зіткнення.
#         Ще треба буде її створити

#     process_endgame_input
#         Завершує / Призупиняє гру, повертаючи game_over_status, game_lost_state
#         Всередині себе має виклики функцій:
#             gameover_logic
#             game_continuation

#     gameover_logic
#         Обробляє натискання клавіші "q", (щоб потім, за цією клавішею, завершилась гра)
#         повертає game_over_status, game_lost_state

#     game_continuation
#         Обробляє натискання клавіші "c",  (щоб потім, за цією клавішею, поновилась гра)
#         Рекурсивно(!) запускає game_loop()...

#     control_snake_keys
#         Обробляє натискання клавіш-стрілок.
#         Повертає координати наступної клітинки для переміщення Змійки

#     game_loop
#         Фактично, містить в собі усю гру (без деяких ініціацій)



# # Які функції виконують більше, ніж одну задачу:
#     game_loop
#         Фактично, містить в собі усю гру (без деяких ініціацій)


# # Які функції потребують оптимізації:
# #     create_grid_surface
# #         Містить два цикли for, - чи можна якось оптимізувати їх?..

#     game_loop
#         Фактично, містить в собі усю гру (без деяких ініціацій)


# !!!
# Всередині функції game_loop відбувається рекурсивний виклик:
#     process_endgame_input() -> game_continuation() -> game_loop()
# Треба замінити рекурсію на цикл, - задля збереження ресурсів програми та машини

# Приведи до ладу функцію get_coord_new_food!..
    # Бо, наразі, я не використовую змінну available_positions,
    # яка створюється саме у цій функції, і більше нікуди не передається...

# Напрямки:
# (1, 0)
# (-1, 0)
# (0, 1)
# (0, -1)

# Перевір зайві змінні, які розпакував, - і прибери їх у моменті присвоєння (розпакування)

# А що, як змінити "систему координат" для Змійки?
# А саме - визначати координати кожної чарунки не за її кутами, а за її центром.
# Відповідно, у нових функціях (які потребують координати Змійки, їжі тощо)
# достатньо буде писати лише одну, а не дві, координати

#  Додаткові можливості для гри
    # Додати паузу: Можна додати можливість ставити гру на паузу,
    # щоб гравець міг зупинити гру та відновити її, натиснувши певну клавішу.

    # Система рівнів: Зробіть так, щоб зі зростанням довжини змійки
    # збільшувалась швидкість гри або складність.

    # Багатокористувацький режим: Додайте другий геймпад або клавіші для управління другою змійкою.
    
    # Реалізуйте систему досягнень: Додайте повідомлення гравцеві про досягнення,
    # як-от "Ви досягли рекорду!" або "Ваша змійка виросла на 50 ланок!".

# Ще поради щодо покращення гри:
#     Розділіть логіку та графіку через класи (Snake, Food, Game).
#     Оптимізуйте продуктивність через попереднє малювання сітки і рідкісні виклики pygame.display.update().
#     Впровадьте ООП для кращої структури коду.
#     Додайте нові функції (паузу, рівні складності, систему досягнень) для покращення геймплею.
#     Винесіть налаштування у конфігураційний файл.

# розділи логіку та графіку!
# Зростання змійки після кожного прийому їжі.
# Коли координати голови змійки (x1, y1) збігаються з координатами їжі (food_x, food_y),
# генерується нова їжа, і змінна params["length_of_snake"] збільшується на 1, що означає зростання змійки.

# А ще ж можна автоматизувати гру (за допомогою AI та звичайних алгоритмів), пустивши Змійку у самостіну подорож!)

# Зроби аналіз:
# Чому витратив так багато часу на редагування кращого коду?
    # Не знав деяких різних речей
# Що саме робив неправильно з самого початку?
# Що саме слід робити з початку, щоб зберегти у подальшому купу свого часу, і не робити зайву справу з кодом?

# Збери усі цікаві коди до купи, в один файл

# У версії гри в Nokia, швидкість Змійки зростала після вдалого проходження поточного рівня складності.
# Там зростала лише кількість балів від спожитої їжі (звичайної, або спец).
# Під час появи спец їжі вмикався таймер.

# Намалюй текстову інформацію (бали та час) нагорі, над ігровим полем.

# !!!
# Помилка у грі:
# Іноді їжа малюється саме на тілі(!) змійки, й тому їжа не з'являється зразу
# (змійка може переміститись на кілька чарунок, перш ніж з її хвоста з'явиться їжа).
# Як бачу, помилка - в обчисленні випадкових координат нового шматка їжі.
# Це функція get_coord_new_food

# Зроби дизайн гри, як в Nokia
# To search:
#     mobile game snake on nokia

# Об'єднай ці дві функції в одну
# snake_score та display_info

# 0) Додай від'ємний відлік часу (поки є спец їжа) на екран
# 0) - Прибрати усі змінні params["name"]
  # 1) Написати функції:
# для визначення швидкості
# для визначення балів / очок ( 1 бал - за одну їжу; 10 балів - за спец їжу )
# для зупинки Змійки (в момент зіткнення)
# 2) Створити нові функції
# 3) Змінити керування Змійкою клавішами
# 4) Змінити код відповідно до нового алгоритму (та перевірити, наскільки цей алгоритм відповідає правилам гри Змійка)
# 5) - Прибрати зайві коментарі
# 6) - Розділи графіку та логіку

# Що запропонував ChatGPT:

# initialize_game()

# while True:
#     handle_events()
#     update_snake()
#     collision = check_collisions()
#     if collision:
#         game_over()
#         break
#     else:
#         draw_game()
        
#         if not food_generated:
#             generate_food()

#     continue

# (x1, y1) - координати голови змійки
# (x1_change, y1_change) - відповідні осьові зміни руху змійки (які задають напрям руху голови змійки)

# to-do list:
    # ! Ще цікаво навчити змійку самостійно заповнювати усе поле собою
    # під час поступового зростання (з допомогою машинного навчання)
    
    # 1) Коли змійка врізається в себе, чи у межу поля, - вона повинна зупинятись,
    # міняти колір тощо, - але аж ніяк не продовжувати рух до повного завершення програми
    # - 1) Додати if name == main
    # - 2) - Додати сітку для поля
    # 3) Намалювати рамку для поля (створив нову гілку - add_frame_thickness)
        # 4) Відобразити швидкість змійки на екран
    # - 5) Коли змійці задаємо напрям, протилежний до її поточного руху, - тоді:
    #   а) Якщо довжина змійки = 1:
    #        змійка просто зупиняється.
    #   б) Якщо довжина змійки > 1:
    #        гра завершується (так, наче змійка "наїхала" на саму себе)
        # Але ж, так не повинно бути!..
        # Змійка просто повинна продовжувати рухатись у своєму поточному напрямку
    # 6) Розбити код на функції
    # 7) Використати ООП

def init_params_for_game_loop():
    params_for_game_loop =  {
            "black": (0, 0, 0),
            "red": (213, 50, 80),
            "blue": (50, 153, 213),
            "yellow": (255, 255, 102),
            "green": (0, 255, 0),
            "colors": [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)],
            "snake_size_link": 10,  # Параметр ланки (елемента) ланцюга Змійки
            "snake_speed": 5,
            "last_key_pressed": None,
            "game_over_status": False,
            "game_lost_state": False,
            "x1_change": 0,
            "y1_change": 0,
            "snake_coord_lists": [],
            "length_of_snake": 1
    }

    params_for_game_loop["key_direction_map"] = {
        pygame.K_LEFT: (-params_for_game_loop["snake_size_link"], 0),
        pygame.K_RIGHT: (params_for_game_loop["snake_size_link"], 0),
        pygame.K_UP: (0, -params_for_game_loop["snake_size_link"]),
        pygame.K_DOWN: (0, params_for_game_loop["snake_size_link"])
    }

    return params_for_game_loop

# Те, чого немає у config.py:

# key_direction_map = {
#     pygame.K_LEFT: (-params["snake_size_link"], 0)
#     pygame.K_RIGHT: (params["snake_size_link"], 0)
#     pygame.K_UP: (0, -params["snake_size_link"])
#     pygame.K_DOWN: (0, params["snake_size_link"])
# }
# clock =  pygame.time.Clock()
# font_style =  pygame.font.SysFont("bahnshrift", 25)
# score_font =  pygame.font.SysFont("comicsansms", 35)
# dis =  pygame.display.set_mode((dis_width, dis_height))


def init_params_for_main():
    pygame.init()

    params_for_main =  {
        "clock":  pygame.time.Clock(),
        "font_style":  pygame.font.SysFont("bahnshrift", 25),
        "score_font":  pygame.font.SysFont("comicsansms", 35)
    }

        # "dis_width": 800,
        # "dis_height": 600,
    # Для прототипу:
    params_for_main["dis_width"] = 300
    params_for_main["dis_height"] = 300

    # !!!
    # Якщо прибрати кому наприкінці, - тоді буде помилка:
    #     snake_base_of_edureka\main.py", line 619, in main
    #     clock, font_style, score_font, dis_width, dis_height, dis = params_main["clock"], params_main["font_style"], params_main["score_font"], params_main["dis_width"], params_main["dis_height"], params_main["dis"][0]
    #     TypeError: 'pygame.surface.Surface' object is not subscriptable
    # А з комою - працює якось і чомусь...
    params_for_main["dis"] =  pygame.display.set_mode((params_for_main["dis_width"], params_for_main["dis_height"])),

    pygame.display.set_caption("Змійка")
    # pygame.time.delay(2000)

    # print(f"params_for_main['dis'] == {params_for_main['dis']}")
    # print(f"type(params_for_main['dis']) == {type(params_for_main['dis'])}")

    return params_for_main


# Змінюємо довжину змійки під час споживання шматка їжі
# Збільшуємо довжину змійки
# І тут же можна додати перевірку на зіткнення Змійки зі своїм тілом, або зі стіною
# логіка
def update_snake(x1, y1, snake_coord_lists):
    snake_head = (int(x1), int(y1))
    snake_coord_lists.append(snake_head)
    return snake_head

# Скорочуємо хвіст Змійки
# логіка
def trim_snake_tail(snake_coord_lists, length_of_snake):
    del snake_coord_lists[:-length_of_snake]


# логіка
def self_collision(snake_coord_lists, snake_head, game_lost_state):
    for x in snake_coord_lists[:-1]:
        if x == snake_head:
            game_lost_state = True
            # pygame.time.delay(2000)
    return game_lost_state

# логіка
def get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y):
    # Зберігаємо усі можливі координати у списку:
    available_positions = [
        (x, y) for x in range(0, dis_width, snake_size_link) for y in range(0, dis_height, snake_size_link)
    ]
    # Видаляємо з неї усі координати тіла Змійки:
    # when available_positions is set
    # available_positions.difference_update(set(snake_coord_lists))
    
    # print(f"available_positions before remove = {available_positions}")
    # print(f"snake_coord_lists before remove = {snake_coord_lists}")
    # when available_positions is set
    
    # if snake_coord_lists in available_positions:
    #     available_positions.remove(snake_coord_lists)                # when available_positions is list
    #     # print(f"available_positions after remove = {available_positions}")
    
    # Вибираємо нову їжу з решти доступних координат:
    # food_x, food_y = random.choice(list(available_positions))
    # print(f"available_positions before IF = {len(available_positions)}")
    if food_x is not None and food_y is not None:
        if ([food_x, food_y] in available_positions):
            # print(f"available_positions in nested IF, Before Remove = {len(available_positions)}")
            # print(f"[food_x, food_y] in nested IF, Before Remove = {[food_x, food_y]}")
            available_positions.remove([food_x, food_y])
            # print(f"available_positions in nested IF, After Remove = {len(available_positions)}")
    if snake_head in available_positions:
        # print(f"available_positions in IF, Before Remove = {len(available_positions)}")
        # print(f"snake_head in nested IF, Before Remove = {snake_head}")
        available_positions.remove(snake_head)
    
    # print(f"available_positions, Before Append = {len(available_positions)}")
    # print(f"snake_tail, Before Append = {snake_coord_lists[:-length_of_snake]}")
    
    # !!!
    # У коді ви додаєте всі координати хвоста до available_positions через:
    available_positions.append(snake_coord_lists[:-length_of_snake])   # + snake_tail
    # Це може призвести до непередбачуваних результатів, оскільки ви додаєте список всередину списку доступних позицій. Правильніше було б додавати окремі координати
    
    food_x, food_y = random.choice(available_positions)
    # print(f"food_x = {food_x}")
    # print(f"food_y = {food_y}")
    # food_x = round(random.randrange(0, dis_width - snake_size_link) / 10.0) * 10.0
    # food_y = round(random.randrange(0, dis_height - snake_size_link) / 10.0) * 10.0
    # return food_x, food_y, available_positions
    return int(food_x), int(food_y)


def increm_len_snake(length_of_snake):
    length_of_snake += 1
    return length_of_snake


# Функція зупинки змійки у момент зіткнення
# def stop_snake():
#     x1_change = y1_change = 0
#     game_lost_state = True
#     return True


def process_endgame_input(params, dis, score_font, clock, font_style, dis_width, dis_height, game_over_status, game_lost_state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_over_status, game_lost_state = gameover_logic(event, game_over_status, game_lost_state, dis)
            game_continuation(event, params, dis, score_font, clock, font_style, dis_width, dis_height)
    return game_over_status, game_lost_state

def gameover_logic(event, game_over_status, game_lost_state, dis):
    if event.key == pygame.K_q:
        game_over_status = True
        game_lost_state = False
        # pygame.time.delay(2000)
        # gameover_anim(dis, colors)
        graphic.fade_to_black(dis)
    return game_over_status, game_lost_state


def game_continuation(event, params, dis, score_font, clock, font_style, dis_width, dis_height):
    if event.key == pygame.K_c:
        game_loop(dis, score_font, clock, font_style, dis_width, dis_height)


def control_snake_keys(event, key_direction_map, length_of_snake, x1_change, y1_change):
    if event.type == pygame.KEYDOWN and event.key in key_direction_map:
        new_x_change, new_y_change = key_direction_map[event.key]
        
        if length_of_snake == 1 or not(x1_change + new_x_change == 0 and y1_change + new_y_change == 0):
            return new_x_change, new_y_change
    
    return x1_change, y1_change

    #     # Old code for def control_snake_keys:

    #     if length_of_snake == 1:    # Для змійки довжиною 1 можна змінювати напрямок без обмежень
    #         x1_change, y1_change = new_x_change, new_y_change
    #     else:                       # Для змійки більше ніж 1 сегмент - перевірка на протилежний напрямок
    #         if (x1_change == 0 or x1_change + new_x_change != 0) and (y1_change == 0 or y1_change + new_y_change != 0):
    #             x1_change, y1_change = new_x_change, new_y_change

    # return x1_change, y1_change

# логіка
def check_collision_with_walls(x1, y1, dis_width, dis_height):
    return not(0 <= x1 < dis_width and 0 <= y1 < dis_height)

# логіка
def update_snake_position(x1, y1, x1_change, y1_change):
    x1 += x1_change
    y1 += y1_change
    return x1, y1


# list_coords = [food_x, food_y, snake_size_link, snake_size_link]
# логіка
def coords_center_rect(list_coords):
    food_x, food_y, snake_size_link, snake_size_link = list_coords
    # print(f"food_x, food_y, snake_size_link, snake_size_link = {food_x}, {food_y}, {snake_size_link}, {snake_size_link}")
# def draw_food(dis, green, food_x, food_y, snake_size_link):
#     pygame.draw.rect(dis, green, [food_x, food_y, snake_size_link, snake_size_link])


def game_loop(dis, score_font, clock, font_style, dis_width, dis_height):

    params = init_params_for_game_loop()
    black, red, blue, yellow, green, colors, snake_size_link, snake_speed, last_key_pressed, game_over_status, game_lost_state, x1_change, y1_change, snake_coord_lists, length_of_snake, key_direction_map = params["black"], params["red"], params["blue"], params["yellow"], params["green"], params["colors"], params["snake_size_link"], params["snake_speed"], params["last_key_pressed"], params["game_over_status"], params["game_lost_state"], params["x1_change"], params["y1_change"], params["snake_coord_lists"], params["length_of_snake"], params["key_direction_map"]
    grid_surface = graphic.create_grid_surface(dis_width, dis_height, snake_size_link, black, blue)

    x1 = int(dis_width / 2)
    y1 = int(dis_height / 2)

    snake_coord_lists = []
    length_of_snake = 1

    # available_positions = []
    snake_head = []
    food_x = food_y = None

    eat_count = 0

    food_x, food_y = get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y)

    while not game_over_status:
        while game_lost_state == True:
            dis.fill(blue)
            graphic.msg_lost("You Lost! Press Q-Quit or C-Play Again", red, font_style, dis_width, dis_height, dis)
            pygame.display.update()
            game_over_status, game_lost_state = process_endgame_input(params, dis, score_font, clock, font_style, dis_width, dis_height, game_over_status, game_lost_state)
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_status = True
                graphic.fade_to_black(dis)

            x1_change, y1_change = control_snake_keys(event, key_direction_map, length_of_snake, x1_change, y1_change)

        # grid_surface = create_grid_surface(dis_width, dis_height, snake_size_link, black, blue)
        graphic.draw_grid(dis, grid_surface)
        
        # list_coords = [food_x, food_y, snake_size_link, snake_size_link]            
        game_lost_state = check_collision_with_walls(x1, y1, dis_width, dis_height)

        graphic.draw_food(dis, green, food_x, food_y, snake_size_link)
        snake_head = update_snake(x1, y1, snake_coord_lists)  # ???
        # eat_count += 1
        # print(f"eat_count == {eat_count}")

        
        # draw_snake(snake_size_link, snake_coord_lists, dis, black)
        # print(f"list(snake_head) before = {list(snake_head)}")
        # print(f"[food_x, food_y] before = {[food_x, food_y]}")
        # print(f"eat_count before = {eat_count}")

        # print(f"list(snake_head) == [food_x, food_y] == {list(snake_head) == [food_x, food_y]}")

        # !!!
        # Некоректна перевірка зіткнення з їжею:
        # Порівняння координат змійки і їжі за допомогою if list(snake_head) == [food_x, food_y]
        # може бути ризикованим. Якщо є зміщення навіть на один піксель (наприклад, через нецілісні числа),
        # змійка може не з'їдати їжу. Краще використовувати точні координати або враховувати розмір змійки
        # та їжі при перевірці.
        if list(snake_head) == [food_x, food_y]:
            
            # print(f"list(snake_head) before = {list(snake_head)}")
            # print(f"[food_x, food_y] before = {[food_x, food_y]}")
            # print(f"eat_count before = {eat_count}")

            snake_coord_lists.append(list(snake_head))
            eat_count += 1

            # print(f"list(snake_head) after = {list(snake_head)}")
            # print(f"[food_x, food_y] after = {[food_x, food_y]}")
            # print(f"eat_count after = {eat_count}")
            print(f"Eat!)\neat_count == {eat_count}")
        else:
            # if length_of_snake == 1:
            #     available_positions.append(list(snake_head))

                # print(f"length_of_snake == {length_of_snake}")
                # print(f"else: ... if length_of_snake == 1:")
                # print(f"eat_count == {eat_count}")
            
            # elif length_of_snake > 1:
            #     available_positions.append(snake_coord_lists[:-length_of_snake])
            
                # print(f"length_of_snake == {length_of_snake}")
                # print(f"else: ... elif length_of_snake > 1:")
                # print(f"eat_count == {eat_count}")
            
            trim_snake_tail(snake_coord_lists, length_of_snake)
        
        # move_snake()
        # print(f"length_of_snake == {length_of_snake}")
        # print(f"length of available_positions == {len(available_positions)}")
        
        x1, y1 = update_snake_position(x1, y1, x1_change, y1_change)
        # snake_head = update_snake(x1, y1, snake_coord_lists)

        # if snake_head in available_positions:
        #     # print(f"snake_head in available_positions")
        #     available_positions.remove(snake_head)
        
        graphic.draw_snake(snake_size_link, snake_coord_lists, dis, black)
        pygame.display.update()
        

        # score = length_of_snake - 1 # to change!
        # # display_info(score, snake_speed, score_font, yellow, dis) # Потім розкоментуй !
        
        # game_lost_state = self_collision(snake_coord_lists, snake_head, game_lost_state)

        if x1 == food_x and y1 == food_y:
            food_x, food_y = get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y)
            length_of_snake = increm_len_snake(length_of_snake)            

        clock.tick(snake_speed)
    
    pygame.quit()
    quit()



    # params = init_params_for_game_loop()
    # black, red, blue, yellow, green, colors, snake_size_link, snake_speed, last_key_pressed, game_over_status, game_lost_state, x1_change, y1_change, snake_coord_lists, length_of_snake, key_direction_map = params["black"], params["red"], params["blue"], params["yellow"], params["green"], params["colors"], params["snake_size_link"], params["snake_speed"], params["last_key_pressed"], params["game_over_status"], params["game_lost_state"], params["x1_change"], params["y1_change"], params["snake_coord_lists"], params["length_of_snake"], params["key_direction_map"]
    # grid_surface = create_grid_surface(dis_width, dis_height, snake_size_link, black, blue)
    

    # x1 = dis_width / 2
    # y1 = dis_height / 2

    # snake_coord_lists = []
    # length_of_snake = 1

    # available_positions = []
    # snake_head = []
    # food_x = food_y = None

    # food_x, food_y = get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y)

    # while not game_over_status:
    #     while game_lost_state == True:
    #         dis.fill(blue)
    #         msg_lost("You Lost! Press Q-Quit or C-Play Again", red, font_style, dis_width, dis_height, dis)
    #         # snake_score(length_of_snake - 1, score_font, yellow, dis)
    #         pygame.display.update()

    #         game_over_status, game_lost_state = process_endgame_input(params, dis, score_font, clock, font_style, dis_width, dis_height, game_over_status, game_lost_state)
                    
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             game_over_status = True
    #             # pygame.time.delay(2000)
    #             # gameover_anim(dis, colors)
    #             fade_to_black(dis)

    #         x1_change, y1_change = control_snake_keys(event, key_direction_map, length_of_snake, x1_change, y1_change)

    #     # stop = stop_snake()
    #     list_coords = [food_x, food_y, snake_size_link, snake_size_link]
    #     list_2_coords = coords_center_rect(list_coords)
    #     # print(f"list_2_coords = {list_2_coords}")
    #     # def coords_center_rect(list_coords):
    #     #     food_x, food_y, snake_size_link, snake_size_link = list_coords
            
    #     game_lost_state = check_collision_with_walls(x1, y1, dis_width, dis_height)
    #     # pygame.time.delay(2000)        
        
    #     x1, y1 = update_snake_position(x1, y1, x1_change, y1_change)
    #     # x1 += x1_change
    #     # y1 += y1_change
        
    #     # grid_surface = create_grid_surface(dis_width, dis_height, snake_size_link, black, blue)
    #     draw_grid(dis, grid_surface)
        
    #     score = length_of_snake - 1 # to change!
    #     # display_info(score, snake_speed, score_font, yellow, dis) # Потім розкоментуй !
        
    #     draw_food(dis, green, food_x, food_y, snake_size_link)
    #     snake_head = update_snake(x1, y1, snake_coord_lists)
        
    #     trim_snake_tail(snake_coord_lists, length_of_snake)

    #     game_lost_state = self_collision(snake_coord_lists, snake_head, game_lost_state)

    #     draw_snake(snake_size_link, snake_coord_lists, dis, black)
        
    #     pygame.display.update()

    #     if x1 == food_x and y1 == food_y:
    #         food_x, food_y = get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y)
    #         length_of_snake = increm_len_snake(length_of_snake)            

    #     clock.tick(snake_speed)
    
    # pygame.quit()
    # quit()


def main():

    # # print(f"config.PARAMETERS = {config.PARAMETERS}")
    # # clock, dis_width, dis_height, dis, = config.PARAMETERS["clock"], config.PARAMETERS["dis_width"], config.PARAMETERS["dis_height"], config.PARAMETERS["dis"]
    # # print(f"config.PARAMETERS.clock = {config.PARAMETERS['clock']}")
    # # print(f"config.PARAMETERS.dis_width = {config.PARAMETERS['dis_width']}")
    # # print(f"config.PARAMETERS.dis_height = {config.PARAMETERS['dis_height']}")
    # # print(f"config.PARAMETERS.dis = {config.PARAMETERS['dis']}")
    
    params_main = init_params_for_main()
    clock, font_style, score_font, dis_width, dis_height, dis = params_main["clock"], params_main["font_style"], params_main["score_font"], params_main["dis_width"], params_main["dis_height"], params_main["dis"][0]
    
    game_loop(dis, score_font, clock, font_style, dis_width, dis_height)
    

if __name__ == "__main__":
    main()