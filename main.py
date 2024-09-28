#!usr/bin/env
import pygame
import time
import random


white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 153, 213)
yellow = (255, 255, 102)
green = (0, 255, 0)

snake_block = 10
snake_speed = 5

# dis_width = 800
# dis_height = 600
# Для прототипу:
dis_width = 300
dis_height = 300

# to-do list:
    # 1) Додати if name == main
    # 2) - Додати сітку для поля
    # 3) Намалювати рамку для поля (створив нову гілку - add_frame_thickness)
        # - 4) Відобразити швидкість змійки на екран
    # 5) Коли змійці задаємо напрям, протилежний до її поточного руху, - тоді:
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
    #     # git push origin --delete master


# Створити нову гілку, та запушити її на сервер:
    # git checkout -b new-branch-name
        # Це створить нову гілку з іменем new-branch-name та одразу перемкне тебе на цю гілку.

        # Якщо в тебе є зміни, які ти хочеш додати в нову гілку, виконай команди:
    # git status
    # git add .
    # git commit -m "Коментар для коміту"

        # Пуш нової гілки на сервер:
    # git push -u origin new-branch-name
        # Прапор -u (або --set-upstream) встановлює зв'язок між локальною гілкою та віддаленою гілкою на сервері, щоб ти міг в майбутньому просто використовувати git push без вказування гілки.
        # Після цього нова гілка буде доступна на сервері.


def draw_grid():
    for x in range(0, dis_width, snake_block):
        pygame.draw.line(dis, black, (x, 0), (x, dis_height))
    for y in range(0, dis_height, snake_block):
        pygame.draw.line(dis, black, (0, y), (dis_width, y))

def your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

def game_loop():
    game_over = False   # стан завершення гри в цілому, і коли воно встановлено на True, гра повністю завершується
    game_close = False  # стан, коли гравець програв і має вибір — або почати гру заново, або вийти

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            # draw_grid()
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Помилкова логіка з напрямком змійки при зміні на протилежний напрям
            # Проблема полягає в тому, що зміна напрямку відбувається без перевірки на те,
            # чи це протилежний напрямок до поточного.
            # Якщо змійка змінює напрямок на протилежний при довжині більше 1,
            # то вона фактично зіткається сама з собою, і гра завершується.
            # Для уникнення цього потрібно додати логіку, яка блокує зміну напрямку
            # на протилежний при довжині змійки більше 1.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -= snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change += snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change -= snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change += snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        draw_grid()
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Цей код видаляє перший елемент у списку snake_list,
        # якщо довжина списку перевищує довжину змійки (length_of_snake).
        # Це робиться для того, щоб змійка рухалася вперед,
        # а її хвіст "відрізався", якщо вона не зростає після прийому їжі.
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Перевірка на зіткнення змійки з самою собою
        # Логіка перевіряє, чи голова змійки (snake_head) перетинається
        # з будь-якою іншою частиною її тіла, яке представлено списком snake_list.
        # Якщо є збіг, змінна game_close встановлюється в True,
        # що означає кінець гри через зіткнення змійки з собою.
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Зростання змійки після кожного прийому їжі.
        # Коли координати голови змійки (x1, y1) збігаються з координатами їжі (foodx, foody),
        # генерується нова їжа, і змінна length_of_snake збільшується на 1, що означає зростання змійки.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()



pygame.init()

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змійка")

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnshrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

game_loop()