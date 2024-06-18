import pygame

from game.entities.platform import Get_player, Platform
from game.lib.sound import get_sound
from game.utils.constants.game_constant import Game_constant

class Crumbling_platform(Platform):
    def __init__(self, playing: Get_player, x, y, time_to_crash = 30, time_to_active = 180) -> None:
        super().__init__(playing, x, y)
        
        self.tick = 0
        self.is_start_crash = False
        self.time_to_crash = time_to_crash
        self.time_to_active = time_to_active
        
    def update(self):
        
        if self.check_is_player_on():
            self.is_start_crash = True
        
        if self.is_start_crash and self.is_active:
            self.tick += 1
            if self.tick >= self.time_to_crash:
                self.is_active = False
                self.tick = 0
                get_sound().play_sfx(get_sound().open_doors)
        
        if not self.is_active:
            self.tick += 1
            if self.tick >= self.time_to_active:
                self.tick = 0
                self.is_active = True
                self.is_start_crash = False
                get_sound().play_sfx(get_sound().open_doors)
        
        super().update()
        
        
    def check_is_player_on(self):
        h = self.playing.get_player().get_hit_box()
        
        return self.hit_box.colliderect(h.x, h.y, h.w, h.h + 2.5 * Game_constant.SCALE)