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
SCORE = 0 
COINS_COLLECTED = 0 

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)
GOLD = (218, 165, 32)

# Fonts
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# Window and timer setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()
FPS = 60

# 2. Loading Resources
background = pygame.image.load("AnimatedStreet.png")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)
crash_sound = pygame.mixer.Sound("crash.wav")

# 3. Game Object Classes

class Enemy(pygame.sprite.Sprite):
    """Enemy car class with movement based on global SPEED"""
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
    """Coin class with random weights for Practice 11"""
    def __init__(self):
        super().__init__()
        # Random weight: 1 or 3
        self.weight = random.choices([1, 3], weights=[80, 20])[0]
        size = 20 if self.weight == 1 else 35
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        color = YELLOW if self.weight == 1 else GOLD
        pygame.draw.circle(self.image, color, (size//2, size//2), size//2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    """Player car controlled by arrows"""
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

# 4. Creating objects
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

    screen.blit(background, (0, 0))
    
    # UI: Displaying Score and Speed
    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    speed_text = font_small.render(f"Speed: {SPEED}", True, BLACK)
    
    # Background for UI text
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 110, 5, 100, 55))
    screen.blit(score_text, (SCREEN_WIDTH - 100, 10))
    screen.blit(speed_text, (SCREEN_WIDTH - 100, 35))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Collision with Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        crash_sound.play()
        
        screen.fill(RED)
        game_over = font_big.render("GAME OVER", True, BLACK)
        final_score = font_small.render(f"Total Score: {SCORE}", True, BLACK)
        screen.blit(game_over, (30, 250))
        screen.blit(final_score, (120, 350))
        
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Coin Collection Logic
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collided_coins:
        SCORE += coin.weight
        COINS_COLLECTED += 1
        
        # Increase speed every 5 coins collected
        if COINS_COLLECTED % 5 == 0:
            SPEED += 1
            
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    pygame.display.update()
    clock.tick(FPS)