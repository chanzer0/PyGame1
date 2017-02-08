import os
import pygame

# Create class for projectile
class Projectile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - 2, self.y - 2, 4, 12)

    def launch_projectile(self):
        self.rect.y -= 5

    def draw(self, view):
        pygame.draw.rect(view, (255, 0, 0), self.rect)


# Create class for Player(user-controlled)
class Player(object):
    def __init__(self):
        self.lives = 3
        self.x = 400
        self.y = 550
        self.rect = pygame.Rect(self.x - 12, self.y - 12, 24, 24)

    def move(self, dx):
        self.rect.x += dx
        self.rect.clamp_ip(game_view_rect)

    def remove_life(self, lives):
        self.lives -= lives

    def draw(self, view):
        pygame.draw.rect(view, (200, 0, 200), self.rect)

# Create class for Enemy(AI-controlled)
class Enemy(object):
    def __init__(self, x, y, dx):
        self.dx = dx
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 16, 16)

    def move(self):
        if 0 <= self.rect.x <= 784:
            if self.rect.x == 784:
                self.dx = -self.dx
            if self.rect.x == 0:
                self.dx = -self.dx
        self.rect.x += self.dx

    def draw(self, view):
        pygame.draw.rect(view, (200, 150, 0), self.rect)

# Create module to update the screen
def update():
    game_view.convert()
    game_view.fill((20, 20, 20))
    user.draw(game_view)
    enemy1.draw(game_view)
    enemy2.draw(game_view)
    enemy3.draw(game_view)
    enemy4.draw(game_view)
    user_projectile.draw(game_view)
    pygame.display.flip()


# --------------------------------------------------------------------- #


# Center the game window & start the environment
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()


# Set up the display
pygame.display.set_caption("~~ Shoot enemies while avoiding their projectiles ~~")
game_view = pygame.display.set_mode((800, 600))
game_view_rect = game_view.get_rect()


# Initiate user and AI sprites
user = Player()
enemy1 = Enemy(1, 1, 1)
enemy2 = Enemy(200, 100, 4)
enemy3 = Enemy(400, 200, 2)
enemy4 = Enemy(600, 300, 4)
i = 0
j = 0
user_projectile = Projectile(0, 0)

# Create a list of projectiles to be fired later
projectiles = []
for count in range(1500):
    projectiles.append(Projectile(0, 0))

# Begin the loop where the game operates - Quit loop when user runs out of lives
while user.lives != 0:

    # Quit the game if either QUIT or Esc. key are initiated
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        user.remove_life(3)
    if event.type == pygame.K_ESCAPE:
        user.remove_life(3)

    # Use arrow keys to move player left & right
    key = pygame.key.get_pressed()
    if 0 <= user.rect.x <= 800:
        if key[pygame.K_LEFT]:
            user.move(-1)
        if key[pygame.K_RIGHT]:
            user.move(1)
        if key[pygame.K_SPACE]:
            user_projectile = projectiles[j]
            j += 1

    # Update AI positions every 10 iterations
    if i % 10 == 0:
        enemy1.move()
        enemy2.move()
        enemy3.move()
        enemy4.move()

    # Fire projectiles at user

    # Populate the game_view
    update()
    i += 1

pygame.quit()
