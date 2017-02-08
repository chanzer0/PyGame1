import os
import pygame
import random


# Create class for Player(user-controlled)
class Player(object):
    def __init__(self):
        x = 400
        y = 500
        self.rect = pygame.Rect(x - 16, y - 16, 32, 32)

    def move(self, dx,):
        self.rect.x += dx

    def projectile(self, x, y, dy):
        self.rect = pygame.Rect(x, y, 8, 16)
        self.rect.y += dy

    def lives(self, lives):
        self.lives += lives


# Create class for Enemy(AI-controlled)
class Enemy(object):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def projectile(self, x, y, dy):
        self.rect = pygame.Rect(x, y, 8, 16)
        self.rect.y += dy

# Center the game window & start the environment
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


# Set up the display
pygame.display.set_caption("Kill all enemies while avoiding their projectiles")
gameView = pygame.display.set_mode((800, 600))


# Get clock values & initialize user and AI variables
clock = pygame.time.Clock()
user = Player()
enemy1 = Enemy(1, 1)
enemy2 = Enemy(1, 1)
enemy3 = Enemy(1, 1)


# Begin the loop where the game lives
while Player.lives != 0:

    # Quit the game if either QUIT or Esc. key are initiated
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Player.lives(user, -3)
        if event.type == pygame.K_ESCAPE:
            Player.lives(user, -3)

    # Use arrow keys to move player left & right
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        Player.move(user, -1)
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        Player.move(user, 1)
