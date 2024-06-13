

import pygame


class Button:
    def __init__(self, hit_box: pygame.Rect) -> None:
        self.hit_box = hit_box
    
    def update(self):
        pass
    
    def draw(self, surface: pygame.Surface):
        pass
    
    def key_down(self ,event: pygame.event.Event):
        pass
            
    def key_up(self ,event: pygame.event.Event):
        pass
                
    def mouse_down(self ,event: pygame.event.Event):
        pass
            
    def mouse_up(self ,event: pygame.event.Event):
        pass
    
    def mouse_motion(self ,event: pygame.event.Event):
        pass