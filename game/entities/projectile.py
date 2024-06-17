

import pygame
from game.entities.entity import Entity
from game.entities.player import Player
from game.utils.constants.game_constant import Dir, Game_constant
from game.utils.helper import can_move_here
from game.utils.loader import load_bullet_animation

class Projectile_manger:
    def get_target_hit_box(self) -> pygame.Rect:
        pass
    def get_block_entities(self) -> list[Entity]:
        pass
    def get_map(self) -> list[list[int]]:
        pass
    def get_target(self) -> Player:
        pass

class Projectile(Entity):
    speed = 3 * Game_constant.SCALE
    
    def __init__(self, x: int , y: int, projectile_manger: Projectile_manger, dir: Dir) -> None:
        super().__init__()
        
        self.projectile_manger = projectile_manger
        
        if dir == Dir.TOP or dir == Dir.DOWN:
            self.hit_box = pygame.Rect(x, y, 5 * Game_constant.SCALE, 12 * Game_constant.SCALE)
            self.draw_offset_x = -6 * Game_constant.SCALE
            self.draw_offset_y = -3 * Game_constant.SCALE
        else:
            self.hit_box = pygame.Rect(x, y, 12 * Game_constant.SCALE, 5 * Game_constant.SCALE)
            self.draw_offset_x = -3 * Game_constant.SCALE
            self.draw_offset_y = -6 * Game_constant.SCALE
        self.dir = dir
        
        self.animation_tick = 0
        self.animation_index = 0
        self.animation = load_bullet_animation(dir)
        self.animation_len = len(self.animation)
        self.animation_speed = 8
        self.is_alive = True
        
    def update(self):
        if not self.is_alive: return
        self.update_animation()
        
        if self.dir == Dir.TOP:
            self.update_pos_y(-self.speed)
        if self.dir == Dir.DOWN:
            self.update_pos_y(self.speed)
        if self.dir == Dir.LEFT:
            self.update_pos_x(-self.speed)
        if self.dir == Dir.RIGHT:
            self.update_pos_x(self.speed)
            
        if self.hit_box.colliderect(self.projectile_manger.get_target_hit_box()):
            self.projectile_manger.get_target().to_die()
            self.is_alive = False
        
    def update_pos_x(self, speed):
        if can_move_here(self.hit_box.x + speed, self.hit_box.y, self.hit_box.w, self.hit_box.h,
                         self.projectile_manger.get_map(), self.projectile_manger.get_block_entities()):
            self.hit_box.x += speed
        else:
            self.is_alive = False
        
    def update_pos_y(self, speed):
        if can_move_here(self.hit_box.x ,self.hit_box.y + speed, self.hit_box.w, self.hit_box.h,
                         self.projectile_manger.get_map(), self.projectile_manger.get_block_entities()):
            self.hit_box.y += speed
        else:
            self.is_alive = False
    
    def update_animation(self):
        self.animation_tick += 1
        if self.animation_tick >= self.animation_speed:
            self.animation_tick = 0
            self.animation_index += 1
            if self.animation_index >= self.animation_len:
                self.animation_index = 0
        
        
    def draw(self, surface: pygame.Surface):
        if not self.is_alive: return
        surface.blit(self.animation[self.animation_index], (self.hit_box.x + self.draw_offset_x, self.hit_box.y + self.draw_offset_y))
