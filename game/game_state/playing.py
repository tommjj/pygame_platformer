import pygame

from game.entities.player import Player
from game.game_state.state import Game_state, State_control
from game.levels.level_manager import Levels_manager
from game.lib.inputs import Key_events, Mouse_events
from game.ui.life_bar import Life_bar

class Playing(Key_events, Mouse_events):
    player = None
    level_manager = None
    
    def __init__(self, game: State_control) -> None:
        self.game = game
        self.player = Player(self)
        self.level_manager = Levels_manager(self)
        self.life_bar = Life_bar(self.player)
        
    def reset(self):
        self.player.reset()
        self.level_manager.current_level = 1
        self.level_manager.reset()
        
    def set_level(self, level):
        self.level_manager.current_level = level
        self.level_manager.reset()
    
    def game_over(self):
        self.game.set_state(Game_state.menu)
        self.reset()

    def update(self):
        self.player.update()
        self.level_manager.update()
    
    def draw(self, surface: pygame.Surface):
        self.level_manager.draw_background(surface)
        self.level_manager.draw_tiles(surface)
        
        self.player.draw(surface)
        self.life_bar.draw(surface)
    
    def key_down(self ,event: pygame.event.Event):
        self.player.key_down(event)
        if event.key == pygame.K_r:
            self.reset()
            
    def key_up(self ,event: pygame.event.Event):
        self.player.key_up(event)
        
        