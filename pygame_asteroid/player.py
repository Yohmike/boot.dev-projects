import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        player_color = "white"
        line_width = 2
        pygame.draw.polygon(
            surface=screen, color=player_color, points=self.triangle(), width=line_width
        )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt=360 - dt)
            # self.rotate(dt=-dt)
        if keys[pygame.K_d]:
            self.rotate(dt=dt)
        if keys[pygame.K_w]:
            self.move(dt=dt)
        if keys[pygame.K_s]:
            self.move(dt=-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.shot_cooldown -= dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown <= 0:
            shot = Shot(*self.position)
            shot.velocity = (
                pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
            )
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
