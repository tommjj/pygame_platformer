import pygame
from game.entities.entity import Entity
from game.entities.player import Player
from game.entities.projectile import Projectile, Projectile_manger
from game.lib.sound import get_sound
from game.utils.constants.game_constant import Dir, Game_constant
from game.utils.loader import load_shooter_animation



class Shooter(Entity, Projectile_manger):
    def __init__(self, playing , x: int, y: int, dir: Dir = Dir.RIGHT ,attack_tick: int = 0 , attack_interval = 120) -> None:
        super().__init__()
        self.playing = playing
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, 
                                   Game_constant.SCALE, Game_constant.TILES_SIZE)
        
        self.dir = dir        
        self.animation_tick = 0
        self.animation_index = 0
        self.animation = load_shooter_animation(dir)
        self.animation_len = len(self.animation)
        self.animation_speed = 8
        self.is_active = False
        
        self.attack_interval = attack_interval
        self.attack_tick = attack_tick
        self.shot = False
        self.bullets: list[Projectile] = []
        
        if dir == Dir.DOWN and dir == Dir.TOP:
            self.shot_offset_x = 0 * Game_constant.SCALE
            self.shot_offset_y = 0 * Game_constant.SCALE
        else: 
            self.shot_offset_x = 14 * Game_constant.SCALE
            self.shot_offset_y = 10 * Game_constant.SCALE
        
    def set_attack_interval(self, attack_interval: int):
        self.attack_interval = attack_interval
    
    def update(self):
        self.animation_tick += 1
        if self.animation_tick >= self.attack_interval:
            self.animation_tick = 0
            self.handle_shot()
            self.shot = True
        
        self.update_animation()
        
        for bullet in self.bullets:
            bullet.update()
            
        for bullet in self.bullets:
            if not bullet.is_alive:
                self.bullets.remove(bullet)
    
    def update_animation(self):
        if not self.shot and self.animation_index == 0: return
        
        self.animation_tick += 1
        if self.animation_tick >= self.animation_speed:
            self.animation_tick = 0
            self.animation_index += 1
            if self.animation_index >= self.animation_len:
                self.animation_index = 0
                self.shot = False
                
    def handle_shot(self):
        self.bullets.append(Projectile(self.hit_box.x + self.shot_offset_x, self.hit_box.y + self.shot_offset_y * Game_constant.SCALE, self, self.dir))
    
    def draw(self, surface: pygame.Surface):
        for bullet in self.bullets:
            bullet.draw(surface)
        surface.blit(self.animation[self.animation_index], self.hit_box)
         
    
    def get_target_hit_box(self) -> pygame.Rect:
        return self.playing.player.get_hit_box()
    
    def get_block_entities(self) -> list[Entity]:
        return self.playing.level_manager.get_block_entities()
    
    def get_map(self) -> list[list[int]]:
        return self.playing.level_manager.get_current_map()
    
    def get_target(self) -> Player:
        return self.playing.player

    