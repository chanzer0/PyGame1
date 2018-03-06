import pygame

# Define constants
WHITE = (255, 255, 255)


# Class for projectiles shot by user or enemy
class Projectile(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Sean/Documents/Python/Space-Invaders/assets/bullet.png").convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.direction = direction

    def update(self):
        if self.direction == "up":
            self.rect.y -= 5
        if self.direction == "down":
            self.rect.y += 5
