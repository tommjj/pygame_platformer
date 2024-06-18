import pygame
from game.entities.entity import Entity
from game.entities.platform import Get_player
from game.lib.sound import get_sound
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import load_jumper_animation


class Jumper(Entity):
    jump_speed = -7
    
    def __init__(self,playing : Get_player, x: int, y: int ) -> None:
        super().__init__()
        self.playing = playing
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE + 24 * Game_constant.SCALE, 
                                   Game_constant.TILES_SIZE, 8 * Game_constant.SCALE)
        
        self.draw_offset_y = -24 * Game_constant.SCALE
        
        self.animation_tick = 0
        self.animation_index = 0
        self.animation = load_jumper_animation()
        self.animation_len = len(self.animation)
        self.animation_speed = 8
        self.is_active = False
        
    def update(self):
        if self.hit_box.colliderect(self.playing.player.get_hit_box()):
            if not self.is_active and self.playing.player.is_alive():
                self.playing.player.in_air = True
                self.playing.player.air_speed = self.jump_speed
                get_sound().play_sfx(get_sound().jumper)
                self.playing.player.jump = False
                self.is_active = True
        
        self.update_animation()
    
    
    def update_animation(self):
        if not self.is_active and self.animation_index == 0: return
        
        self.animation_tick += 1
        if self.animation_tick >= self.animation_speed:
            self.animation_tick = 0
            self.animation_index += 1
            if self.animation_index >= self.animation_len:
                self.animation_index = 0
                self.is_active = False
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.animation[self.animation_index], (self.hit_box.x , self.hit_box.y + self.draw_offset_y, self.hit_box.w, self.hit_box.h))
    
    