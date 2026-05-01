import pygame

from settings import PLAYER_MAX_HITS, SCREEN_HEIGHT, SCREEN_WIDTH, TEXT_COLOR


class UI:
    """Draws simple screen-space interface text."""

    def __init__(self):
        self.font = pygame.font.Font(None, 32)
        self.large_font = pygame.font.Font(None, 72)
        self.restart_button = pygame.Rect(0, 0, 190, 54)
        self.restart_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70)

    def draw(self, screen, scrap, player_hits):
        scrap_text = self.font.render(f"Scrap: {scrap}", True, TEXT_COLOR)
        health_text = self.font.render(
            f"Hits: {player_hits}/{PLAYER_MAX_HITS}",
            True,
            TEXT_COLOR,
        )

        screen.blit(scrap_text, (16, 16))
        screen.blit(health_text, (16, 46))

    def draw_game_over(self, screen):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 165))
        screen.blit(overlay, (0, 0))

        title_text = self.large_font.render("GAME OVER", True, TEXT_COLOR)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 35))
        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, (80, 230, 160), self.restart_button, border_radius=8)
        pygame.draw.rect(screen, (210, 255, 230), self.restart_button, 2, border_radius=8)

        button_text = self.font.render("Restart", True, (10, 12, 16))
        button_rect = button_text.get_rect(center=self.restart_button.center)
        screen.blit(button_text, button_rect)

    def restart_clicked(self, mouse_position):
        return self.restart_button.collidepoint(mouse_position)
