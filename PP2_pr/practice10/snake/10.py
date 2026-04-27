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
pygame.display.set_caption('Snake Game')

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
        # Logic 1: Check if snake hits the boundaries
        if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
            return True
        return False

class Food:
    def __init__(self, snake_body):
        self.pos = Point(0, 0)
        self.generate_random_pos(snake_body)

    def draw(self):
        # Render green food
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        # Logic 2: Generate random food position ensuring it doesn't spawn on the snake
        while True:
            self.pos.x = random.randint(0, (WIDTH // CELL) - 1)
            self.pos.y = random.randint(0, (HEIGHT // CELL) - 1)
            
            # Check for overlap with the snake body
            overlap = False
            for segment in snake_body:
                if segment.x == self.pos.x and segment.y == self.pos.y:
                    overlap = True
                    break
            if not overlap:
                break

# Game state variables
FPS = 5
score = 0
level = 1
foods_per_level = 3 # Logic 3: Condition for leveling up

clock = pygame.time.Clock()
snake = Snake()
food = Food(snake.body)

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Prevent snake from moving directly opposite to current direction
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1

    # Movement and collision checks
    snake.move()

    # Logic 1: Collision with wall ends the game
    if snake.check_border_collision():
        running = False

    # Check for food collection
    head = snake.body[0]
    if head.x == food.pos.x and head.y == food.pos.y:
        score += 1
        snake.body.append(Point(head.x, head.y)) # Grow snake
        food.generate_random_pos(snake.body)     # New food location
        
        # Logic 3 & 4: Increase level and speed
        if score % foods_per_level == 0:
            level += 1
            FPS += 2 

    # Drawing section
    screen.fill(colorBLACK)
    
    # Grid lines (optional visual aid)
    for i in range(0, WIDTH, CELL):
        pygame.draw.line(screen, colorGRAY, (i, 0), (i, HEIGHT))
    for i in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, colorGRAY, (0, i), (WIDTH, i))

    snake.draw()
    food.draw()

    # Logic 5: Render score and level on screen
    score_text = font.render(f"Score: {score}", True, colorWHITE)
    level_text = font.render(f"Level: {level}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()