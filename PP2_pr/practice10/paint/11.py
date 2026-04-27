import pygame
import math

# Base class for scenes to manage game states
class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        pass

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

# Main game loop handler
def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    active_scene = starting_scene

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

# Initial screen before starting the paint app
class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(GameScene())
    
    def Render(self, screen):
        screen.fill((40, 40, 40))
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("PAINT PRO: Press ENTER to Start", True, (255, 255, 255))
        screen.blit(text, (200 // 4, 300 // 2))

# Main painting logic scene
class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.canvas = pygame.Surface((800, 600)) # Persistent surface for drawing
        self.canvas.fill((255, 255, 255))         # White background for the canvas
        self.mode = 'brush'                       # Default tool
        self.color = (0, 0, 0)                    # Default color (Black)
        self.start_pos = None                     # Initial click position for shapes
        self.radius = 10                          # Brush and Eraser size

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            # Color selection and tool switching via keyboard
            if event.type == pygame.KEYDOWN:
                # RGB Colors
                if event.key == pygame.K_r: self.color = (255, 0, 0)
                if event.key == pygame.K_g: self.color = (0, 255, 0)
                if event.key == pygame.K_b: self.color = (0, 0, 255)
                
                # Tool Selection (1-8)
                if event.key == pygame.K_1: self.mode = 'brush'
                if event.key == pygame.K_2: self.mode = 'rect'
                if event.key == pygame.K_3: self.mode = 'circle'
                if event.key == pygame.K_4: self.mode = 'eraser'
                if event.key == pygame.K_5: self.mode = 'square'
                if event.key == pygame.K_6: self.mode = 'right_tr'
                if event.key == pygame.K_7: self.mode = 'equal_tr'
                if event.key == pygame.K_8: self.mode = 'rhombus'

            # Record starting position on mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.start_pos = event.pos
            
            # Continuous drawing for Brush and Eraser
            if event.type == pygame.MOUSEMOTION:
                if self.start_pos and (self.mode == 'brush' or self.mode == 'eraser'):
                    # Eraser simply draws with the background color (white)
                    draw_color = self.color if self.mode == 'brush' else (255, 255, 255)
                    pygame.draw.circle(self.canvas, draw_color, event.pos, self.radius)

            # Finalize shape drawing on mouse release
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.start_pos:
                    x1, y1 = self.start_pos
                    x2, y2 = event.pos
                    
                    # Draw Rectangle
                    if self.mode == 'rect':
                        pygame.draw.rect(self.canvas, self.color, (min(x1, x2), min(y1, y2), abs(x1-x2), abs(y1-y2)), 2)
                    
                    # Draw Circle based on distance between points
                    elif self.mode == 'circle':
                        rad = int(((x1-x2)**2 + (y1-y2)**2)**0.5)
                        pygame.draw.circle(self.canvas, self.color, (x1, y1), rad, 2)
                    
                    # Draw Square (equal sides)
                    elif self.mode == 'square':
                        side = max(abs(x1-x2), abs(y1-y2))
                        pygame.draw.rect(self.canvas, self.color, (x1 if x2 > x1 else x1-side, y1 if y2 > y1 else y1-side, side, side), 2)
                    
                    # Draw Right Triangle
                    elif self.mode == 'right_tr':
                        pygame.draw.polygon(self.canvas, self.color, [(x1, y1), (x1, y2), (x2, y2)], 2)
                    
                    # Draw Equilateral Triangle using height formula
                    elif self.mode == 'equal_tr':
                        side = abs(x1-x2)
                        h = int((math.sqrt(3)/2) * side)
                        pygame.draw.polygon(self.canvas, self.color, [(x1, y1), (x1-side//2, y1+h), (x1+side//2, y1+h)], 2)
                        
                    # Draw Rhombus
                    elif self.mode == 'rhombus':
                        dx, dy = abs(x1-x2), abs(y1-y2)
                        points = [(x1, y1-dy), (x1+dx, y1), (x1, y1+dy), (x1-dx, y1)]
                        pygame.draw.polygon(self.canvas, self.color, points, 2)
                    
                    self.start_pos = None

    def Render(self, screen):
        screen.blit(self.canvas, (0, 0)) # Display the canvas
        # Status bar for user instructions
        font = pygame.font.SysFont("Arial", 14)
        info = font.render(f"Tool: {self.mode} | 1-8:Tools | R/G/B:Colors", True, (120, 120, 120))
        screen.blit(info, (10, 10))

# Execute the game
width, height = 800, 600
run_game(width, height, 60, TitleScene())