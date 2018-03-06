import pygame

# Define constants
WHITE = (255, 255, 255)


# Class for enemy sprites
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Sean/Documents/Python/Space-Invaders/assets/t_fighter.png").convert_alpha()
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
