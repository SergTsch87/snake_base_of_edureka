#!usr/bin/env
import pygame, os
import time
import random
from config import PARAMS
import graphic
import input_handle
import collisions
import move
import food, sound, barriers, init_settings


black, red, blue, green, lazur, colors = PARAMS["black"], PARAMS["red"], PARAMS["blue"], PARAMS["green"], PARAMS["lazur"], PARAMS["colors"]
# snake_size_link = PARAMS["snake_size_link"]
snake_speed = PARAMS["snake_speed"]
snake_score = PARAMS["snake_score"]
length_of_snake, key_direction_map = PARAMS["length_of_snake"], PARAMS["key_direction_map"]
screen_width, screen_height, screen = PARAMS["screen_width"], PARAMS["screen_height"], PARAMS["screen"]
food_x, food_y, eat_count = PARAMS["food_x"], PARAMS["food_y"], PARAMS["eat_count"]
available_positions, x1, y1 = PARAMS["available_positions"], PARAMS["x1"], PARAMS["y1"]

clock, font_style, score_font = PARAMS["clock"], PARAMS["font_style"], PARAMS["score_font"]

snake = [(screen_width // 2, screen_height // 2)]
game_is_running = True

    # чарунка    # пряма лінія    # зигзаг    # квадрат 2 на 2    # лабіринт    # периметр ("паркан" для поля)


def main():
    # if prapor:
    #     гра працює
    # else:
    #     гра зупиняється
    
    target, x1_change, y1_change, crunch, collision, all_barriers, all_coords_all_barriers, CELL_SIZE, barriers_surface = init_settings.init_game()
    grid_surface = graphic.create_grid_surface(screen_width, screen_height, CELL_SIZE, black, blue)
    snake_score = PARAMS["snake_score"]
    is_paused = False
    was_just_unpaused = False

    while game_is_running:
        
        # is_paused = False
        # game_paused = input_handle.pause(is_paused)
        # print(f'game_paused == {game_paused}')
    
        # if game_paused:
        #     print(f'\nIF game_paused...\n')
        #     screen.fill(black)
        #     x1_change, y1_change = 0, 0
        #     head = snake[0]
        #     graphic.draw_grid_snake_food(grid_surface, target, snake_score, CELL_SIZE, snake, screen, lazur, snake_speed, score_font, black, red, all_barriers, green)
        #     pygame.display.update()
        # else:
        # print(f'\nELSE game_paused...\n')
        screen.fill(black)
        screen.blit(barriers_surface, (0, 0)) # Відображення поверхні з перешкодами
        x1_change, y1_change, is_paused, was_just_unpaused = input_handle.get_coord_direction(x1_change, y1_change, snake, is_paused, was_just_unpaused)
        if is_paused:
            continue
        move.update_snake(x1_change, y1_change, snake)

        if collisions.check_collisions(snake, all_coords_all_barriers):
            pygame.mixer.Sound.play(collision)
            get_game_over_or_again = input_handle.game_over_or_again()
            if get_game_over_or_again == 'exit':
                break
            elif get_game_over_or_again == 'continue':
                target, x1_change, y1_change, crunch, collision, burriers, all_coords_all_barriers, CELL_SIZE, barriers_surface = init_settings.init_game()
                snake_score = 0
                snake.clear()
                snake.append((screen_width // 2, screen_height // 2))
        
        if move.check_target(target, snake):
            pygame.mixer.Sound.play(crunch)
            snake_score += 1
            target = food.next_random_target(snake, screen_width, CELL_SIZE, screen_height, target, all_coords_all_barriers)
            move.grow_snake(snake)
            
        graphic.draw_grid_snake_food(grid_surface, target, snake_score, CELL_SIZE, snake, screen, lazur, snake_speed, score_font, black, red, all_barriers, green)
        
        pygame.display.update()
        clock.tick(3)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()