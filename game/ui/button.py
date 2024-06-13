import pygame

from game.entities.entity import Entity
from game.lib.inputs import Mouse_events

class Button(Entity, Mouse_events):
    def __init__(self, hit_box: pygame.Rect) -> None:
        self.hit_box = hit_box
        self.is_mouse_down = False
        self.is_hover = False
    
    def update(self):
        pass
    
    def draw(self, surface: pygame.Surface):
        pass
                
    def mouse_down(self ,event: pygame.event.Event):
        x,y = pygame.mouse.get_pos()
        
        if self.hit_box.collidepoint(x, y):
            self.is_mouse_down = True
            
    def mouse_up(self ,event: pygame.event.Event):
        x,y = pygame.mouse.get_pos()
        
        if self.hit_box.collidepoint(x, y) and self.is_mouse_down:
            self.on_click()
            
        self.is_mouse_down = False
    
    def mouse_motion(self ,event: pygame.event.Event):
        x,y = pygame.mouse.get_pos()
        
        is_mouse_collide = self.hit_box.collidepoint(x, y)
        
        if is_mouse_collide:
            if not self.is_hover:
                self.on_mouse_over()
                self.is_hover = True
            return
            
        if self.is_hover:
            self.on_mouse_out()
            self.is_hover = False
        
    def on_mouse_over(self):
        pass
    
    def on_mouse_out(self):
        pass
    
    def on_click(self):
        pass