
import pygame

from game.game_state.state import Game_state, State_control
from game.levels.background import draw_background
from game.lib.font import Game_font
from game.lib.inputs import Key_events, Mouse_events
from game.ui.button import Button
from game.ui.play_button import  Play_button
from game.ui.high_score_button import  High_score_button
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale

IMAGE_BG = loader_with_scale('game/res/Background/menu.png', Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT)

class Game_menu(Key_events, Mouse_events):
    def __init__(self, game: State_control) -> None:
        self.game = game
        self.buttons: list[Button] = []
        self.buttons.append(Play_button(game))
        self.buttons.append(High_score_button(game))
        
        self.text = Game_font(int(4.5 * Game_constant.TILES_SIZE)).render('PLATFORMER', True, (255, 255, 255))
        self.text_shadow = Game_font(int(4.5 * Game_constant.TILES_SIZE)).render('PLATFORMER', True, (180, 180, 200))
        self.text_rect = self.text.get_rect()
        self.text_rect.x = Game_constant.GAME_WIDTH / 2 - self.text_rect.width / 2 + 7 * Game_constant.SCALE
        self.text_rect.y = Game_constant.TILES_SIZE * 1.5
        self.mouse_x = 0
        
    
    def draw(self, surface: pygame.Surface):
        draw_background(surface, self.mouse_x)
        surface.blit(IMAGE_BG, (0,0))
        
        surface.blit(self.text_shadow, (self.text_rect.x + 4 * Game_constant.SCALE, self.text_rect.y + 4 * Game_constant.SCALE))
        surface.blit(self.text, self.text_rect)
        
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
    