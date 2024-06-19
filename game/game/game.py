import pygame

from game.game_state.menu import Game_menu
from game.game_state.playing import Playing
from game.game_state.state import Game_state, State_control
from game.lib.font import Game_font
from game.utils.loader import loader
from game.utils.constants.game_constant import Game_constant 
from game.lib.sound import SOUND_END_EVENT, get_sound
from game.game_state.high_score import High_score

GAME_TICK = 120

class Game(State_control):
    _state = Game_state.menu
    _tick = 0
    
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        self.pygame = pygame
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
        pygame.display.set_caption('PLATFORMER')
        pygame.display.set_icon(loader('game/res/icon.png'))
        self.clock = self.pygame.time.Clock()
        
        self.playing = Playing(self)
        self.menu = Game_menu(self)
        self.high_score = High_score(self)
   
    
    def run(self): 
        text_title = Game_font(int(4.5 * Game_constant.TILES_SIZE)).render('PLATFORMER', True, (255, 255, 255))
        text_shadow_title = Game_font(int(4.5 * Game_constant.TILES_SIZE)).render('PLATFORMER', True, (180, 180, 200))
        text_rect_title = text_title.get_rect()
        text_rect_title.x = Game_constant.GAME_WIDTH / 2 - text_rect_title.width / 2 + 7 * Game_constant.SCALE
        text_rect_title.y = Game_constant.TILES_SIZE * 2
        
        pygame.draw.rect(self.screen, '#267ae9', (0,0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))   
        text = Game_font(int(1.5 * Game_constant.TILES_SIZE)).render('Loading...', True, (255, 255, 255))
        text_rect = text.get_rect()
        
        self.screen.blit(text, (Game_constant.GAME_WIDTH - text_rect.w - 20, Game_constant.GAME_HEIGHT - text_rect.h - 10))
        self.screen.blit(text_shadow_title, (text_rect_title.x + 4 * Game_constant.SCALE, text_rect_title.y + 4 * Game_constant.SCALE))
        self.screen.blit(text_title, text_rect_title)
        
        pygame.display.flip()  
        get_sound().play_music(get_sound().soundtrack)
        
        running = True
    
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.key_down(event)
                if event.type == pygame.KEYUP:
                    self.key_up(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down(event)
                if event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_up(event)
                if event.type == pygame.MOUSEMOTION:
                    self.mouse_motion(event)
                if event.type == SOUND_END_EVENT:
                    get_sound().play_music(get_sound().soundtrack)

            self.update()
            if self._tick > 0:
                self.draw()
                self._tick = 0
            else:
                self._tick += 1
                
            self.clock.tick(GAME_TICK)  
            
    def set_state(self, state):
        self._state = state

    def key_down(self ,event: pygame.event.Event):
        if self._state == Game_state.playing:
            self.playing.key_down(event)
        elif self._state == Game_state.menu:
            self.menu.key_down(event)
        elif self._state == Game_state.high_score:
            self.high_score.key_down(event)
            
    def key_up(self ,event: pygame.event.Event):
        if self._state == Game_state.playing:
            self.playing.key_up(event)
        elif self._state == Game_state.menu:
            self.menu.key_up(event)
        elif self._state == Game_state.high_score:
            self.high_score.key_up(event)
        
    def mouse_down(self ,event: pygame.event.Event):
        if self._state == Game_state.playing:
            self.playing.mouse_down(event)
        elif self._state == Game_state.menu:
            self.menu.mouse_down(event)
        elif self._state == Game_state.high_score:
            self.high_score.mouse_down(event)
            
    def mouse_up(self ,event: pygame.event.Event):
        if self._state == Game_state.playing:
            self.playing.mouse_up(event)
        elif self._state == Game_state.menu:
            self.menu.mouse_up(event)
        elif self._state == Game_state.high_score:
            self.high_score.mouse_up(event)
            
    def mouse_motion(self ,event: pygame.event.Event):
        if self._state == Game_state.playing:
            self.playing.mouse_motion(event)
        elif self._state == Game_state.menu:
            self.menu.mouse_motion(event)
        elif self._state == Game_state.high_score:
            self.high_score.mouse_motion(event)

    def update(self):
        if self._state == Game_state.playing:
            self.playing.update()
        elif self._state == Game_state.menu:
            self.menu.update()
        elif self._state == Game_state.high_score:
            self.high_score.update()
    
    def draw(self):
        if self._state == Game_state.playing:
            self.playing.draw(self.screen)
        elif self._state == Game_state.menu:
            self.menu.draw(self.screen)
        elif self._state == Game_state.high_score:
            self.high_score.draw(self.screen)
            
        pygame.display.flip()   
        