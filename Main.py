import os
import pygame
import sys
import random
import Projectile
import Enemy
import Player

# Center the game window & start the environment, set up display
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("Shoot the enemy tie fighters to escape the Imperial fleet")
game_view = pygame.display.set_mode([1024, 768])
game_view_rect = game_view.get_rect()


def __main__():
    # Create user sprite
    user = Player.Player()

    # Create enemies
    enemies = make_enemies(7)

    # Main game loop
    while user.lives != 0:

        # Quit the game if QUIT is initiated
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Drawing
        enemies.draw(game_view)

        # Updates
        update_game()

def make_enemies(n):
    enemy_list = pygame.sprite.Group()
    offset = 86
    for enemy in range(0,n):
        enemy = Enemy.Enemy(86, 86)
        enemy.set_xy((len(enemy_list) * offset), 0)
        enemy_list.add(enemy)
    return enemy_list

def draw_list(list):
    for _ in range(0, len(list)):
        list[_].draw()

def update_game():
    pygame.display.update()

def update_user(user):
    user.update()

def update_enemies(enemy_list):
    for enemy in enemy_list:
        enemy.update()

if __name__ == '__main__':
    __main__()

