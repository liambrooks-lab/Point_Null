from settings import NODE_DAMAGE_FROM_ENEMY


def handle_bullet_enemy_collisions(bullets, enemies):
    """Remove bullets/enemies that collide and return scrap earned."""
    scrap_earned = 0

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                scrap_earned += 1
                break

    return scrap_earned


def handle_enemy_node_collisions(enemies, nodes):
    """Damage node cores when enemies touch them and return hit count."""
    hits = 0

    for enemy in enemies[:]:
        for node in nodes[:]:
            if enemy.rect.colliderect(node.core_rect):
                node.take_damage(NODE_DAMAGE_FROM_ENEMY)
                enemies.remove(enemy)
                hits += 1

                if node.is_destroyed():
                    nodes.remove(node)
                break

    return hits
