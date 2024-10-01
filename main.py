#!usr/bin/env
import pygame
import time
import random

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

    # 8) Чудові поради з сайту щодо можливих подальших покращень гри Змійка:
    #     Extra Features That Can Be Added To This Game
        
    #     There are many things that can be added to the Snake game to make it more fun and interesting. Here are some suggestions:

    #     Use different levels with rising amounts of challenge.
    #           As the game goes on, you can add barriers or make the snake move faster.
    #     Power-ups:
    #           Add things that give the player brief benefits, like making the snake move faster, making it longer, or letting it go through walls.
    #     Special food:
    #           Make special food things that only show up sometimes and give the snake extra points or special powers when it eats them.
    #     Keep track of the people with the highest scores:
    #           Set up a way to keep track of who has the highest scores. Store the scores in a file or a database and show the ranking.
    #     5.Sound effects and music:
    #           Add sound effects when things happen, like when you eat food, hit something, or finish a level. Add background sounds to make the game more enjoyable.

    #     Customizable options:
    #           Let players change game settings, such as the speed of the snake, the size of the screen, or the colour scheme, to their liking.
    #     Two-player mode:
    #           Make a mode where two people can play against each other on the same screen, each controlling their own snake.
    #     Game over animations:
    #           When the game is over, add animations or visual effects like an explosion or a screen that shows the score.
    #     Bonus Challenge:
    #           Add bonus tasks or minigames to the main game so that players can earn extra points or prizes.
    #     Mobile version:
    #           Change the settings and layout of the game so that they work best on touchscreens.

# Створюємо нову гілку, пушимо її на сервер,
# а потім перемикаємося назад на основну гілку main, щоб завантажити останні зміни з сервера
    # git checkout -b add_frame_thickness
    # git status
    # git add .\main.py
    # git commit -m "Додав код з рамкою, fra"
    # git push -u origin add_frame_thickness
    # git checkout main
    # git pull origin main

# Є дві гілки: master (m_0) та branch (m_1), - треба зробити гілку m_1 новою гілкою master.
# При бажанні, можна буде повернути назад роль гілки master гілці m_0.
    # Перейменовуєш:
    #     # git branch -m master old_master
    #     # git branch -m m_1 master
    # Пушиш:
    #     # git push origin -u master
    #     # git push origin -u old_master
    # Вилучаєш резервну копію на сервері:
    #     # git push origin --delete master# git branch -m master old_master

def init_params():
    params =  {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (213, 50, 80),
            "blue": (50, 153, 213),
            "yellow": (255, 255, 102),
            "green": (0, 255, 0),

            "snake_block": 10,
            "snake_speed": 5,

            # "dis_width": 800,
            # "dis_height": 600,
            # Для прототипу:
            "dis_width": 300,
            "dis_height": 300,
            "last_key_pressed": None
    }
    return params


def draw_grid(params, dis, dis_width, snake_block, dis_height, black):
    for x in range(0, dis_width, snake_block):
        pygame.draw.line(dis, black, (x, 0), (x, dis_height))
    for y in range(0, dis_height, snake_block):
        pygame.draw.line(dis, black, (0, y), (dis_width, y))


def snake_score(score, score_font, params, dis):
    value = score_font.render("Your score: " + str(score), True, params["yellow"])
    dis.blit(value, [0, 0])


def draw_food_and_grow_snake(snake_block, snake_list, dis, params):
    for x in snake_list:
        pygame.draw.rect(dis, params["black"], [x[0], x[1], snake_block, snake_block])


# Збільшуємо довжину змійки під час споживання шматка їжі
# def snake_growth(dis, green, food_x, food_y, snake_block, x1, y1, snake_list, stop):
def snake_growth(dis, green, food_x, food_y, snake_block, x1, y1, snake_list):
    # if not stop:
    pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    # else:
    #     snake_head = [0, 0]
    return snake_head


# ! To delete here coment
# Цей код видаляє перший елемент у списку snake_list,
# якщо довжина списку перевищує довжину змійки (length_of_snake).
# Це робиться для того, щоб змійка рухалася вперед,
# а її хвіст "відрізався", якщо вона не зростає після прийому їжі.
# def remove_the_tail_to_move_forward(snake_list, length_of_snake, stop_snake()):
def remove_the_tail_to_move_forward(snake_list, length_of_snake):
    # if not stop_snake():
    if len(snake_list) > length_of_snake:
        del snake_list[0]


def msg_lost(msg, color, font_style, params, dis):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [params["dis_width"]/6, params["dis_height"]/3])


def check_for_a_snake_collision_with_itself(snake_list, snake_head, state_when_a_player_has_lost_the_current_game):
    for x in snake_list[:-1]:
        if x == snake_head:
            state_when_a_player_has_lost_the_current_game = True
    return state_when_a_player_has_lost_the_current_game


# Зростання змійки після кожного прийому їжі.
# Коли координати голови змійки (x1, y1) збігаються з координатами їжі (food_x, food_y),
# генерується нова їжа, і змінна length_of_snake збільшується на 1, що означає зростання змійки.
def check_food_consumption(x1, y1, food_x, food_y, length_of_snake, params):
    if x1 == food_x and y1 == food_y:
        food_x = round(random.randrange(0, params["dis_width"] - params["snake_block"]) / 10.0) * 10.0
        food_y = round(random.randrange(0, params["dis_height"] - params["snake_block"]) / 10.0) * 10.0
        length_of_snake += 1
    return food_x, food_y, length_of_snake


# def stop_snake():
#     x1_change = y1_change = 0
#     state_when_a_player_has_lost_the_current_game = True
#     return True


def game_loop(params, dis, score_font, clock, font_style):
    game_over_status = False
    state_when_a_player_has_lost_the_current_game = False

    x1 = params["dis_width"] / 2
    y1 = params["dis_height"] / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    snake_block = params["snake_block"]

    food_x = round(random.randrange(0, params["dis_width"] - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, params["dis_height"] - snake_block) / 10.0) * 10.0

    while not game_over_status:
        while state_when_a_player_has_lost_the_current_game == True:
            dis.fill(params["blue"])
            msg_lost("You Lost! Press Q-Quit or C-Play Again", params["red"], font_style, params, dis)
            snake_score(length_of_snake - 1, score_font, params, dis)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over_status = True
                        state_when_a_player_has_lost_the_current_game = False
                    
                    if event.key == pygame.K_c:
                        game_loop(params, dis, score_font, clock, font_style)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_status = True

            # Помилкова логіка з напрямком змійки при зміні на протилежний напрям
            # Проблема полягає в тому, що зміна напрямку відбувається без перевірки на те,
            # чи це протилежний напрямок до поточного.
            # Якщо змійка змінює напрямок на протилежний при довжині більше 1,
            # то вона фактично зіткається сама з собою, і гра завершується.
            # Для уникнення цього потрібно додати логіку, яка блокує зміну напрямку
            # на протилежний при довжині змійки більше 1.
            
            if event.type == pygame.KEYDOWN:
                
                if length_of_snake == 1:
                    if event.key == pygame.K_LEFT and (x1_change == 0 or x1_change == snake_block):
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and (x1_change == 0 or x1_change == -snake_block):
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and (y1_change == 0 or y1_change == snake_block):
                        x1_change = 0
                        y1_change = -snake_block
                    elif event.key == pygame.K_DOWN and (y1_change == 0 or y1_change == -snake_block):
                        x1_change = 0
                        y1_change = snake_block
                
                elif length_of_snake > 1:
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        x1_change = 0
                        y1_change = -snake_block
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        x1_change = 0
                        y1_change = snake_block
                
        # stop = stop_snake()
        
        # Обробка зіткнення змійки зі стіною
        if x1 >= params["dis_width"] or x1 < 0 or y1 >= params["dis_height"] or y1 < 0:
            state_when_a_player_has_lost_the_current_game = True
        # # if x1 >= params["dis_width"] or x1 < 0 or y1 >= params["dis_height"] or y1 < 0:
        # if (x1 == params["dis_width"] and x1_change > 0) or (x1 == 0 and x1_change < 0) or (y1 == params["dis_height"] and y1_change > 0) or (y1 == 0 and y1_change < 0):
        #     # Працює тіко для лівого та верхнього зіткнення, - і тіко для одиничної змійки...
        #     x1_change = y1_change = 0
        #     state_when_a_player_has_lost_the_current_game = True
        # else:    
        #     x1 += x1_change
        #     y1 += y1_change
        
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(params["blue"])
        draw_grid(params, dis, params["dis_width"], snake_block, params["dis_height"], params["black"])
        
        # snake_head = snake_growth(dis, params["green"], food_x, food_y, snake_block, x1, y1, snake_list, stop)
        snake_head = snake_growth(dis, params["green"], food_x, food_y, snake_block, x1, y1, snake_list)
        
        # remove_the_tail_to_move_forward(snake_list, length_of_snake, stop_snake())
        remove_the_tail_to_move_forward(snake_list, length_of_snake)

        state_when_a_player_has_lost_the_current_game = check_for_a_snake_collision_with_itself(snake_list, snake_head, state_when_a_player_has_lost_the_current_game)

        draw_food_and_grow_snake(snake_block, snake_list, dis, params)
        snake_score(length_of_snake - 1, score_font, params, dis)

        pygame.display.update()

        food_x, food_y, length_of_snake = check_food_consumption(x1, y1, food_x, food_y, length_of_snake, params)

        clock.tick(params["snake_speed"])

    pygame.quit()
    quit()


def main():
    params= init_params()
    pygame.init()

    dis = pygame.display.set_mode((params["dis_width"], params["dis_height"]))
    pygame.display.set_caption("Змійка")

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont("bahnshrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    game_loop(params, dis, score_font, clock, font_style)


if __name__ == "__main__":
    main()