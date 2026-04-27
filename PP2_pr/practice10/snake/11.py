import pygame
from color_palette import *
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game - Advanced Food')

# Font for score and level display
font = pygame.font.SysFont("Verdana", 20)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        # Initial snake position and direction
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    def move(self):
        # Move body segments following the head
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Update head position
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        # Render snake: Red head and Yellow body
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_border_collision(self):
        head = self.body[0]
        # Logic: Check if snake hits the boundaries
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            return True
        return False

class Food:
    def __init__(self, snake_body):
        self.pos = Point(0, 0)
        self.weight = 1
        self.timer = 0
        self.lifetime = 5000 # 5 seconds in milliseconds
        self.generate_random_pos(snake_body)

    def draw(self):
        # Render food: Color depends on weight
        color = colorGREEN if self.weight == 1 else colorBLUE
        pygame.draw.rect(screen, color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        # New Task 1: Randomly generate food with different weights
        self.weight = random.choice([1, 2, 3])
        
        # New Task 2: Reset timer when food is generated
        self.timer = pygame.time.get_ticks()
        
        while True:
            self.pos.x = random.randint(0, (WIDTH // CELL) - 1)
            self.pos.y = random.randint(0, (HEIGHT // CELL) - 1)
            
            overlap = False
            for segment in snake_body:
                if segment.x == self.pos.x and segment.y == self.pos.y:
                    overlap = True
                    break
            if not overlap:
                break

    def check_timer(self, snake_body):
        # New Task 2: Food disappears after some time
        current_time = pygame.time.get_ticks()
        if current_time - self.timer > self.lifetime:
            self.generate_random_pos(snake_body)

# Game state variables
FPS = 5
score = 0
level = 1
foods_per_level = 3 

clock = pygame.time.Clock()
snake = Snake()
food = Food(snake.body)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1

    snake.move()

    if snake.check_border_collision():
        running = False

    # Task 2: Update food timer every frame
    food.check_timer(snake.body)

    # Check for food collection
    head = snake.body[0]
    if head.x == food.pos.x and head.y == food.pos.y:
        # Task 1: Add weight to score
        score += food.weight
        snake.body.append(Point(head.x, head.y))
        food.generate_random_pos(snake.body)
        
        if score // foods_per_level >= level:
            level += 1
            FPS += 2 

    screen.fill(colorBLACK)
    
    # Grid lines
    for i in range(0, WIDTH, CELL):
        pygame.draw.line(screen, colorGRAY, (i, 0), (i, HEIGHT))
    for i in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, colorGRAY, (0, i), (WIDTH, i))

    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()