import pygame
import sys
import random
from pygame.locals import *

# 1. Pygame Initialization
pygame.init()

# Screen Settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COINS_COLLECTED = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)

# Fonts for text rendering
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# Window and timer setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game - Practice 10")
clock = pygame.time.Clock()
FPS = 60

# 2. Loading Resources (Images and Sounds)
background = pygame.image.load("AnimatedStreet.png")

# Background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1) 

# Crash sound
crash_sound = pygame.mixer.Sound("crash.wav")

# 3. Game Object Classes

class Enemy(pygame.sprite.Sprite):
    """Class for enemy cars (red car)"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Coin(pygame.sprite.Sprite):
    """Class for collectible coins (Task 1)"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (15, 15), 15)
        pygame.draw.circle(self.image, (184, 134, 11), (15, 15), 15, 2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    """Player class (blue car)"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# 4. Creating objects and groups
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# 5. Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    screen.blit(background, (0, 0))
    
    # Show coin counter (Task 2)
    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 110, 5, 100, 30))
    screen.blit(coin_text, (SCREEN_WIDTH - 100, 10))

    # Update positions and render all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Check for enemy collision (Game Over logic)
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        crash_sound.play()
        
        # Displaying Game Over screen
        screen.fill(RED)
        game_over = font_big.render("GAME OVER", True, BLACK)
        total_coins = font_small.render(f"Total coins: {COINS_COLLECTED}", True, BLACK)
        screen.blit(game_over, (30, 250))
        screen.blit(total_coins, (80, 350))
        
        pygame.display.update()
        pygame.time.delay(2000) # Wait to show score
        
        pygame.quit()
        sys.exit()

    # Coin collection logic
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        COINS_COLLECTED += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    clock.tick(FPS)