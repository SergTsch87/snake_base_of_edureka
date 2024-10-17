import pygame

pygame.init()
PARAMS =  {
            "black": (0, 0, 0),
            "red": (213, 50, 80),
            "blue": (50, 153, 213),
            "green": (0, 255, 0),
            "colors": [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)],
            "snake_size_link": 20,  # Параметр ланки (елемента) ланцюга Змійки
            "snake_speed": 20,
            "game_over_status": False,
            "game_lost_state": False,
            "x1_change": 0,
            "y1_change": 0,
            "snake_coord_lists": [],
            "length_of_snake": 1,
            "clock":  pygame.time.Clock(),
            "font_style":  pygame.font.SysFont("bahnshrift", 25),
            "score_font":  pygame.font.SysFont("comicsansms", 18),
            "screen_width": 400,
            "screen_height": 400,
            "snake_score": 1,

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

PARAMS["screen"] = pygame.display.set_mode((PARAMS["screen_width"], PARAMS["screen_height"]))
PARAMS["caption"] = pygame.display.set_caption("Змійка")
PARAMS["x1"] = int(PARAMS["screen_width"] / 2)
PARAMS["y1"] = int(PARAMS["screen_height"] / 2)


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
# screen_width
# screen_height
# dis