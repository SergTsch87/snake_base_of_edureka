#!usr/bin/env
import pygame
import graphic
import main

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

def process_endgame_input(dis, score_font, clock, font_style, dis_width, dis_height, game_over_status, game_lost_state):
# def process_endgame_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_over_status = True
                game_lost_state = False
                # graphic.fade_to_black(dis)
            elif event.key == pygame.K_c:
                # print(f"Before main.reset_game_state() in elif event.key == pygame.K_c:")
                main.reset_game_state()
                # print(f"After main.reset_game_state() in elif event.key == pygame.K_c:")
    
            # game_over_status, game_lost_state = gameover_logic(event, game_over_status, game_lost_state, dis)
            # game_continuation(event, dis, score_font, clock, font_style, dis_width, dis_height)
    return game_over_status, game_lost_state


# def gameover_logic(event, game_over_status, game_lost_state, dis):
#     if event.key == pygame.K_q:
#         game_over_status = True
#         game_lost_state = False
#         # pygame.time.delay(2000)
#         # gameover_anim(dis, colors)
#         graphic.fade_to_black(dis)
#     return game_over_status, game_lost_state


# def game_continuation(event, dis, score_font, clock, font_style, dis_width, dis_height):
#     if event.key == pygame.K_c:
#         main.game_loop(dis, score_font, clock, font_style, dis_width, dis_height)


def control_snake_keys(event, key_direction_map, length_of_snake, x1_change, y1_change):
    if event.type == pygame.KEYDOWN and event.key in key_direction_map:
        new_x_change, new_y_change = key_direction_map[event.key]
        
        if length_of_snake == 1 or not(x1_change + new_x_change == 0 and y1_change + new_y_change == 0):
            return new_x_change, new_y_change
    
    return x1_change, y1_change