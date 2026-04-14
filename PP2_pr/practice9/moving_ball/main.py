import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 25
ball_x = WIDTH // 2 
ball_y = HEIGHT // 2
velocity = 20       

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - velocity >= ball_radius:
                    ball_y -= velocity
            if event.key == pygame.K_DOWN:
                if ball_y + velocity <= HEIGHT - ball_radius:
                    ball_y += velocity
            if event.key == pygame.K_LEFT:
                if ball_x - velocity >= ball_radius:
                    ball_x -= velocity
            if event.key == pygame.K_RIGHT:
                if ball_x + velocity <= WIDTH - ball_radius:
                    ball_x += velocity

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()