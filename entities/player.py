import pygame

from settings import PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH


class Player:
    """The controllable character.

    The player class owns movement input, screen-boundary clamping, and drawing.
    """

    def __init__(self, x, y):
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED
        self.position = pygame.Vector2(x, y)
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            direction.y -= 1
        if keys[pygame.K_s]:
            direction.y += 1
        if keys[pygame.K_a]:
            direction.x -= 1
        if keys[pygame.K_d]:
            direction.x += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()

        self.position += direction * self.speed * dt
        self.rect.topleft = self.position
        self._keep_inside_screen()

    def _keep_inside_screen(self):
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, SCREEN_WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, SCREEN_HEIGHT)
        self.position.update(self.rect.topleft)

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)
