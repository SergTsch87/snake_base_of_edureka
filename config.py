import pygame

pygame.init()
PARAMS =  {
            "black": (0, 0, 0),
            "red": (213, 50, 80),
            "blue": (50, 153, 213),
            "green": (0, 255, 0),
            "colors": [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)],
            "snake_size_link": 10,  # Параметр ланки (елемента) ланцюга Змійки
            "snake_speed": 5,
            "game_over_status": False,
            "game_lost_state": False,
            "x1_change": 0,
            "y1_change": 0,
            "snake_coord_lists": [],
            "length_of_snake": 1,
            "clock":  pygame.time.Clock(),
            "font_style":  pygame.font.SysFont("bahnshrift", 25),
            "score_font":  pygame.font.SysFont("comicsansms", 35),
            "dis_width": 200,
            "dis_height": 200,

            "available_positions": [],
            "snake_head": [],
            "food_x": None,
            "food_y": None,
            "eat_count": 0,
    }

PARAMS["key_direction_map"] = {
            pygame.K_LEFT: (-PARAMS["snake_size_link"], 0),
            pygame.K_RIGHT: (PARAMS["snake_size_link"], 0),
            pygame.K_UP: (0, -PARAMS["snake_size_link"]),
            pygame.K_DOWN: (0, PARAMS["snake_size_link"]),
    }

PARAMS["dis"] = pygame.display.set_mode((PARAMS["dis_width"], PARAMS["dis_height"]))
PARAMS["caption"] = pygame.display.set_caption("Змійка")
PARAMS["x1"] = int(PARAMS["dis_width"] / 2)
PARAMS["y1"] = int(PARAMS["dis_height"] / 2)


# pygame.quit()
# quit()


# black
# red
# blue
# yellow
# green
# colors
# snake_size_link
# snake_speed
# last_key_pressed
# game_over_status
# game_lost_state
# x1_change
# y1_change
# snake_coord_lists
# length_of_snake
# key_direction_map


# clock
# font_style
# score_font
# dis_width
# dis_height
# dis