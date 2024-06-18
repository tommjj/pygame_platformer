import pygame
from pygame.event import Event

from game.entities.platform import Get_player
from game.entities.player import Player
from game.game_state.state import Game_state, Playing_state, Playing_state_control, State_control
from game.levels.level_manager import Levels_manager
from game.levels.levels_builder.level_builder import NUMBER_OF_LEVEL
from game.lib.inputs import Key_events, Mouse_events
from game.ui.life_bar import Life_bar
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale
from .result import Result

OVER_LAY = loader_with_scale('game/res/ui/overlay.png', Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT)

START_LEVEL = 1

class Playing(Key_events, Mouse_events, Playing_state_control, Get_player):
    player = None
    level_manager = None
    
    def __init__(self, game: State_control) -> None:
        super().__init__()
        self.game = game
        self.player = Player(self)
        self.level_manager = Levels_manager(self)
        self.life_bar = Life_bar(self.player)
        
        self.score = 0
        
        self.result = Result(game, self)
        self.state = Playing_state.PLAY
    
    def set_state(self, game_state: Playing_state):
        self.state = game_state
    
    def get_level_manager(self) -> Levels_manager:
        return self.level_manager

    def get_player(self) -> Player:
        return self.player

    def next_level(self):
        self.score += self.level_manager.score
        if self.level_manager.current_level < NUMBER_OF_LEVEL:
            self.level_manager.next_level()
        else:
            self.score += (self.player.life_points - 1) * 120
            self.result.set_score(self.score)
            self.result.set_status(self.result.FINISHED)
            self.set_state(Playing_state.RESULT)
    
    def reset(self):
        self.score = 0
        self.set_state(Playing_state.PLAY)
        self.player.reset()
        self.level_manager.current_level = START_LEVEL
        self.level_manager.reset()
        
    def set_level(self, level):
        self.level_manager.current_level = level
        self.level_manager.reset()
    
    def game_over(self):
        self.result.set_score(self.score)
        self.result.set_status(self.result.GAME_OVER)
        self.set_state(Playing_state.RESULT)

    def update(self):
        if self.state == Playing_state.PLAY:
            self.player.update()
            self.level_manager.update()
        elif self.reset == Playing_state.RESULT:
            self.result.update()
    
    def draw(self, surface: pygame.Surface):
        if self.state == Playing_state.PLAY:
            self.level_manager.draw_background(surface)
            self.level_manager.draw_tiles(surface)
        
            self.player.draw(surface)
            self.life_bar.draw(surface)
            
        elif self.state == Playing_state.PAUSE:
            self.level_manager.draw_background(surface)
            self.level_manager.draw_tiles(surface)
        
            self.player.draw(surface)
            self.life_bar.draw(surface)
            
            surface.blit(OVER_LAY, (0, 0))
            
        elif self.state == Playing_state.RESULT:
            self.result.draw(surface)
    
    def key_down(self ,event: pygame.event.Event):
        if self.state == Playing_state.PLAY:
            self.player.key_down(event)
            if event.key == pygame.K_ESCAPE:
                self.set_state(Playing_state.PAUSE)
            
        elif self.state == Playing_state.RESULT:
            self.result.key_down(event)
            
        elif self.state == Playing_state.PAUSE:
            if event.key == pygame.K_ESCAPE:
                self.set_state(Playing_state.PLAY)
            
    def key_up(self ,event: pygame.event.Event):
        if self.state == Playing_state.PLAY:
            self.player.key_up(event)
        elif self.state == Playing_state.RESULT:
            self.result.key_up(event)
        
    def mouse_down(self, event: Event):
        if self.state == Playing_state.RESULT:
            self.result.mouse_down(event)
    
    def mouse_up(self, event: Event):
        if self.state == Playing_state.RESULT:
            self.result.mouse_up(event)
    
    def mouse_motion(self, event: Event):
        if self.state == Playing_state.RESULT:
            self.result.mouse_motion(event)