from pygame import Rect, Surface, draw
import pygame
from game.game_state.state import Game_state, Playing_state_control, State_control
from game.lib.font import Game_font
from game.ui.button import Button
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale

IMAGE_BUTTON = loader_with_scale('game/res/ui/button_03.png', 10 * Game_constant.TILES_SIZE, 3 * Game_constant.TILES_SIZE)
OVERLAY = loader_with_scale('game/res/ui/overlay.png', 10 * Game_constant.TILES_SIZE, 3 * Game_constant.TILES_SIZE)

class Save_score:
    def save(self):
        pass

class Back_to_menu_button(Button):
    def __init__(self,play: Save_score , game: State_control , x, y) -> None:
        super().__init__(Rect(x, y, 9 * Game_constant.TILES_SIZE, 3 * Game_constant.TILES_SIZE))
        self.game = game
        self.play = play
        self.text = Game_font(int(1.6 * Game_constant.TILES_SIZE)).render('BACK TO MENU', True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        
        self.text_rect.x = self.hit_box.x + self.hit_box.width / 2 - self.text_rect.width / 2 + 16 * Game_constant.SCALE
        self.text_rect.y = self.hit_box.y + self.hit_box.height / 2 - self.text_rect.height / 2 + 2 * Game_constant.SCALE
        
    def draw(self, surface: Surface):
        surface.blit(IMAGE_BUTTON, self.hit_box)
        surface.blit(self.text, self.text_rect)
        if self.is_hover:
            surface.blit(OVERLAY, self.hit_box)
    
    def update(self):
        if self.is_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    
    def on_mouse_out(self):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
    def on_click(self):
        try:
            self.play.save()
            self.game.set_state(Game_state.menu)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        except:
            pass
            
       