import pygame

# Define constants
WHITE = (255, 255, 255)


# Class for enemy sprites
class Enemy(pygame.sprite.Sprite):

    def __init__(self, height, width):
        super().__init__()
        self.temp = pygame.image.load("C:/Users/Sean/Documents/Python/Space-Invaders/assets/t_fighter.png").convert_alpha()
        self.image = pygame.Surface([height, width])
        pygame.transform.scale(self.temp, (height, width), self.image)

        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)

    def set_xy(self, x, y):
        self.rect.x = x
        self.rect.y = y

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
