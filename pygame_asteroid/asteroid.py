import pygame
import random
from circleshape import CircleShape
from constants import *


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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            left = self.velocity.rotate(-random_angle)
            right = self.velocity.rotate(random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            left_asteroid = Asteroid(*self.position, new_radius)
            right_asterdoi = Asteroid(*self.position, new_radius)
            left_asteroid.velocity = left * 1.2
            right_asterdoi.velocity = right * 1.2
