import pygame

from game.game_state.menu import Game_menu
from game.game_state.playing import Playing
from game.game_state.state import Game_state
from game.utils.loader import res_path 
from ..utils.constants.game_constant import Game_constant 
from ..lib.sound import SOUND_END_EVENT, Sound, get_sound

GAME_TICK = 120


class Game:
    state = Game_state.playing
    
    def __init__(self) -> None:
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        self.pygame = pygame
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
        self.clock = self.pygame.time.Clock()
        
        self.playing = Playing(self)
        self.menu = Game_menu(self)
        
    
    def run(self): 
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
                if event.type == SOUND_END_EVENT:
                    print('end')
                    get_sound().play_music(get_sound().soundtrack)

            self.update()
            self.draw()
            self.clock.tick(GAME_TICK)  

    def key_down(self ,event: pygame.event.Event):
        if self.state == Game_state.playing:
            self.playing.key_down(event)
        if self.state == Game_state.menu:
            self.menu.key_down(event)
            
    def key_up(self ,event: pygame.event.Event):
        if self.state == Game_state.playing:
            self.playing.key_up(event)
        if self.state == Game_state.menu:
            self.menu.key_up(event)
        
    def mouse_down(self ,event: pygame.event.Event):
        if self.state == Game_state.playing:
            self.playing.mouse_down(event)
        if self.state == Game_state.menu:
            self.menu.mouse_down(event)
            
    def mouse_up(self ,event: pygame.event.Event):
        if self.state == Game_state.playing:
            self.playing.mouse_up(event)
        if self.state == Game_state.menu:
            self.menu.mouse_up(event)

    def update(self):
        self.playing.update()
    
    def draw(self):
        if self.state == Game_state.playing:
            self.playing.draw(self.screen)
        if self.state == Game_state.menu:
            self.menu.draw(self.screen)
            
        pygame.display.flip()   
        


    