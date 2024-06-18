import pygame
from pygame.event import Event
from game.game_state.state import Game_state, State_control
from game.lib.font import Game_font
from game.lib.inputs import Key_events, Mouse_events
from game.ui.button import Button
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale
from game.database import db

BG_IMAGE = loader_with_scale('game/res/Background/high_score.png', Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT)
BACK_BUTTON_IMAGE = loader_with_scale('game/res/ui/back_button.png', 42 * Game_constant.SCALE, 42 * Game_constant.SCALE)
NEXT_BUTTON_IMAGE = loader_with_scale('game/res/ui/next_button.png', 42 * Game_constant.SCALE, 42 * Game_constant.SCALE)
PRIV_BUTTON_IMAGE = loader_with_scale('game/res/ui/priv_button.png', 42 * Game_constant.SCALE, 42 * Game_constant.SCALE)

def format_number(num, num_len):
    num = str(num)
    
    for i in range(num_len- len(num)):
        num = '0'+num
    return num

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

        self.text_font = Game_font(int(Game_constant.TILES_SIZE))
        
        self.page_index = 0
        self.page_size = 8
        self.list = []
        
    def next_page(self):
        data = db.select("SELECT * FROM high_score_model ORDER BY score DESC LIMIT ? OFFSET ?", self.page_size, (self.page_index +1) * self.page_size)
        if len(data) == 0: return
        self.page_index += 1
        self.list = data
    
    def priv_page(self):
        if self.page_index == 0: return
        self.page_index -= 1
        self.list = db.select("SELECT * FROM high_score_model ORDER BY score DESC LIMIT ? OFFSET ?", self.page_size, self.page_index * self.page_size)
        
        
    def reset(self):
        self.page_index = 0
        self.list = db.select("SELECT * FROM high_score_model ORDER BY score DESC LIMIT ? OFFSET ?", self.page_size, self.page_index * self.page_size)
        
    def update(self):
        for button in self.buttons:
            button.update()
            
    def draw(self, surface: pygame.Surface): 
        surface.blit(BG_IMAGE, (0,0))
        self.draw_header(surface)
        
        for button in self.buttons:
            button.draw(surface)
          
            
        for i, data in enumerate(self.list):
            name = data['name']
            score = format_number(data['score'], 5)
            
            pygame.draw.line(surface, (120, 120, 200), ( 30 * Game_constant.SCALE ,(i+1) * (Game_constant.TILES_SIZE + 5 * Game_constant.SCALE) + Game_constant.TILES_SIZE * 3),( Game_constant.GAME_WIDTH - 30 ,(i+1) * (Game_constant.TILES_SIZE + 5 * Game_constant.SCALE) + Game_constant.TILES_SIZE * 3))
            
            surface.blit(self.text_font.render(f'{self.page_index * self.page_size+i +1}. {name}' ,True, (255,255,255)), (35 * Game_constant.SCALE, i * (Game_constant.TILES_SIZE + 5 * Game_constant.SCALE) + Game_constant.TILES_SIZE * 3 + 8 * Game_constant.SCALE))
            surface.blit(self.text_font.render(f'{score}' ,True, (255,255,255)), (Game_constant.TILES_SIZE * 25, i * (Game_constant.TILES_SIZE + 5 * Game_constant.SCALE) + Game_constant.TILES_SIZE * 3 + 8 * Game_constant.SCALE))
    
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
    



        