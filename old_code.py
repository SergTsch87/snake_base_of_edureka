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