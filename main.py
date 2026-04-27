import asyncio

import pygame

from entities import Bullet, Node, Player
from settings import (
    BACKGROUND_COLOR,
    ENEMY_SPAWN_DELAY,
    FPS,
    NODE_BUILD_COST,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from systems import (
    AudioManager,
    UI,
    handle_bullet_enemy_collisions,
    handle_enemy_node_collisions,
    spawn_enemy,
)


# Global resource counter. Bullet/enemy kills increase this by 1.
scrap = 0


async def main():
    """Run the Pygame loop in the async format required by Pygbag."""
    global scrap

    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Root Access")
    clock = pygame.time.Clock()

    player = Player(80, SCREEN_HEIGHT // 2)
    nodes = [Node(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    enemies = []
    bullets = []

    ui = UI()
    audio = AudioManager()
    enemy_spawn_timer = 0

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                if scrap >= NODE_BUILD_COST:
                    nodes.append(Node(player.rect.centerx, player.rect.centery))
                    scrap -= NODE_BUILD_COST
                    audio.play("build")
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bullets.append(
                    Bullet(
                        player.rect.centerx,
                        player.rect.centery,
                        mouse_x,
                        mouse_y,
                    )
                )
                audio.play("shoot")

        player.update(dt)

        enemy_spawn_timer += dt
        if enemy_spawn_timer >= ENEMY_SPAWN_DELAY:
            enemy_spawn_timer = 0
            enemies.append(spawn_enemy(player, nodes))

        for enemy in enemies:
            enemy.update(dt)

        for bullet in bullets:
            bullet.update(dt)

        enemies = [enemy for enemy in enemies if not enemy.is_off_screen()]
        bullets = [bullet for bullet in bullets if not bullet.is_off_screen()]

        scrap_earned = handle_bullet_enemy_collisions(bullets, enemies)
        if scrap_earned > 0:
            scrap += scrap_earned
            audio.play("hit")

        node_hits = handle_enemy_node_collisions(enemies, nodes)
        if node_hits > 0:
            audio.play("node_hit")

        screen.fill(BACKGROUND_COLOR)

        for node in nodes:
            node.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

        player.draw(screen)
        ui.draw(screen, scrap)

        pygame.display.flip()

        # Required for Pygbag: yield control back to the browser event loop.
        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
