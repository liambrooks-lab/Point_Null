import random

import pygame

from entities.enemy import Enemy
from settings import SCREEN_HEIGHT, SCREEN_WIDTH


def spawn_enemy(player, nodes):
    """Create an enemy at a random screen edge, avoiding safe zones."""
    for _ in range(100):
        edge = random.choice(("top", "bottom", "left", "right"))

        if edge == "top":
            x = random.randint(0, SCREEN_WIDTH)
            y = -30
        elif edge == "bottom":
            x = random.randint(0, SCREEN_WIDTH)
            y = SCREEN_HEIGHT + 30
        elif edge == "left":
            x = -30
            y = random.randint(0, SCREEN_HEIGHT)
        else:
            x = SCREEN_WIDTH + 30
            y = random.randint(0, SCREEN_HEIGHT)

        spawn_point = pygame.Vector2(x, y)

        if not any(node.contains_point(spawn_point) for node in nodes):
            return Enemy(x, y, player.rect.centerx, player.rect.centery)

    # Fallback: if player-built nodes cover every edge, still spawn one enemy
    # instead of letting the browser game loop hang.
    return Enemy(-30, random.randint(0, SCREEN_HEIGHT), player.rect.centerx, player.rect.centery)
