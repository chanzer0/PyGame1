import os
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (30, 30, 30)


# Create class for the background
class Background(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.image = pygame.image.load(location)
        self.rect = self.image.get_rect()

# Create class for Player(user-controlled)
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.image.load("C:/Users/seans/PycharmProjects/PyGame1/millenium_falcon.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.lives = 3

    def remove_life(self, lives):
        self.lives -= lives


# Create class for enemy("AI"-controlled)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.image.load("C:/Users/seans/PycharmProjects/PyGame1/tie_fighter.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

# Center the game window & start the environment
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


# Set up the display
pygame.display.set_caption("Shoot enemies while avoiding their projectiles")
screen_width = 1024
screen_height = 768
game_view = pygame.display.set_mode([screen_width, screen_height])
game_view_rect = game_view.get_rect()
background = Background('C:')

# Create user avatar
height = 128
width = 128
user = Player(WHITE, height, width)
user.rect.x = (screen_width * 0.5) - (width / 2)
user.rect.y = (screen_height * 0.9) - (height / 2)

# Create enemies
enemy1 = Enemy(WHITE, height, width)


# List of all game objects
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(user)

# Begin the loop where the game operates - Quit loop when user runs out of lives
while user.lives != 0:

    # Quit the game if QUIT is initiated
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        user.remove_life(3)

    all_sprites_list.update()

    key = pygame.key.get_pressed()

    game_view.convert()
    game_view.fill(GREY)
    game_view.blit(user.image, user.rect)
    pygame.display.flip()