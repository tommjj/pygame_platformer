import pygame

from game.entities.entity import Entity
from game.entities.player import Player
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import load_entry_animation, load_platform_animation

class Get_player:
    def get_player(self) -> Player:
        pass

class Platform(Entity):  
    def __init__(self, playing: Get_player , x, y) -> None:
        super().__init__()
        self.playing = playing
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE)
        
        self.is_active = True
        self.animation_tick = 0
        self.animation_index = 0
        self.animation = load_platform_animation()
        self.animation_len = len(self.animation)
        self.animation_speed = 2
        
    def get_hit_box(self):
        if not self.is_active:
            return pygame.Rect(0, 0, 0, 0)
        return self.hit_box
    
    def set_pos(self, x, y):
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE)
    
    def update(self):
        self.update_animation()
        
    def update_animation(self):
        self.animation_tick += 1
             
        if self.animation_tick >= self.animation_speed:
            self.animation_tick = 0
            
            if not self.is_active and self.animation_index < 4:
                self.animation_index += 1
            elif self.is_active and self.animation_index > 0:    
                self.animation_index += 1
                if self.animation_index >= self.animation_len:
                    self.animation_index = 0
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.animation[self.animation_index], self.hit_box)
    

