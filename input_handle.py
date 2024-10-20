#!usr/bin/env
import pygame
import graphic
import main, config

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


# !!!
# Це зайва ф-ція, яку слід вилучити
# def process_endgame_input(dis, score_font, clock, font_style, dis_width, dis_height, game_over_status, game_lost_state):
# # def process_endgame_input():
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_q:
#                 game_over_status = True
#                 game_lost_state = False
#                 # graphic.fade_to_black(dis)
#             elif event.key == pygame.K_c:
#                 # print(f"Before main.reset_game_state() in elif event.key == pygame.K_c:")
#                 main.reset_game_state()
#                 # print(f"After main.reset_game_state() in elif event.key == pygame.K_c:")
    
#             # game_over_status, game_lost_state = gameover_logic(event, game_over_status, game_lost_state, dis)
#             # game_continuation(event, dis, score_font, clock, font_style, dis_width, dis_height)
#     return game_over_status, game_lost_state


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

def game_over_or_again():
    font = pygame.font.Font(None, 25)
    game_over_text = font.render('Game Over! Press Y to play again or N to exit.', True, main.red)
    main.screen.blit(game_over_text, (main.screen_width // 6, main.screen_height // 2))
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

# Це код для старої версії, для game_lop()
# def control_snake_keys(event, key_direction_map, length_of_snake, x1_change, y1_change):
#     if event.type == pygame.KEYDOWN and event.key in key_direction_map:
#         new_x_change, new_y_change = key_direction_map[event.key]
        
#         if length_of_snake == 1 or not(x1_change + new_x_change == 0 and y1_change + new_y_change == 0):
#             return new_x_change, new_y_change
    
#     return x1_change, y1_change


def get_coord_direction(x1_change, y1_change, snake):
    length_of_snake, key_direction_map = config.PARAMS["length_of_snake"], config.PARAMS['key_direction_map']
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key in key_direction_map:
            new_x_change, new_y_change = key_direction_map[event.key]
            
            # print(f'\nx1_change == {x1_change}\nnew_x_change =={new_x_change}\n')
            # print(f'\ny1_change == {y1_change}\nnew_y_change =={new_y_change}\n')
            # if length_of_snake == 1 or not(x1_change + new_x_change == 0 and y1_change + new_y_change == 0):
            if len(snake) == 1 or not(x1_change + new_x_change == 0 and y1_change + new_y_change == 0):
                # if length_of_snake > 1:
                #     print(f'\nx1_change == {x1_change}\nnew_x_change =={new_x_change}\n')
                #     print(f'\ny1_change == {y1_change}\nnew_y_change =={new_y_change}\n')
                return new_x_change, new_y_change
    return x1_change, y1_change