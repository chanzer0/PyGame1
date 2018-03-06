import os
import pygame
import sys
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (30, 30, 30)
clock = pygame.time.Clock()
time = pygame.time.get_ticks()
score = 0


# Create class for Projectile
class Projectile(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.image = pygame.image.load("C:/Users/seans/PycharmProjects/PyGame1/bullet.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.direction = direction

    def update(self):
        if self.direction == "up":
            self.rect.y -= 5
        if self.direction == "down":
            self.rect.y += 5

# Create class for Player(user-controlled)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/seans/PycharmProjects/PyGame1/millenium_falcon.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.lives = 3

    def remove_life(self, lives):
        self.lives -= lives

    def move(self, a):
        if a == 1 and self.rect.right < 1024:
            self.rect.x += 5
        if a == -1 and self.rect.left > 0:
            self.rect.x -= 5


# Create class for enemy("AI"-controlled)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/seans/PycharmProjects/PyGame1/tie_fighter.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def update(self, direction):
        dist = 3
        if direction == "left":
            self.rect.x -= dist
            if self.rect.left <= 0:
                self.rect.left = 1024
        if direction == "right":
            self.rect.x += dist
            if self.rect.left >= 1024:
                self.rect.right = 0


# Create method holding all "update" actions
def update():
    enemy1.update("left")
    enemy2.update("left")
    enemy3.update("left")
    enemy4.update("right")
    enemy5.update("right")

    score_text = my_font.render("Score " + str(score), 1, WHITE)
    game_view.blit(score_text, (5, height - 10))

    game_view.convert()
    game_view.fill(GREY)

    all_enemies.draw(game_view)
    user_list.draw(game_view)
    bullet_list.draw(game_view)

    bullet_list.update()
    pygame.display.flip()
    clock.tick(90)


# Center the game window & start the environment
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


# Set up the display
pygame.display.set_caption("Shoot the enemy tie fighters to escape the Imperial fleet")
screen_width = 1024
screen_height = 768
game_view = pygame.display.set_mode([screen_width, screen_height])
game_view_rect = game_view.get_rect()


# Create user avatar
height = 128
width = 128
user = Player()
user.rect.x = (screen_width * 0.5) - (width / 2)
user.rect.y = (screen_height * 0.9) - (height / 2)

# Create enemies
enemy1 = Enemy()
enemy1.rect.x = (screen_width * 0.25) - (width / 2)
enemy1.rect.y = (screen_height * 0.15) - (height / 2)

enemy2 = Enemy()
enemy2.rect.x = (screen_width * 0.5) - (width / 2)
enemy2.rect.y = (screen_height * 0.15) - (height / 2)

enemy3 = Enemy()
enemy3.rect.x = (screen_width * 0.75) - (width / 2)
enemy3.rect.y = (screen_height * 0.15) - (height / 2)

enemy4 = Enemy()
enemy4.rect.x = (screen_width * 0.33) - (width / 2)
enemy4.rect.y = (screen_height * 0.45) - (height / 2)

enemy5 = Enemy()
enemy5.rect.x = (screen_width * 0.66) - (width / 2)
enemy5.rect.y = (screen_height * 0.45) - (height / 2)

# Create bullet list
bullet_list = pygame.sprite.Group()


# List of all game objects
all_enemies = pygame.sprite.Group()
user_list = pygame.sprite.Group()
user_list.add(user)
all_enemies.add(enemy1)
all_enemies.add(enemy2)
all_enemies.add(enemy3)
all_enemies.add(enemy4)
all_enemies.add(enemy5)

# Create text to display lives and score
my_font = pygame.font.SysFont("monospace", 16)


# Begin the loop where the game operates - Quit loop when user runs out of lives
while user.lives != 0:

    # Quit the game if QUIT is initiated
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        user.remove_life(3)

    # Handle key inputs
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        user.move(1)
    if key[pygame.K_LEFT]:
        user.move(-1)
    if key[pygame.K_SPACE]:
        if pygame.time.get_ticks() - time >= 300:
            bullet = Projectile("up")
            bullet.rect.x = (user.rect.left + (user.rect.right - user.rect.left) / 2.65)
            bullet.rect.y = user.rect.top
            bullet_list.add(bullet)
            time = pygame.time.get_ticks()

    # Have enemies randomly shoot bullets

    # Handle collisions
    if pygame.sprite.groupcollide(bullet_list, all_enemies, True, True):
        score += 100

    # Update screen and draw sprites
    update()
