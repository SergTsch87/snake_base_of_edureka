#!usr/bin/env
import pygame
import time
import random


# 0) - Прибрати усі змінні params["name"]
# 1) Написати функції:
# для визначення швидкості
# для визначення балів / очок
# для зупинки Змійки (в момент зіткнення)
# 2) Створити нові функції
# 3) Змінити керування Змійкою клавішами
# 4) Змінити код відповідно до нового алгоритму (та перевірити, наскільки цей алгоритм відповідає правилам гри Змійка)
# 5) Прибрати зайві коментарі
# 6) Розділи графіку та логіку

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

def init_params():
    params =  {
            "black": (0, 0, 0),
            "red": (213, 50, 80),
            "blue": (50, 153, 213),
            "yellow": (255, 255, 102),
            "green": (0, 255, 0),
            "colors": [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)],

            "snake_size_link": 10,  # Параметр ланки (елемента) ланцюга Змійки
            "snake_speed": 5,

            # "dis_width": 800,
            # "dis_height": 600,
            # Для прототипу:
            "dis_width": 200,
            "dis_height": 200,
            "last_key_pressed": None,

            "game_over_status": False,
            "game_lost_state": False,
            "x1_change": 0,
            "y1_change": 0,
            "snake_coord_lists": [],
            "length_of_snake": 1,
    }
    return params

# графіка
def draw_grid(dis, dis_width, snake_size_link, dis_height, black):
    for x in range(0, dis_width, snake_size_link):
        pygame.draw.line(dis, black, (x, 0), (x, dis_height))
    for y in range(0, dis_height, snake_size_link):
        pygame.draw.line(dis, black, (0, y), (dis_width, y))


# --------------------------------------------------------
# Об'єднай ці дві функції в одну
# графіка
def snake_score(score, score_font, color, dis):
    value = score_font.render("Your score: " + str(score), True, color)
    dis.blit(value, [0, 0])

def display_info(score, speed, score_font, color, dis):
    score_text = score_font.render("Score: " + str(score), True, color)
    speed_text = score_font.render("Speed: " + str(speed), True, color)
    dis.blit(score_text, [0, 0])
    dis.blit(speed_text, [0, 30])
# --------------------------------------------------------
# графіка
def draw_snake(snake_size_link, snake_coord_lists, dis, black):
    for xy_coord_link in snake_coord_lists:
        pygame.draw.rect(dis, black, [xy_coord_link[0], xy_coord_link[1], snake_size_link, snake_size_link])

# графіка
def draw_food(dis, green, food_x, food_y, snake_size_link):
    pygame.draw.rect(dis, green, [food_x, food_y, snake_size_link, snake_size_link])


# логіка
# Збільшуємо довжину змійки під час споживання шматка їжі
def update_snake(x1, y1, snake_coord_lists):
    snake_head = [x1, y1]
    snake_coord_lists.append(snake_head)
    return snake_head

# логіка
def trim_snake_tail(snake_coord_lists, length_of_snake):
    # if not stop_snake():
    if len(snake_coord_lists) > length_of_snake:
        del snake_coord_lists[0]

# графіка
def msg_lost(msg, color, font_style, dis_width, dis_height, dis):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# логіка
def self_collision(snake_coord_lists, snake_head, game_lost_state):
    for x in snake_coord_lists[:-1]:
        if x == snake_head:
            game_lost_state = True
            pygame.time.delay(2000)
    return game_lost_state


# розділи логіку та графіку!
# Зростання змійки після кожного прийому їжі.
# Коли координати голови змійки (x1, y1) збігаються з координатами їжі (food_x, food_y),
# генерується нова їжа, і змінна params["length_of_snake"] збільшується на 1, що означає зростання змійки.

# логіка
def get_coord_new_food(dis_width, snake_size_link, dis_height):
    food_x = round(random.randrange(0, dis_width - snake_size_link) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_size_link) / 10.0) * 10.0
    return food_x, food_y


def increm_len_snake(length_of_snake):
    length_of_snake += 1
    return length_of_snake


# Функція зупинки змійки у момент зіткнення
# def stop_snake():
#     x1_change = y1_change = 0
#     game_lost_state = True
#     return True

# -------------------------------------
# графіка
# Функції завершення гри
def gameover_anim(dis, colors):
    for color in colors:
        dis.fill(color)
        pygame.display.update()
        time.sleep(0.5)

# графіка
def fade_to_black(dis):
    fade_surface = pygame.Surface(dis.get_size())
    fade_surface.fill((0, 0, 0))

    for alpha in range(0, 300, 5):
        fade_surface.set_alpha(alpha)
        dis.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(50)
# -------------------------------------

def game_loop(params, dis, score_font, clock, font_style, dis_width, dis_height):
    black = params["black"]
    red = params["red"]
    blue = params["blue"]
    yellow = params["yellow"]
    green = params["green"]
    colors = params["colors"]
    
    snake_speed = params["snake_speed"]
    
    game_over_status = params["game_over_status"] = False
    game_lost_state = params["game_lost_state"]

    x1 = params["dis_width"] / 2
    y1 = params["dis_height"] / 2

    x1_change = params["x1_change"] = 0
    y1_change = params["y1_change"] = 0

    snake_coord_lists = params["snake_coord_lists"] = []
    length_of_snake = params["length_of_snake"] = 1

    snake_size_link = params["snake_size_link"]

    food_x, food_y = get_coord_new_food(dis_width, snake_size_link, dis_height)

    # print(f"snake_coord_lists: {snake_coord_lists}")
    # print(f"length_of_snake: {length_of_snake}")
    

    while not game_over_status:
        while game_lost_state == True:
            dis.fill(blue)
            msg_lost("You Lost! Press Q-Quit or C-Play Again", red, font_style, dis_width, dis_height, dis)
            # snake_score(length_of_snake - 1, score_font, yellow, dis)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over_status = True
                        game_lost_state = False
                        pygame.time.delay(2000)
                        # gameover_anim(dis, colors)
                        fade_to_black(dis)
                    
                    if event.key == pygame.K_c:
                        game_loop(params, dis, score_font, clock, font_style, dis_width, dis_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_status = True
                pygame.time.delay(2000)
                # gameover_anim(dis, colors)
                fade_to_black(dis)
  
            if event.type == pygame.KEYDOWN:
                
                if length_of_snake == 1:
                    if event.key == pygame.K_LEFT and (x1_change == 0 or x1_change == snake_size_link):
                        x1_change = -snake_size_link
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and (x1_change == 0 or x1_change == -snake_size_link):
                        x1_change = snake_size_link
                        y1_change = 0
                    elif event.key == pygame.K_UP and (y1_change == 0 or y1_change == snake_size_link):
                        x1_change = 0
                        y1_change = -snake_size_link
                    elif event.key == pygame.K_DOWN and (y1_change == 0 or y1_change == -snake_size_link):
                        x1_change = 0
                        y1_change = snake_size_link
                
                elif length_of_snake > 1:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -snake_size_link
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = snake_size_link
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        x1_change = 0
                        y1_change = -snake_size_link
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        x1_change = 0
                        y1_change = snake_size_link
                
        # stop = stop_snake()
        
        # Обробка зіткнення змійки зі стіною
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_lost_state = True
            pygame.time.delay(2000)
        
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(blue)
        draw_grid(dis, dis_width, snake_size_link, dis_height, black)
        
        score = length_of_snake - 1 # to change!
        # display_info(score, snake_speed, score_font, yellow, dis) # Потім розкоментуй !
        
        draw_food(dis, green, food_x, food_y, snake_size_link)
        snake_head = update_snake(x1, y1, snake_coord_lists)
        
        trim_snake_tail(snake_coord_lists, length_of_snake)

        game_lost_state = self_collision(snake_coord_lists, snake_head, game_lost_state)

        draw_snake(snake_size_link, snake_coord_lists, dis, black)
        
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x, food_y = get_coord_new_food(dis_width, snake_size_link, dis_height)
            length_of_snake = increm_len_snake(length_of_snake)            

        clock.tick(snake_speed)
        # Поки що змійка миттєво збільшує свою швидкість вже після 4-го шматка їжі...
        # if params["length_of_snake"] % 5 == 0:    # Збільшенн швидкості кожні 5 балів
        #     params["snake_speed"] += 1

    pygame.quit()
    quit()


def main():
    params = init_params()
    pygame.init()

    dis_width = params["dis_width"]
    dis_height = params["dis_height"]

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption("Змійка")

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont("bahnshrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    game_loop(params, dis, score_font, clock, font_style, dis_width, dis_height)


if __name__ == "__main__":
    main()