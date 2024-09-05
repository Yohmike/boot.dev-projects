import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        shot_color = "green"
        line_width = 2
        pygame.draw.circle(
            surface=screen,
            color=shot_color,
            center=self.position,
            radius=self.radius,
            width=line_width,
        )

    def update(self, dt):
        self.position += self.velocity * dt
