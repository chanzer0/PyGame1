import os
import pygame


# Create class for Player(user-controlled)
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Sean/PycharmProjects/PyGame1/millenium_falcon.png").convert()
        self.rect = self.image.get_rect()


# Center the game window & start the environment
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


# Set up the display
pygame.display.set_caption("~~ Shoot enemies while avoiding their projectiles ~~")
screen_width = 800
screen_height = 600
game_view = pygame.display.set_mode([screen_width, screen_height])
game_view.fill((20, 20, 20))
game_view_rect = game_view.get_rect()


# Update screen
game_view.convert()
pygame.display.flip()