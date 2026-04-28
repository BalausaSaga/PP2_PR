import pygame
import math
from datetime import datetime

# --- Scene Management ---
# Simplified classes to keep the structure professional but clear
class SceneBase:
    def __init__(self):
        self.next = self
    def ProcessInput(self, events, pressed_keys): pass
    def Update(self): pass
    def Render(self, screen): pass
    def Terminate(self): self.next = None

class TitleScene(SceneBase):
    def __init__(self):
        super().__init__()
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.next = GameScene() # Start the paint
    def Render(self, screen):
        screen.fill((30, 30, 30))
        font = pygame.font.SysFont("Arial", 32)
        text = font.render("PAINT PRO: Press ENTER to Start", True, (255, 255, 255))
        screen.blit(text, (180, 280))

class GameScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.canvas = pygame.Surface((800, 600))
        self.canvas.fill((255, 255, 255))
        self.mode = 'pencil' 
        self.color = (0, 0, 0)
        self.thickness = 2
        self.start_pos = None
        self.last_pos = None
        
        # Text tool helpers
        self.typing = False
        self.text_input = ""
        self.text_pos = (0, 0)
        self.font_main = pygame.font.SysFont("Arial", 24)
        self.font_ui = pygame.font.SysFont("Arial", 18)

    def flood_fill(self, x, y, new_color):
        # Basic stack-based flood fill algorithm
        target = self.canvas.get_at((x, y))
        if target == new_color: return
        pixels = [(x, y)]
        while pixels:
            cx, cy = pixels.pop()
            if 0 <= cx < 800 and 0 <= cy < 600:
                if self.canvas.get_at((cx, cy)) == target:
                    self.canvas.set_at((cx, cy), new_color)
                    pixels.extend([(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)])

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                # Save functionality (Ctrl + S)
                if event.key == pygame.K_s and (pressed_keys[pygame.K_LCTRL] or pressed_keys[pygame.K_RCTRL]):
                    pygame.image.save(self.canvas, f"image_{datetime.now().strftime('%H%M%S')}.png")

                # Text input handling
                if self.typing:
                    if event.key == pygame.K_RETURN:
                        surf = self.font_main.render(self.text_input, True, self.color)
                        self.canvas.blit(surf, self.text_pos)
                        self.typing = False
                    elif event.key == pygame.K_BACKSPACE: self.text_input = self.text_input[:-1]
                    else: self.text_input += event.unicode
                    continue

                # Color switching
                if event.key == pygame.K_r: self.color = (255, 0, 0)
                if event.key == pygame.K_g: self.color = (0, 255, 0)
                if event.key == pygame.K_b: self.color = (0, 0, 255)

                # Thickness switching (F1, F2, F3)
                if event.key == pygame.K_F1: self.thickness = 2
                if event.key == pygame.K_F2: self.thickness = 5
                if event.key == pygame.K_F3: self.thickness = 10

                # Tool mapping
                keys = {pygame.K_1:'pencil', pygame.K_2:'line', pygame.K_3:'rect', 
                        pygame.K_4:'circle', pygame.K_5:'square', pygame.K_6:'right_tr', 
                        pygame.K_7:'equal_tr', pygame.K_8:'rhombus', pygame.K_9:'fill', 
                        pygame.K_0:'text', pygame.K_e:'eraser'}
                if event.key in keys: self.mode = keys[event.key]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mode == 'fill': self.flood_fill(event.pos[0], event.pos[1], self.color)
                elif self.mode == 'text':
                    self.typing = True
                    self.text_pos, self.text_input = event.pos, ""
                else:
                    self.start_pos = self.last_pos = event.pos

            if event.type == pygame.MOUSEMOTION and self.start_pos:
                if self.mode == 'pencil':
                    pygame.draw.line(self.canvas, self.color, self.last_pos, event.pos, self.thickness)
                    self.last_pos = event.pos
                elif self.mode == 'eraser':
                    pygame.draw.circle(self.canvas, (255, 255, 255), event.pos, self.thickness * 4)

            if event.type == pygame.MOUSEBUTTONUP and self.start_pos:
                x1, y1 = self.start_pos
                x2, y2 = event.pos
                if self.mode == 'line': pygame.draw.line(self.canvas, self.color, (x1, y1), (x2, y2), self.thickness)
                elif self.mode == 'rect': pygame.draw.rect(self.canvas, self.color, (min(x1, x2), min(y1, y2), abs(x1-x2), abs(y1-y2)), self.thickness)
                elif self.mode == 'circle':
                    r = int(math.hypot(x1-x2, y1-y2))
                    pygame.draw.circle(self.canvas, self.color, (x1, y1), r, self.thickness)
                elif self.mode == 'square':
                    s = max(abs(x1-x2), abs(y1-y2))
                    pygame.draw.rect(self.canvas, self.color, (x1, y1, s if x2 > x1 else -s, s if y2 > y1 else -s), self.thickness)
                elif self.mode == 'right_tr': pygame.draw.polygon(self.canvas, self.color, [(x1, y1), (x1, y2), (x2, y2)], self.thickness)
                elif self.mode == 'equal_tr':
                    side = abs(x1-x2)
                    h = int((math.sqrt(3)/2) * side)
                    pygame.draw.polygon(self.canvas, self.color, [(x1, y1), (x1-side//2, y1+h), (x1+side//2, y1+h)], self.thickness)
                elif self.mode == 'rhombus':
                    dx, dy = abs(x1-x2), abs(y1-y2)
                    pygame.draw.polygon(self.canvas, self.color, [(x1, y1-dy), (x1+dx, y1), (x1, y1+dy), (x1-dx, y1)], self.thickness)
                self.start_pos = None

    def Render(self, screen):
        screen.blit(self.canvas, (0, 0))
        if self.start_pos and self.mode == 'line':
            pygame.draw.line(screen, self.color, self.start_pos, pygame.mouse.get_pos(), self.thickness)
        if self.typing:
            screen.blit(self.font_main.render(self.text_input + "|", True, self.color), self.text_pos)
        
        # UI Status bar at the top
        status = f"MODE: {self.mode.upper()} | SIZE: {self.thickness} | COLOR: {self.color}"
        txt = self.font_ui.render(status, True, (50, 50, 50))
        screen.blit(txt, (10, 10))

# --- Main Game Execution ---
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
active_scene = TitleScene()

while active_scene is not None:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: active_scene.Terminate()
    
    active_scene.ProcessInput(events, pygame.key.get_pressed())
    active_scene.Render(screen)
    active_scene = active_scene.next
    pygame.display.flip()
    clock.tick(60)