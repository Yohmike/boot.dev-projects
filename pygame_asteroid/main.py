import pygame
from constants import *


def main():
    pygame.init()
    py_game_time = pygame.time.Clock()
    dt: int = 0
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = py_game_time.tick(60) // 1000


if __name__ == "__main__":
    main()
