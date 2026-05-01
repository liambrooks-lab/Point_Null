import pygame

from settings import ENEMY_COLOR, ENEMY_SIZE, ENEMY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy:
    """A hostile entity that moves in a straight line from the screen edge."""

    def __init__(self, x, y, target_x, target_y):
        self.size = ENEMY_SIZE
        self.speed = ENEMY_SPEED
        self.position = pygame.Vector2(x, y)
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.rect.center = self.position

        target_position = pygame.Vector2(target_x, target_y)
        direction = target_position - self.position

        if direction.length_squared() > 0:
            self.velocity = direction.normalize() * self.speed
        else:
            self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def is_off_screen(self):
        margin = 80
        return (
            self.rect.right < -margin
            or self.rect.left > SCREEN_WIDTH + margin
            or self.rect.bottom < -margin
            or self.rect.top > SCREEN_HEIGHT + margin
        )

    def draw(self, screen):
        pygame.draw.circle(screen, ENEMY_COLOR, self.rect.center, self.size // 2)
