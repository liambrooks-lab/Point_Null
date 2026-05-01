import pygame

from settings import (
    PLAYER_COLOR,
    PLAYER_GUN_COLOR,
    PLAYER_SIZE,
    PLAYER_SKIN_COLOR,
    PLAYER_SPEED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


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

    def draw(self, screen, mouse_position):
        center = pygame.Vector2(self.rect.center)
        aim_direction = pygame.Vector2(mouse_position) - center

        if aim_direction.length_squared() > 0:
            aim_direction = aim_direction.normalize()
        else:
            aim_direction = pygame.Vector2(1, 0)

        body_radius = self.size // 2
        head_radius = 6
        gun_start = center + aim_direction * 8
        gun_end = center + aim_direction * 24

        # Simple top-down person: body, head, and a gun aimed at the cursor.
        pygame.draw.circle(screen, PLAYER_COLOR, center, body_radius)
        pygame.draw.circle(screen, PLAYER_SKIN_COLOR, center - aim_direction * 5, head_radius)
        pygame.draw.line(screen, PLAYER_GUN_COLOR, gun_start, gun_end, 5)
        pygame.draw.circle(screen, (30, 34, 38), gun_end, 3)
