from pygame import Rect, Surface
import pygame
from game.game_state.state import Game_state
from game.lib.font import Game_font
from game.ui.button import  Button
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale

IMAGE_BUTTON = loader_with_scale('game/res/ui/button_02.png', 10 * Game_constant.TILES_SIZE, 3 * Game_constant.TILES_SIZE)
OVERLAY = loader_with_scale('game/res/ui/overlay.png', 10 * Game_constant.TILES_SIZE, 3 * Game_constant.TILES_SIZE)

class High_score_button(Button):
    def __init__(self, game) -> None:
        super().__init__(Rect(9 * Game_constant.TILES_SIZE, 10.5 * Game_constant.TILES_SIZE, 10 * Game_constant.TILES_SIZE, 3 * Game_constant.TILES_SIZE))
        self.game = game
        self.text = Game_font(int(1.5 * Game_constant.TILES_SIZE)).render('High score', True, (255, 255, 255))
        self.text_rect = self.text.get_rect()
        self.text_rect.x = self.hit_box.x + self.hit_box.width / 2 - self.text_rect.width / 2
        self.text_rect.y = self.hit_box.y + self.hit_box.height / 2 - self.text_rect.height / 2
        
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
        self.game.set_state(Game_state.high_score)
        self.game.high_score.reset()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)