import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        asteroid_color = "red"
        line_width = 2
        pygame.draw.circle(
            surface=screen,
            color=asteroid_color,
            center=self.position,
            radius=self.radius,
            width=line_width,
        )

    def update(self, dt):
        self.position += self.velocity * dt
