#!usr/bin/env
import pygame


def main():
    pygame.init()
    dis = pygame.display.set_mode((400, 300))
    pygame.display.update()
    pygame.display.set_caption("Змійка")
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            print(event)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()