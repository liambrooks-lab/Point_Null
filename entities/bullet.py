import math

import pygame

from settings import BULLET_COLOR, BULLET_SIZE, BULLET_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Bullet:
    """A projectile fired from the player toward the mouse cursor."""

    def __init__(self, x, y, target_x, target_y):
        self.size = BULLET_SIZE
        self.speed = BULLET_SPEED
        self.position = pygame.Vector2(x, y)
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = self.position

        angle = math.atan2(target_y - y, target_x - x)
        self.velocity = pygame.Vector2(
            math.cos(angle) * self.speed,
            math.sin(angle) * self.speed,
        )

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def is_off_screen(self):
        return (
            self.rect.right < 0
            or self.rect.left > SCREEN_WIDTH
            or self.rect.bottom < 0
            or self.rect.top > SCREEN_HEIGHT
        )

    def draw(self, screen):
        pygame.draw.rect(screen, BULLET_COLOR, self.rect)
