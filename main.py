#!usr/bin/env
import pygame, os
import time
import random
from config import PARAMS
import graphic
import input_handle
import collisions
import move
import food

# Додатки до гри:
# +0,8    Намалюй текстову інформацію (бали та час) нагорі, над ігровим полем

# ?.. Чи вона потрібна?..    Нова система координат

#  +1   Зроби ефективне створення нової їжі за допомогою available_positions
    # Треба змінити код ф-ції random_target() у food.py

#     Перешкоди на полі:
#       намальовані межі поля
#       лабіринт
#       випадкові блоки, стіни
#       "кораблі" з гри "морський бій"
#       відсутність меж, - коли Змійка виходить з одної стіни, а виходить з протилежної стіни

# Зроби рівень, в якому поле є гіперплощиною (як у грі в Nokia), - де Змійка вільно переходить межу поля, зявляючись на її протилежному боці

# +0,5    Звуки до гри: лишилось додати самі файли, з авторськими правами тощо. Here: https://opensource.com/article/20/9/add-sound-python-game
#     Павза
#     Система рівнів
#     Дошка досягнень
#     Налаштування для гри
#     Дизайн у стилі Nokia
#     ООП


# Функції, які потребують об'єднання:
#     init_params_for_game_loop()
#     init_params_for_main()

#     snake_score
#     display_info

# Перевір, або об'єднай їх!
    # add_head_to_body
    # move_snake_head


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
#     add_head_to_body
#     trim_snake_tail
#     self_collision
#     get_coord_new_food
#     check_collision_with_walls
#     move_snake_head
#     coords_center_rect


# Пояснення до функцій:


# +
# Ініціація
    # config.py
    # from config import PARAMS

# +
# графіка
# інформативність
    # graphic.py
    # import graphic
        # create_grid_surface
        # draw_grid
        # snake_score
        # display_info
        # draw_snake
        # draw_food
        # msg_lost
        # gameover_anim
        # fade_to_black
        # coords_center_rect

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

#     draw_grid
#         Просто блітимо вже намальований grid_surface на екран

#     coords_center_rect
#         Буде використовуватись для повернення координат центру прямокутника, -
#         для полегшення переходу до іншої системи координат



# +
# обробка вводу
# input_handle.py
#     process_endgame_input
#     gameover_logic
#     game_continuation
#     control_snake_keys

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


# +
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


# Їжа
# food.py
#     get_coord_new_food
#         Щокроку змінює список available_positions згідно алгоритму, - щоб залишати тіко ті чарунки,
#         які вільні для створення їжі на них
#         Повертає int(food_x), int(food_y)



#     game_loop
#         Фактично, містить в собі усю гру (без деяких ініціацій)





# стани гри


# # Які функції виконують більше, ніж одну задачу:
#     game_loop
#         Фактично, містить в собі усю гру (без деяких ініціацій)


# # Які функції потребують оптимізації:
# #     create_grid_surface
# #         Містить два цикли for, - чи можна якось оптимізувати їх?..

    # get_coord_new_food
    #     Неправильно обчислює пару координат available_positions для їжі

    # game_continuation
    #     Містить в собі рекурсивний виклик game_loop

    # process_endgame_input
    #     Містить в собі game_continuation, яка у свою чергу виконує рекурсивний виклик game_loop

#     game_loop
#         Фактично, містить в собі усю гру (без деяких ініціацій)
        # Містить в собі process_endgame_input, яка має рекурсивний виклик game_loop



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
# - 2) Створити нові функції
# - 3) Змінити керування Змійкою клавішами
# - 4) Змінити код відповідно до нового алгоритму (та перевірити, наскільки цей алгоритм відповідає правилам гри Змійка)
# 5) - Прибрати зайві коментарі
# 6) - Розділи графіку та логіку

# Що запропонував ChatGPT:

# initialize_game()

# while True:
#     handle_events()
#     add_head_to_body()
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


    # # Змінюємо довжину змійки під час споживання шматка їжі
    # # Збільшуємо довжину змійки
    # # І тут же можна додати перевірку на зіткнення Змійки зі своїм тілом, або зі стіною
    # # логіка
    # def add_head_to_body(x1, y1, snake_coord_lists):
    #     snake_head = (int(x1), int(y1))
    #     snake_coord_lists.append(snake_head)
    #     return snake_head

    # # Скорочуємо хвіст Змійки
    # # логіка
    # def trim_snake_tail(snake_coord_lists, length_of_snake):
    #     del snake_coord_lists[:-length_of_snake]




    # def increm_len_snake(length_of_snake):
    #     length_of_snake += 1
    #     return length_of_snake


    # # логіка
    # def move_snake_head(x1, y1, x1_change, y1_change):
    #     x1 += x1_change
    #     y1 += y1_change
    #     return x1, y1

def reset_game_state():
    # print(f"begin reset_game_state")
    PARAMS["snake_coord_lists"] = [[0, 0]]
    PARAMS["length_of_snake"] = 1
    PARAMS["x1"] = int(PARAMS["dis_width"] / 2)
    PARAMS["y1"] = int(PARAMS["dis_height"] / 2)
    PARAMS["x1_change"] = 0
    PARAMS["y1_change"] = 0
    PARAMS["eat_count"] = 0
    PARAMS["game_over_status"] = False
    PARAMS["game_lost_state"] = False
    PARAMS["snake_speed"] = 5
    PARAMS["available_positions"] = []
    PARAMS["snake_head"] = [0, 0]
    PARAMS["food_x"] = None
    PARAMS["food_y"] = None
    # print(f"the end reset_game_state")
    


def game_loop(dis, score_font, clock, font_style, dis_width, dis_height):
    reset_game_state()

    black, red, blue, green, colors = PARAMS["black"], PARAMS["red"], PARAMS["blue"], PARAMS["green"], PARAMS["colors"]
    snake_size_link, snake_speed = PARAMS["snake_size_link"], PARAMS["snake_speed"]
    game_over_status, game_lost_state = PARAMS["game_over_status"], PARAMS["game_lost_state"]
    x1_change, y1_change, snake_coord_lists = PARAMS["x1_change"], PARAMS["y1_change"], PARAMS["snake_coord_lists"]
    length_of_snake, key_direction_map = PARAMS["length_of_snake"], PARAMS["key_direction_map"]
    snake_head, food_x, food_y, eat_count = PARAMS["snake_head"], PARAMS["food_x"], PARAMS["food_y"], PARAMS["eat_count"]
    available_positions, x1, y1 = PARAMS["available_positions"], PARAMS["x1"], PARAMS["y1"]
    
    grid_surface = graphic.create_grid_surface(dis_width, dis_height, snake_size_link, black, blue)
    food_x, food_y = food.get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y)\

    while not game_over_status:
        # while game_lost_state == True:
        while game_lost_state:
            dis.fill(blue)
            graphic.msg_lost("You Lost! Press Q-Quit or C-Play Again", red, font_style, dis_width, dis_height, dis)
            pygame.display.update()

            # print(f"game_over_status, game_lost_state Before input_handle.process_endgame_input(): {game_over_status}, {game_lost_state}")

            # input_handle.process_endgame_input()
            # input_handle.process_endgame_input(dis, score_font, clock, font_style, dis_width, dis_height, game_over_status, game_lost_state)
            game_over_status, game_lost_state = input_handle.process_endgame_input(dis, score_font, clock, font_style, dis_width, dis_height, game_over_status, game_lost_state)
            # game_over_status, game_lost_state = input_handle.process_endgame_input()
            
            # print(f"game_over_status, game_lost_state After input_handle.process_endgame_input(): {game_over_status}, {game_lost_state}")
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_status = True
                graphic.fade_to_black(dis)

            x1_change, y1_change = input_handle.control_snake_keys(event, key_direction_map, length_of_snake, x1_change, y1_change)

        # grid_surface = create_grid_surface(dis_width, dis_height, snake_size_link, black, blue)
        graphic.draw_grid(dis, grid_surface)
        
        # list_coords = [food_x, food_y, snake_size_link, snake_size_link]            
        game_lost_state = collisions.check_collision_with_walls(x1, y1, dis_width, dis_height)

        graphic.draw_food(dis, green, food_x, food_y, snake_size_link)
        snake_head = move.add_head_to_body(x1, y1, snake_coord_lists)  # ???

        # !!!
        # Некоректна перевірка зіткнення з їжею:
        # Порівняння координат змійки і їжі за допомогою if list(snake_head) == [food_x, food_y]
        # може бути ризикованим. Якщо є зміщення навіть на один піксель (наприклад, через нецілісні числа),
        # змійка може не з'їдати їжу. Краще використовувати точні координати або враховувати розмір змійки
        # та їжі при перевірці.
        # !!!
        # 1) У add_head_to_body(), snake_head є списком.
        # 2) Чи не краще замінити цей код на add_head_to_body() ?..
        if list(snake_head) == [food_x, food_y]:            
            snake_coord_lists.append(list(snake_head))
            eat_count += 1
            # food_x, food_y = food.get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y)
            # length_of_snake = move.increm_len_snake(length_of_snake)
        else:
            move.trim_snake_tail(snake_coord_lists, length_of_snake)

        x1, y1 = move.move_snake_head(x1, y1, x1_change, y1_change)        
        graphic.draw_snake(snake_size_link, snake_coord_lists, dis, black)
        pygame.display.update()
        
        game_lost_state = collisions.self_collision(snake_coord_lists, snake_head, game_lost_state)

        # if x1 == food_x and y1 == food_y:
        #     food_x, food_y = get_coord_new_food(dis_width, snake_size_link, dis_height, snake_coord_lists, snake_head, length_of_snake, food_x, food_y)
        #     length_of_snake = increm_len_snake(length_of_snake)            

        clock.tick(snake_speed)
    
    pygame.quit()
    quit()


    # delete!
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
        
    #     x1, y1 = move_snake_head(x1, y1, x1_change, y1_change)
    #     # x1 += x1_change
    #     # y1 += y1_change
        
    #     # grid_surface = create_grid_surface(dis_width, dis_height, snake_size_link, black, blue)
    #     draw_grid(dis, grid_surface)
        
    #     score = length_of_snake - 1 # to change!
    #     # display_info(score, snake_speed, score_font, yellow, dis) # Потім розкоментуй !
        
    #     draw_food(dis, green, food_x, food_y, snake_size_link)
    #     snake_head = add_head_to_body(x1, y1, snake_coord_lists)
        
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



        # ================================================
        # ================================================
        # ================================================

black, red, blue, green, colors = PARAMS["black"], PARAMS["red"], PARAMS["blue"], PARAMS["green"], PARAMS["colors"]
snake_size_link, snake_speed = PARAMS["snake_size_link"], PARAMS["snake_speed"]
snake_score = PARAMS["snake_score"]
length_of_snake, key_direction_map = PARAMS["length_of_snake"], PARAMS["key_direction_map"]
screen_width, screen_height, screen = PARAMS["screen_width"], PARAMS["screen_height"], PARAMS["screen"]
food_x, food_y, eat_count = PARAMS["food_x"], PARAMS["food_y"], PARAMS["eat_count"]
available_positions, x1, y1 = PARAMS["available_positions"], PARAMS["x1"], PARAMS["y1"]

clock, font_style, score_font = PARAMS["clock"], PARAMS["font_style"], PARAMS["score_font"]

snake = [(screen_width // 2, screen_height // 2)]
game_is_running = True


def init_sound():
    pygame.mixer.init()
    dir_for_sound_files = os.path.join(os.path.dirname(__file__), 'sound')
    crunch = pygame.mixer.Sound(os.path.join(dir_for_sound_files, 'crunch.ogg'))
    collision = pygame.mixer.Sound(os.path.join(dir_for_sound_files, 'collision.wav'))
    # pygame.mixer.Sound.play(my_file) # Під час програвання певної події
    pygame.mixer.Sound.play(collision)
        # dir_for_sound_files = os.path.join(os.path.dirname(__file__), 'sound')
    # crunch = pygame.mixer.Sound(os.path.join(dir_for_sound_files, 'crunch.ogg'))
    # collision = pygame.mixer.Sound(os.path.join(dir_for_sound_files, 'collision.wav'))
    # # pygame.mixer.Sound.play(my_file) # Під час програвання певної події
    # pygame.mixer.Sound.play(collision)
    
    # Додавання та запуск фонової музики:
    # !!! Потім розкоментуй!
    # bckgrnd_music = pygame.mixer.music.load(os.path.join(dir_for_sound_files, 'bckgrnd Space Jazz.mp3'))
    # pygame.mixer.music.play(-1)

    # sound/crunch.ogg
    #     Apple Bite by AntumDeluge -- https://freesound.org/s/584290/ -- License: Creative Commons 0
    #     apple bite by sonicmariobrotha -- https://freesound.org/s/333825/ -- License: Creative Commons 0

    # sound/collision.wav
    #     Hit 2 by NearTheAtmoshphere -- https://freesound.org/s/676462/ -- License: Creative Commons 0
    
    # background
    # sound/bckgrnd sirius-by-sascha-ende-from-filmmusic-io.mp3
    #     https://filmmusic.io/uk/song/3233-sirius
    #     Sirius by Sascha Ende
    #         мрійливі, пливучі синтезаторні підкладки та заводний ритм. ідеально підходить для космічних тем!
    
    # sound/bckgrnd Space Jazz.mp3
    # "Space Jazz"
    # https://incompetech.com/music/royalty-free/music.html
    #     Instruments: Synths
    #     Feel: Bright, Grooving, Relaxed
    #     While working on a video game, the script called for "Space Jazz". I don't know if that is a thing, but this is what I made. Sounds like Space Jazz to me!
    #     ISRC: USUAN2100030
    #     Uploaded: 2021-09-29
    
    # Credit this piece by copying the following to your credits section:
    #     "Space Jazz" Kevin MacLeod (incompetech.com)
    #     Licensed under Creative Commons: By Attribution 4.0 License
    #     http://creativecommons.org/licenses/by/4.0/

    return crunch, collision


    # list_coords_all_cells_barriers = [] # Після створення усіх перешкод,
    #                             # заповнюємо цей список, - задля перевірки неперетину координат кожної перешкоди

# barrier_rectangle = {
#         'barrier_type': 'rectangle',
#         'x_start': 5,
#         'y_start': 5,
#         'length_line_1': 0,
#         'length_line_2': 0,
#         'width': 2,
#         'height': 2,
#         'direction': None,
#         'barrier_list_coords': координати відповідного квадрата
#     }



# cell_size = snake_size_link_in_cells = 1

# barrier_cell = {
#         'barrier_type': 'cell',
#         'x_start': 5,
#         'y_start': 5,
#         'length_line_1': 5, 
#         'length_line_2': 0,
#         'direction': None,
#         'barrier_list_coords': ('x_start', 'y_start')
#     }

#     barrier_line = {
#         'barrier_type': 'line',
#         'x_start': 5,
#         'y_start': 5,
#         'length_line_1': 5,
#         'length_line_2': 0,
#         'direction': 'vert',
#         'barrier_list_coords': [[('x_start'.value, 'y_start'.value), ('x_start'.value, 'y_start'.value + 'length_line'.value)]],

#     }

#     barrier_zigzag = {
#         'barrier_type': 'zigzag',
#         'x_start': 7,
#         'y_start': 7,
#         'length_line_1': 5,
#         'length_line_2': 3,
#         'direction': 'vert',
#         'barrier_list_coords': [[('x_start'.value, 'y_start'.value), ('x_start'.value, 'y_start'.value + 'length_line_1'.value)],
#                                 [('x_start'.value + 1, 'y_start'.value + 'length_line_1'.value), ('x_start'.value + 1, 'y_start'.value + 'length_line_1'.value + 'length_line_2'.value)]]
#     }

def get_list_coords_cell(x_start, y_start, CELL_SIZE):
    barrier_list_coords = [(x_start - 1 * CELL_SIZE, y_start - 1 * CELL_SIZE)]
    # barrier_list_coords_20 = map(lambda x[0]: x[0]*20, barrier_list_coords[0])
    print(f'\ncell: {barrier_list_coords}\n')
    return barrier_list_coords


def get_list_coords_line(x_start, y_start, length_line, CELL_SIZE):
    barrier_list_coords = []
    x_start -= 1 * CELL_SIZE
    y_start -= 1 * CELL_SIZE
    print(f'\nlength_line == {length_line}')
    for _ in range(length_line):
        barrier_list_coords.append((x_start, y_start))
        y_start += 1 * CELL_SIZE
    print(f'line: {barrier_list_coords}\n')
    return barrier_list_coords


def get_list_coords_zigzag(x_start, y_start, length_line_1, length_line_2, CELL_SIZE):
    barrier_list_coords = []
    x_start -= 1 * CELL_SIZE
    y_start -= 1 * CELL_SIZE
    print(f'\nlength_line_1 == {length_line_1}\n')
    print(f'\nlength_line_2 == {length_line_2}\n')
    for _ in range(length_line_1):
        barrier_list_coords.append((x_start, y_start))
        y_start += 1 * CELL_SIZE
        
    x_start += 1 * CELL_SIZE
    y_start += length_line_1 - 1 * CELL_SIZE
    for _ in range(length_line_2):
        barrier_list_coords.append((x_start, y_start))
        y_start += 1 * CELL_SIZE
    print(f'zigzag: {barrier_list_coords}')
    return barrier_list_coords


def get_list_coords_rectangle(x_start, y_start, width, height, CELL_SIZE):
    print(f'\nwidth == {width}\n')
    print(f'\nheight == {height}\n')
    x_start -= 1 * CELL_SIZE
    y_start -= 1 * CELL_SIZE
    barrier_list_coords = []
    for _ in range(width):
        for _ in range(height):
            barrier_list_coords.append((x_start, y_start))
            y_start += 1 * CELL_SIZE
        x_start += 1 * CELL_SIZE
        y_start -= height * CELL_SIZE
    print(f'rectangle: {barrier_list_coords}')
    return barrier_list_coords

# def create_barrier(dict_params_screen, barrier_type = 'cell', x_start = 0, y_start = 0, length_line_1 = 0, length_line_2 = 0, width = 0, height = 0, direction = 'vert'):
def create_barrier(barrier_type, x_start, y_start, length_line_1, length_line_2, width, height, CELL_SIZE):
    # barrier_type = ['cell', 'line', 'zigzag', 'rectangle']
    # x_start *= 20
    # y_start *= 20
    nums = [x_start, y_start]
    nums_mul_20 = map(lambda x: cell_to_pixels(x, CELL_SIZE), nums)
    # x_start, y_start, length_line_1, length_line_2, width, height = nums_mul_20
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


# def draw_barrier(snake_size_link, barrier_list_coords, screen, color):
# size_cell = snake_size_link // 20
size_cell = snake_size_link
# !!! Шукай помилку у визначенні, серед вхідних параметрів!
# draw_barrier(size_cell, screen, red, barrier_types[item], barriers[item])
def draw_barrier(size_cell, screen, color, barrier_type, barrier_list_coords):
    # print(f'barrier_list_coords == {barrier_list_coords}')
    if barrier_type == 'cell':
        # print(f'draw_barrier > if > barrier_list_coords == {barrier_list_coords}')
        pygame.draw.rect(screen, color, [barrier_list_coords[0][0], barrier_list_coords[0][1], size_cell, size_cell])
    else:
        # len_barrier_list_coords = len(barrier_list_coords)
        # for xy_coord_link in range(len_barrier_list_coords):
        # print(f'draw_barrier > else > barrier_list_coords == {barrier_list_coords}')
        for x, y in barrier_list_coords:
            pygame.draw.rect(screen, color, [x, y, size_cell, size_cell])
            # pygame.draw.rect(screen, color, [item[0][0], item[0][1], size_cell, size_cell])

# def draw_snake(snake_size_link, snake_coord_lists, dis, color):
#     for xy_coord_link in snake_coord_lists:
#         pygame.draw.rect(dis, color, [xy_coord_link[0], xy_coord_link[1], snake_size_link, snake_size_link])

# def draw_food(dis, color, food_x, food_y, snake_size_link):
#     pygame.draw.rect(dis, color, [food_x, food_y, snake_size_link, snake_size_link])

    # чарунка
    # пряма лінія
    # зигзаг
    # квадрат 2 на 2
    # лабіринт
    # периметр ("паркан" для поля)

    # створити координати
    # намалювати
    # обробити зіткнення


def cell_to_pixels(cell_coord, CELL_SIZE):
    return cell_coord * CELL_SIZE


def pixels_to_cell(cell_coord, CELL_SIZE):
    return cell_coord // CELL_SIZE


def init_game():
    target = None
    pygame.init()
    crunch, collision = init_sound()

    # --------------
    CELL_SIZE = PARAMS['CELL_SIZE']
    # dict_params_screen = 0
    # dict_params_barrier = 0
    dict_params_screen = {
        'width_screen_in_cells': 20,
        'height_screen_in_cells': 20,
        'cell_size': snake_size_link
    }

    # barrier_types = {
    #     'cell',
    #     'line',
    #     'zigzag',
    #     'rectangle'
    # }

    # dict_params_barrier = {
    #     'barrier_type': ['cell', 'line', 'zigzag', 'rectangle'],
    #     'x_start': -1,
    #     'y_start': -1,
    #     'length_line_1': 0, 
    #     'length_line_2': 0,
    #     'direction': ['vert', 'horz', None],
    #     'barrier_list_coords': [(None, None)]
    # }

    # barrier_list_coords_1 = [[(3, 3), (8, 3)]]
    # barrier_list_coords_2 = [[(1, 1), (2, 3)]]
    # create_barrier(dict_params_screen, barrier_type = 'cell', x_start = 0, y_start = 0, length_line_1 = 0, length_line_2 = 0, width = 0, height = 0, direction = 'vert')
    barrier_list_coords_0 = create_barrier('cell', 5, 5, 0, 0, 0, 0, CELL_SIZE)
    # print(f'barrier_list_coords_0 == {barrier_list_coords_0}')
    barrier_list_coords_1 = create_barrier('line', 7, 7, 5, 0, 0, 0, CELL_SIZE)
    # print(f'barrier_list_coords_1 == {barrier_list_coords_1}')
    barrier_list_coords_2 = create_barrier('zigzag', 1, 1, 3, 2, 0, 0, CELL_SIZE)
    # print(f'barrier_list_coords_2 == {barrier_list_coords_2}')
    barrier_list_coords_3 = create_barrier('rectangle', 10, 10, 0, 0, 2, 3, CELL_SIZE)
    # print(f'barrier_list_coords_3 == {barrier_list_coords_3}')

    # --------------
    x1_change, y1_change, snake_coord_lists = PARAMS["x1_change"], PARAMS["y1_change"], PARAMS["snake_coord_lists"]
    key_direction_map = PARAMS["key_direction_map"]
    PARAMS["caption"]
    target = food.random_target(screen_width, snake_size_link, screen_height, snake, target)
    barriers = [barrier_list_coords_0, barrier_list_coords_1, barrier_list_coords_2, barrier_list_coords_3]
    return target, x1_change, y1_change, crunch, collision, barriers, CELL_SIZE


def get_coord_direction(x1_change, y1_change):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in key_direction_map:
            new_x_change, new_y_change = key_direction_map[event.key]
            
            if length_of_snake == 1 or not(x1_change + new_x_change == 0 and y1_change + new_y_change == 0):
                return new_x_change, new_y_change
    return x1_change, y1_change


def check_collision_with_walls():
    return not(0 <= snake[0][0] < screen_width and 0 <= snake[0][1] < screen_height)
    

def self_collision():
    head = snake[0]
    if head in snake[1:]:
        return True
    return False


def check_collisions():
    return check_collision_with_walls() or self_collision()


def game_over_or_again():
    font = pygame.font.Font(None, 25)
    game_over_text = font.render('Game Over! Press Y to play again or N to exit.', True, red)
    screen.blit(game_over_text, (screen_width // 6, screen_height // 2))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    return 'exit'
                elif event.key == pygame.K_y:
                    return 'continue'
            elif event.type == pygame.QUIT:
                return 'exit'


def check_target(target):
    return snake[0] == target


def update_snake(x1_change, y1_change):
    new_head = (snake[0][0] + x1_change, snake[0][1] + y1_change)
    snake.insert(0, new_head)
    snake.pop()


def grow_snake():
    snake.append(snake[-1])


def draw_grid_snake_food(grid_surface, target, snake_score, *kwarg):
    graphic.draw_grid(screen, grid_surface)
    graphic.draw_snake(snake_size_link, snake, screen, green)
    
    graphic.draw_food(screen, red, target[0], target[1], snake_size_link)
    
    graphic.display_info(snake_score, snake_speed, score_font, black, screen)
    # draw_barrier(size_cell, screen, red, barrier_type, barrier_list_coords)


# А чи є потреба у такій функції?..
# def set_coords(my_x, my_y):
#     return my_x * snake_size_link, my_y * snake_size_link


def main():
    target, x1_change, y1_change, crunch, collision, barriers, CELL_SIZE = init_game()
    grid_surface = graphic.create_grid_surface(screen_width, screen_height, snake_size_link, black, blue)
    snake_score = PARAMS["snake_score"]
    
    while game_is_running:
        screen.fill(black)
        x1_change, y1_change = get_coord_direction(x1_change, y1_change)
        update_snake(x1_change, y1_change)

        if check_collisions():
            pygame.mixer.Sound.play(collision)
            get_game_over_or_again = game_over_or_again()
            if get_game_over_or_again == 'exit':
                break
            elif get_game_over_or_again == 'continue':
                target, x1_change, y1_change, crunch, collision, burriers, CELL_SIZE = init_game()
                snake_score = 0
                snake.clear()
                snake.append((screen_width // 2, screen_height // 2))
        
        if check_target(target):
            pygame.mixer.Sound.play(crunch)
            snake_score += 1
            target = food.next_random_target(snake, screen_width, snake_size_link, screen_height, target)
            grow_snake()
            
        draw_grid_snake_food(grid_surface, target, snake_score, graphic.draw_grid, graphic.draw_snake, graphic.draw_food, graphic.display_info)
        
        barrier_types = [
            'cell',
            'line',
            'zigzag',
            'rectangle'
        ]
        # for barrier_type in barriers:
        for item in range(4):
            # print(f'barrier_types[item] == {barrier_types[item]}')
            # print(f'barriers[item] == {barriers[item]}')

            # !!! Шукай помилку у визначенні, серед вхідних параметрів!
            draw_barrier(size_cell, screen, green, barrier_types[item], barriers[item])

        # pygame.draw.rect(dis, color, [xy_coord_link[0], xy_coord_link[1], snake_size_link, snake_size_link])
        # pygame.draw.rect(dis, color, [food_x, food_y, snake_size_link, snake_size_link])

        # draw_barrier(size_cell, screen, red, 'cell', barriers[0])
        # draw_barrier(size_cell, screen, red, 'line', barriers[1])
        # draw_barrier(size_cell, screen, red, 'zigzag', barriers[2])
        # draw_barrier(size_cell, screen, red, 'rectangle', barriers[3])
            
        pygame.display.update()
        clock.tick(5)
    
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()