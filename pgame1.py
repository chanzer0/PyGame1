import os
import pygame
import random


# Create class for Player(user-controlled)
class Player(object):
    lives = 3

    def __init__(self):
        self.x = 400
        self.y = 550
        self.rect = pygame.Rect(self.x - 12, self.y - 12, 24, 24)
        self.projectile = pygame.Rect(self.x, self.y, 4, 12)

    def move(self, dx):
        self.rect.x += dx

    def projectile(self, x, y, dy):
        self.projectile = pygame.Rect(x, y, 4, 8)
        self.projectile.y += dy

    def remove_life(self, lives):
        self.lives -= lives


# Create class for Enemy(AI-controlled)
class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 16, 16)
        self.projectile = pygame.Rect(self.x, self.y, 4, 12)

    def move(self, dx, dy):
            self.rect.x += dx

    def projectile(self, x, y, dy):
        self.rect = pygame.Rect(x, y, 4, 8)
        self.rect.y += dy

# Center the game window & start the environment
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


# Set up the display
pygame.display.set_caption("Shoot enemies while avoiding their projectiles")
game_view = pygame.display.set_mode((800, 600))


# Get clock values & initialize user variable
clock = pygame.time.Clock()
user = Player()
i = 0
_x = 1
_y = 1

# Initiate 3 random AI enemies
rand_x = random.randint(0, 800)
rand_y = random.randint(0, 400)
enemy1 = Enemy(rand_x, rand_y)

rand_x = random.randint(0, 800)
rand_y = random.randint(0, 400)
enemy2 = Enemy(rand_x, rand_y)

rand_x = random.randint(0, 800)
rand_y = random.randint(0, 400)
enemy3 = Enemy(rand_x, rand_y)

rand_x = random.randint(0, 800)
rand_y = random.randint(0, 400)
enemy4 = Enemy(rand_x, rand_y)


# Begin the loop where the game operates - Quit loop when user runs out of lives
while user.lives != 0:

    # Quit the game if either QUIT or Esc. key are initiated
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        user.lives = 0
    if event.type == pygame.K_ESCAPE:
        user.lives = 0

    # Use arrow keys to move player left & right
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        Player.move(user, -1)
    if key[pygame.K_RIGHT]:
        Player.move(user, 1)

    # Update AI positions every 10 iterations
    if i % random.randint(1000, 10000) == 0:
        _x = -_x
        _y = -_y

    if i % 10 == 0:
        enemy1.move(_x, _y)
        enemy2.move(_x, _y)
        enemy3.move(_x, _y)
        enemy4.move(_x, _y)

    # Populate the game_view
    game_view.fill((20, 20, 20))
    pygame.draw.rect(game_view, (180, 180, 180), user.rect)
    pygame.draw.rect(game_view, (200, 150, 0), enemy1.rect)
    pygame.draw.rect(game_view, (200, 150, 0), enemy2.rect)
    pygame.draw.rect(game_view, (200, 150, 0), enemy3.rect)
    pygame.display.flip()
    i += 1

pygame.quit()
