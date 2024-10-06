import pygame
PARAMETERS =  {
            "black": (0, 0, 0),
            "red": (213, 50, 80),
            "blue": (50, 153, 213),
            "yellow": (255, 255, 102),
            "green": (0, 255, 0),
            "colors": [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)],
            "snake_size_link": 10,  # Параметр ланки (елемента) ланцюга Змійки
            "snake_speed": 5,
            "last_key_pressed": None,
            "game_over_status": False,
            "game_lost_state": False,
            "x1_change": 0,
            "y1_change": 0,
            "snake_coord_lists": [],
            "length_of_snake": 1,
            "clock":  pygame.time.Clock(),
            # "font_style":  pygame.font.SysFont("bahnshrift", 25),
            # "score_font":  pygame.font.SysFont("comicsansms", 35),
            "dis_width": 200,
            "dis_height": 200
    }

PARAMETERS["key_direction_map"] = {
            pygame.K_LEFT: (-PARAMETERS["snake_size_link"], 0),
            pygame.K_RIGHT: (PARAMETERS["snake_size_link"], 0),
            pygame.K_UP: (0, -PARAMETERS["snake_size_link"]),
            pygame.K_DOWN: (0, PARAMETERS["snake_size_link"])
    }

PARAMETERS["dis"] = pygame.display.set_mode((PARAMETERS["dis_width"], PARAMETERS["dis_height"]))