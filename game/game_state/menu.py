
import pygame

from game.game_state.state import Game_state
from game.levels.background import draw_background
from game.lib.inputs import Key_events, Mouse_events
from game.ui.button import Button
from game.ui.play_button import  Play_button
from game.ui.high_score_button import  High_score_button
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale

IMAGE_BG = loader_with_scale('game/res/Background/menu.png', Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT)

class Game_menu(Key_events, Mouse_events):
    def __init__(self, game) -> None:
        self.game = game
        self.buttons: list[Button] = []
        self.buttons.append(Play_button(game))
        self.buttons.append(High_score_button(game))
    
    def draw(self, surface: pygame.Surface):
        draw_background(surface, self.mouse_x)
        surface.blit(IMAGE_BG, (0,0))
        
        for button in self.buttons:
            button.draw(surface)
    
    def update(self):
        for button in self.buttons:
            button.update()
    
    def key_down(self ,event: pygame.event.Event):
        pass
            
    def key_up(self ,event: pygame.event.Event):
        pass
        
    def mouse_down(self ,event: pygame.event.Event):
        for button in self.buttons:
            button.mouse_down(event)
            
    def mouse_up(self ,event: pygame.event.Event):
        for button in self.buttons:
            button.mouse_up(event)
    
    def mouse_motion(self ,event: pygame.event.Event):
        x, y = pygame.mouse.get_pos()
        self.mouse_x = x
        
        for button in self.buttons:
            button.mouse_motion(event)
    