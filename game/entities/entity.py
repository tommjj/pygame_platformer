import pygame


class Entity:
    hit_box: pygame.Rect
    
    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        pass
    
    def set_pos(self, x : float, y: float):
        pass
    
    def get_hit_box(self):
        return self.hit_box