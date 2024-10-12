#!usr/bin/env
import pygame
import time
import random
from config import PARAMS
import graphic
import input_handle
import collisions
import move
import food

# Змійка кілька разів ковтає їжу, поступово зростає, і все добре.
# Аж ось, десь на 7-10-му кроці, щойно вона ковтнула черговий шматок їжі (і нікуди не врізалась!), - гра тут же завершується з помилкою:
#                                                                         line 385, in get_coord_new_food
#     food_x, food_y = random.choice(available_positions)
#     ^^^^^^^^^^^^^^
# ValueError: not enough values to unpack (expected 2, got 0)

# Може, це через рекурсивні виклики game_loop()?..


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
    print(f"begin reset_game_state")
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
    print(f"the end reset_game_state")
    


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


def main():
    clock, font_style, score_font = PARAMS["clock"], PARAMS["font_style"], PARAMS["score_font"]
    dis_width, dis_height, dis = PARAMS["dis_width"], PARAMS["dis_height"], PARAMS["dis"]
    game_over_status = PARAMS["game_over_status"]
    PARAMS["caption"]
    
    while not game_over_status:
        game_loop(dis, score_font, clock, font_style, dis_width, dis_height)
    

if __name__ == "__main__":
    main()