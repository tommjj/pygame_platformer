import pygame  
    
from game.entities.entity import Entity
from game.lib.sound import get_sound
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import load_card_animation


class Card(Entity):
    def __init__(self, playing ,x, y) -> None:
        self.playing = playing
        self.is_alive = True,
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE + 10 * Game_constant.SCALE, y * Game_constant.TILES_SIZE + 12 *Game_constant.SCALE,
                                   Game_constant.SCALE * 12, Game_constant.SCALE * 12)
        
        self.animation_tick = 0
        self.animation_index = 0
        self.animation = load_card_animation()
        self.animation_len = len(self.animation)
        self.animation_speed = 16
        
        self.draw_offset_x = -5 * Game_constant.SCALE
        self.draw_offset_y = -5 * Game_constant.SCALE
        
    def set_pos(self, x, y):
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE + 10 * Game_constant.SCALE, y * Game_constant.TILES_SIZE + 12 *Game_constant.SCALE,
                                   Game_constant.SCALE * 12, Game_constant.SCALE * 12)
        
    def update(self):
        if not self.is_alive: return
        
        if self.playing.player.get_hit_box().colliderect(self.hit_box):
            self.is_alive = False
            get_sound().play_sfx(get_sound().card_collect)
        self.update_animation()
    
    def update_animation(self):
        self.animation_tick += 1
        if self.animation_tick >= self.animation_speed:
            self.animation_tick = 0
            self.animation_index += 1
            if self.animation_index >= self.animation_len:
                self.animation_index = 0
        
    
    def draw(self, surface: pygame.Surface):
        if not self.is_alive: return
        
        surface.blit(self.animation[self.animation_index], (self.hit_box.x + self.draw_offset_x, self.hit_box.y + self.draw_offset_y, self.hit_box.width, self.hit_box.height))