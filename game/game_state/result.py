import pygame
from datetime import datetime
from pygame.event import Event

from game.game_state.state import State_control, Playing_state_control
from game.lib.font import Game_font
from game.lib.inputs import Key_events, Mouse_events
from game.ui.back_to_menu_button import Back_to_menu_button, Save_score
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale
from game.database import High_score_model

BG_IMAGE = loader_with_scale('game/res/Background/result_bg.png', Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT)

MAX_NAME_LEN = 16

class Result(Key_events, Mouse_events, Save_score):
    FINISHED = "FINISHED"
    GAME_OVER = "GAME OVER"
    status = FINISHED
    
    def __init__(self, game: State_control, play: Playing_state_control) -> None:
        super().__init__()
        
        self.username = ""
        self.back_to_menu_button = Back_to_menu_button(self, game, 17.5 * Game_constant.TILES_SIZE, 11.5 * Game_constant.TILES_SIZE)
        
        self.header_txt_finished = Game_font(int(92 * Game_constant.SCALE)).render(self.FINISHED, True, (255, 255, 255))
        self.header_txt_game_over = Game_font(int(92 * Game_constant.SCALE)).render(self.GAME_OVER, True, (255, 255, 255))
        
        self.score_font = Game_font(int(48 * Game_constant.SCALE))
        self.h1_font = Game_font(int(82 * Game_constant.SCALE))
        self.h2_font = Game_font(int(28 * Game_constant.SCALE))
        self.score = 0
        
    def save(self):
        if len(self.username.split()) == 0:
            raise Exception("enter name ")
        
        data = High_score_model({"name": self.username, "score": self.score, "createdAt": self.created_at})
        data.save()
    
    def set_status(self, status):
        self.status = status
    
    def set_score(self, score):
        now = datetime.now()
        self.created_at = now.strftime("%m/%d/%Y, %H:%M:%S")
        self.score = score
    
    def reset(self):
        pass

    def update(self):
        self.back_to_menu_button.update()
    
    def draw(self, surface: pygame.Surface):
        surface.blit(BG_IMAGE, (0, 0))
        if self.status == self.GAME_OVER:
            surface.blit(self.header_txt_game_over, (12 * Game_constant.SCALE, 10 * Game_constant.SCALE))
        else: 
            surface.blit(self.header_txt_finished, (12 * Game_constant.SCALE, 10 * Game_constant.SCALE))
            
        
        surface.blit(self.h2_font.render('ENTER_NAME:', True, (255, 255, 255)), (24 * Game_constant.SCALE, 4.2 * Game_constant.TILES_SIZE))
        surface.blit(self.h1_font.render(f'{self.username}', True, (255, 255, 255)), (24 * Game_constant.SCALE, 5 * Game_constant.TILES_SIZE))
        
        surface.blit(self.h2_font.render('score:', True, (255, 255, 255)), (24 * Game_constant.SCALE, 8.2 * Game_constant.TILES_SIZE))
        surface.blit(self.score_font.render(f'{self.score}', True, (255, 255, 255)), (24 * Game_constant.SCALE, 9 * Game_constant.TILES_SIZE))
        
        self.back_to_menu_button.draw(surface)
    
    def key_down(self ,event: pygame.event.Event):
        if event.key >= pygame.K_0 and event.key <= pygame.K_z:
            if len(self.username) < MAX_NAME_LEN:
                self.username += pygame.key.name(event.key)
        if event.key == pygame.K_SPACE:
            if len(self.username) < MAX_NAME_LEN:
                self.username += '_'
        if event.key == pygame.K_BACKSPACE:
            self.username = self.username[:-1]
            
    def key_up(self ,event: pygame.event.Event):
       pass
    
    def mouse_up(self, event: Event):
        self.back_to_menu_button.mouse_up(event)
        
    def mouse_down(self, event: Event):
        self.back_to_menu_button.mouse_down(event)
    
    def mouse_motion(self, event: Event):
        self.back_to_menu_button.mouse_motion(event)