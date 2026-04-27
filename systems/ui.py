import pygame

from settings import TEXT_COLOR


class UI:
    """Draws simple screen-space interface text."""

    def __init__(self):
        self.font = pygame.font.Font(None, 32)

    def draw(self, screen, scrap):
        scrap_text = self.font.render(f"Scrap: {scrap}", True, TEXT_COLOR)
        screen.blit(scrap_text, (16, 16))
