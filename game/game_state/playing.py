import pygame

from game.entities.player import Player
from game.levels.level_manager import Levels_manager


class Playing:
    player = None
    level_manager = None
    
    def __init__(self, game) -> None:
        self.player = Player(self)
        self.level_manager = Levels_manager(self)
        
    def set_level(self):
        pass
        
    def update(self):
        self.player.update()
        self.level_manager.update()
    
    def draw(self, surface: pygame.Surface):
        self.level_manager.draw_background(surface)
        self.level_manager.draw_tiles(surface)
        
        self.player.draw(surface)
    
    def key_down(self ,event: pygame.event.Event):
        self.player.key_down(event)
        if event.key == pygame.K_r:
            self.level_manager.reset()
            
    def key_up(self ,event: pygame.event.Event):
        self.player.key_up(event)
        
    def mouse_down(self ,event: pygame.event.Event):
        pass
            
    def mouse_up(self ,event: pygame.event.Event):
        pass
        