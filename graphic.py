#!usr/bin/env
import pygame, time


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

#     draw_grid
#         Просто блітимо вже намальований grid_surface на екран
    

# Використання pygame.Surface для збереження сітки ігрового поля
# Це зменшить кількість малювань і збільшить продуктивність.
# графіка
def create_grid_surface(dis_width, dis_height, snake_size_link, black, blue):
    # Створюємо новий Surface з потрібними розмірами
    grid_surface = pygame.Surface((dis_width, dis_height))
    grid_surface.fill(blue)

    for x in range(0, dis_width, snake_size_link):
        pygame.draw.line(grid_surface, black, (x, 0), (x, dis_height))
    for y in range(0, dis_height, snake_size_link):
        pygame.draw.line(grid_surface, black, (0, y), (dis_width, y))

    return grid_surface


def draw_grid(dis, grid_surface):
    # Просто блітимо вже намальований grid_surface на екран
    dis.blit(grid_surface, (0, 0))


# --------------------------------------------------------
# Об'єднай ці дві функції в одну

# графіка
def snake_score(score, score_font, color, dis):
    value = score_font.render("Your score: " + str(score), True, color)
    dis.blit(value, [0, 0])

# графіка
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


# графіка
def msg_lost(msg, color, font_style, dis_width, dis_height, dis):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


# -------------------------------------
# Функції завершення гри

# графіка
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
        # pygame.time.delay(50)
# -------------------------------------