import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    py_game_time = pygame.time.Clock()
    dt: int = 0
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # update groups for player
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player_initial_location = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player = Player(*player_initial_location, radius=30)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for updatable_object in updatable:
            updatable_object.update(dt=dt)
        for drawable_object in drawable:
            drawable_object.draw(screen=screen)
        pygame.display.flip()
        dt = py_game_time.tick(60) / 1000


if __name__ == "__main__":
    main()
