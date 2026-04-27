import pygame

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

def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    active_scene = starting_scene

    while active_scene is not None:
        pressed_keys = pygame.key.get_pressed()
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.SwitchToScene(GameScene())
    
    def Render(self, screen):
        screen.fill((50, 50, 50))
        # Simple label for visual appeal
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Press ENTER to Start Paint", True, (255, 255, 255))
        screen.blit(text, (50, 130))

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.canvas = pygame.Surface((400, 300)) # Drawing canvas
        self.canvas.fill((255, 255, 255))         # White background
        self.mode = 'brush'                       # Current tool
        self.color = (0, 0, 0)                    # Current color (black)
        self.start_pos = None                     # Starting point for shapes
        self.radius = 5

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            # Color switching
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: self.color = (255, 0, 0)
                if event.key == pygame.K_g: self.color = (0, 255, 0)
                if event.key == pygame.K_b: self.color = (0, 0, 255)
                
                # Tool switching
                if event.key == pygame.K_1: self.mode = 'brush'
                if event.key == pygame.K_2: self.mode = 'rect'
                if event.key == pygame.K_3: self.mode = 'circle'
                if event.key == pygame.K_4: self.mode = 'eraser'

            # Drawing logic
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left mouse button
                    self.start_pos = event.pos
            
            if event.type == pygame.MOUSEMOTION:
                if self.start_pos and (self.mode == 'brush' or self.mode == 'eraser'):
                    draw_color = self.color if self.mode == 'brush' else (255, 255, 255)
                    pygame.draw.circle(self.canvas, draw_color, event.pos, self.radius)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.start_pos:
                    end_pos = event.pos
                    if self.mode == 'rect':
                        width = abs(end_pos[0] - self.start_pos[0])
                        height = abs(end_pos[1] - self.start_pos[1])
                        top_left = (min(self.start_pos[0], end_pos[0]), min(self.start_pos[1], end_pos[1]))
                        pygame.draw.rect(self.canvas, self.color, (top_left[0], top_left[1], width, height), 2)
                    
                    elif self.mode == 'circle':
                        # Calculate radius as distance between points
                        radius = int(((end_pos[0]-self.start_pos[0])**2 + (end_pos[1]-self.start_pos[1])**2)**0.5)
                        pygame.draw.circle(self.canvas, self.color, self.start_pos, radius, 2)
                    
                    self.start_pos = None

    def Render(self, screen):
        screen.blit(self.canvas, (0, 0))
        # Small info panel in the corner
        font = pygame.font.SysFont("Arial", 14)
        info = font.render(f"Tool: {self.mode} | RGB for Colors | 1-4 for Tools", True, (100, 100, 100))
        screen.blit(info, (5, 5))

run_game(400, 300, 60, TitleScene())