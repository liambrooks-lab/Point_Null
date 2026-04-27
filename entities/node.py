import pygame

from settings import (
    NODE_CORE_COLOR,
    NODE_CORE_SIZE,
    NODE_HEALTH_COLOR,
    NODE_SAFE_RADIUS,
    NODE_SAFE_ZONE_COLOR,
    NODE_STARTING_HEALTH,
)


class Node:
    """A safe-zone hardware point.

    A node draws a transparent safe radius and a small hardware square that
    enemies can damage.
    """

    def __init__(self, x, y, safe_radius=NODE_SAFE_RADIUS):
        self.position = pygame.Vector2(x, y)
        self.core_size = NODE_CORE_SIZE
        self.safe_radius = safe_radius
        self.health = NODE_STARTING_HEALTH
        self.max_health = NODE_STARTING_HEALTH
        self.core_rect = pygame.Rect(0, 0, self.core_size, self.core_size)
        self.core_rect.center = self.position

    def draw(self, screen):
        self._draw_safe_zone(screen)
        self._draw_core(screen)
        self._draw_health_bar(screen)

    def _draw_safe_zone(self, screen):
        diameter = self.safe_radius * 2
        safe_zone_surface = pygame.Surface((diameter, diameter), pygame.SRCALPHA)

        pygame.draw.circle(
            safe_zone_surface,
            NODE_SAFE_ZONE_COLOR,
            (self.safe_radius, self.safe_radius),
            self.safe_radius,
        )

        screen.blit(
            safe_zone_surface,
            (
                self.position.x - self.safe_radius,
                self.position.y - self.safe_radius,
            ),
        )

    def _draw_core(self, screen):
        pygame.draw.rect(screen, NODE_CORE_COLOR, self.core_rect)

    def _draw_health_bar(self, screen):
        bar_width = 28
        bar_height = 4
        health_percent = max(self.health, 0) / self.max_health
        bar_rect = pygame.Rect(0, 0, bar_width, bar_height)
        bar_rect.centerx = self.core_rect.centerx
        bar_rect.top = self.core_rect.bottom + 5

        fill_rect = bar_rect.copy()
        fill_rect.width = int(bar_width * health_percent)

        pygame.draw.rect(screen, (35, 38, 45), bar_rect)
        pygame.draw.rect(screen, NODE_HEALTH_COLOR, fill_rect)

    def contains_point(self, point):
        return self.position.distance_to(point) <= self.safe_radius

    def take_damage(self, amount):
        self.health -= amount

    def is_destroyed(self):
        return self.health <= 0
