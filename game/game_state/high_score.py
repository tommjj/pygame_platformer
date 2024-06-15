import pygame
from pygame.event import Event
from game.game_state.state import Game_state
from game.lib.font import Game_font
from game.lib.inputs import Key_events, Mouse_events
from game.ui.button import Button
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale

BG_IMAGE = loader_with_scale('game/res/Background/high_score.png', Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT)
BACK_BUTTON_IMAGE = loader_with_scale('game/res/ui/back_button.png', 42 * Game_constant.SCALE, 42 * Game_constant.SCALE)
OVERLAY = loader_with_scale('game/res/ui/overlay.png', 42 * Game_constant.SCALE,  42 * Game_constant.SCALE)

class Back_button(Button):
    def __init__(self, hit_box: pygame.Rect, game) -> None:
        super().__init__(hit_box)
        self.game = game
        
    def draw(self, surface: pygame.Surface):
        surface.blit(BACK_BUTTON_IMAGE, self.hit_box)
        if self.is_hover:
            surface.blit(OVERLAY, self.hit_box)
            
    def update(self):
        if self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    def on_mouse_out(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
    def on_click(self):
        self.game.set_state(Game_state.menu)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


class High_score(Mouse_events, Key_events): 
    def __init__(self, game) -> None:
        super().__init__()
        
        self.back_button = Back_button(pygame.Rect(
            18 * Game_constant.SCALE, 18 * Game_constant.SCALE, 42 * Game_constant.SCALE, 42 * Game_constant.SCALE            
        ), game)
        
        self.game = game
        self.header_txt = Game_font(int(48 * Game_constant.SCALE)).render('HIGH SCORE', True, (255, 255, 255))
        
    def update(self):
        self.back_button.update()   
    
    def draw(self, surface: pygame.Surface): 
        surface.blit(BG_IMAGE, (0,0))
        self.draw_header(surface)
        self.back_button.draw(surface)

    def draw_header(self, surface: pygame.Surface):
        surface.blit(self.header_txt, (2.6 * Game_constant.TILES_SIZE, 24 * Game_constant.SCALE))
    
    def mouse_down(self, event: Event):
        self.back_button.mouse_down(event)
    
    def mouse_up(self, event: Event):
        self.back_button.mouse_up(event)

    
    def mouse_motion(self, event: Event):
        self.back_button.mouse_motion(event)
    
    def key_down(self, event: Event):
        return super().key_down(event)
    
    def key_up(self, event: Event):
        return super().key_up(event)
    



        