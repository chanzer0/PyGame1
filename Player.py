import pygame

# Define constants
WHITE = (255, 255, 255)


# Class for user-controlled sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Sean/Documents/Python/Space-Invaders/assets/m_falcon.png").convert_alpha()
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
