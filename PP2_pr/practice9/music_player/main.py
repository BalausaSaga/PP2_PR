import pygame
import sys
from player import MusicPlayer

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

player = MusicPlayer("music") # Указываем папку с музыкой

print("P - Play, S - Stop, N - Next, B - Back")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: player.play()
            if event.key == pygame.K_s: player.stop()
            if event.key == pygame.K_n: player.next()
            if event.key == pygame.K_b: player.prev()

    screen.fill((100, 100, 250)) # Синий фон
    pygame.display.flip()