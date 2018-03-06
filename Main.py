import os
import pygame
import sys
import random
import Projectile
import Enemy
import Player

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (30, 30, 30)
clock = pygame.time.Clock()
time = pygame.time.get_ticks()

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
    enemy_list = []
    for enemy in range(0,1):
        enemy = Enemy.Enemy()
        enemy_list.append(enemy)

    # Begin the loop where the game operates - Quit loop when user runs out of lives
    while user.lives != 0:

        # Quit the game if QUIT is initiated
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key inputs
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            user.move(1)
        if key[pygame.K_LEFT]:
            user.move(-1)

        # Update screen and draw sprites



# Create method holding all "update" actions
def update(enemy_list, user):
    for enemy in enemy_list:
        enemy.draw(game_view)

    user.draw(game_view)

    pygame.display.update()
    clock.tick(90)
