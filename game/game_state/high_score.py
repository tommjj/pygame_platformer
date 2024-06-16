import pygame
from pygame.event import Event
from game.game_state.state import Game_state, State_control
from game.lib.font import Game_font
from game.lib.inputs import Key_events, Mouse_events
from game.ui.button import Button
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale

BG_IMAGE = loader_with_scale('game/res/Background/high_score.png', Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT)
BACK_BUTTON_IMAGE = loader_with_scale('game/res/ui/back_button.png', 42 * Game_constant.SCALE, 42 * Game_constant.SCALE)
NEXT_BUTTON_IMAGE = loader_with_scale('game/res/ui/next_button.png', 42 * Game_constant.SCALE, 42 * Game_constant.SCALE)
PRIV_BUTTON_IMAGE = loader_with_scale('game/res/ui/priv_button.png', 42 * Game_constant.SCALE, 42 * Game_constant.SCALE)


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
     
class Page_control:
    def next_page(self):
        pass
    def priv_page(self):
        pass
        
class Next_button(Button):
    def __init__(self, hit_box: pygame.Rect, page_control: Page_control) -> None:
        super().__init__(hit_box)
        self.page_control = page_control
        
    def draw(self, surface: pygame.Surface):
        surface.blit(NEXT_BUTTON_IMAGE, self.hit_box)
        if self.is_hover:
            surface.blit(OVERLAY, self.hit_box)
            
    def update(self):
        if self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    def on_mouse_out(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
    def on_click(self):
        self.page_control.next_page()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
class Priv_button(Button):
    def __init__(self, hit_box: pygame.Rect, page_control: Page_control) -> None:
        super().__init__(hit_box)
        self.page_control = page_control
        
    def draw(self, surface: pygame.Surface):
        surface.blit(PRIV_BUTTON_IMAGE, self.hit_box)
        if self.is_hover:
            surface.blit(OVERLAY, self.hit_box)
            
    def update(self):
        if self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    def on_mouse_out(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
    def on_click(self):
        self.page_control.priv_page()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


class High_score(Mouse_events, Key_events, Page_control): 
    def __init__(self, game: State_control) -> None:
        super().__init__()
        self.buttons : list[Button]= []    
        
        
        self.buttons.append(Back_button(pygame.Rect(
            18 * Game_constant.SCALE, 18 * Game_constant.SCALE, 42 * Game_constant.SCALE, 42 * Game_constant.SCALE            
        ), game))
        self.buttons.append(Next_button(pygame.Rect(
            Game_constant.GAME_WIDTH - 63 * Game_constant.SCALE, Game_constant.GAME_HEIGHT - 58 * Game_constant.SCALE, 42 * Game_constant.SCALE, 42 * Game_constant.SCALE            
        ), self))
        self.buttons.append(Priv_button(pygame.Rect(
            Game_constant.GAME_WIDTH - 120 * Game_constant.SCALE, Game_constant.GAME_HEIGHT - 58 * Game_constant.SCALE, 42 * Game_constant.SCALE, 42 * Game_constant.SCALE            
        ), self))
        
        self.game = game
        self.header_txt = Game_font(int(48 * Game_constant.SCALE)).render('HIGH SCORE', True, (255, 255, 255))
     
    def next_page(self):
        print("next")
    
    def priv_page(self):
        print("priv")
        
    def update(self):
        for button in self.buttons:
            button.update()
            
    def draw(self, surface: pygame.Surface): 
        surface.blit(BG_IMAGE, (0,0))
        self.draw_header(surface)
        
        for button in self.buttons:
            button.draw(surface)

    def draw_header(self, surface: pygame.Surface):
        surface.blit(self.header_txt, (2.6 * Game_constant.TILES_SIZE, 24 * Game_constant.SCALE))
    
    def mouse_down(self, event: Event):
        for button in self.buttons:
            button.mouse_down(event)
    
    def mouse_up(self, event: Event):
        for button in self.buttons:
            button.mouse_up(event)

    def mouse_motion(self, event: Event):
        for button in self.buttons:
            button.mouse_motion(event)
    
    def key_down(self, event: Event):
        return super().key_down(event)
    
    def key_up(self, event: Event):
        return super().key_up(event)
    



        