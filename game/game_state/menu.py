
import pygame

from game.game_state.state import Game_state
from game.levels.background import draw_background
from game.lib.inputs import Key_events, Mouse_events


class Game_menu(Key_events, Mouse_events):
    def __init__(self, game) -> None:
        self.game = game
    
    def draw(self, surface: pygame.Surface):
        draw_background(surface, 0)
    
    def update(self):
        pass
    
    def key_down(self ,event: pygame.event.Event):
        pass
            
    def key_up(self ,event: pygame.event.Event):
        self.game.set_state(Game_state.playing)
        
    def mouse_down(self ,event: pygame.event.Event):
        pass
            
    def mouse_up(self ,event: pygame.event.Event):
        pass
    
    def mouse_motion(self ,event: pygame.event.Event):
        pass
    