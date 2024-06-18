import pygame
from game.entities.entity import Entity
from game.lib.sound import get_sound
from game.utils.bot_helper import is_floor
from game.utils.constants.game_constant import Dir, Game_constant
from game.utils.helper import can_move_here, get_entity_y_pos_under_roof_of_above_floor, is_entity_on_floor
from game.utils.loader import load_bot_01_animations

class Bot_state:
    IDLE = 0
    RUNNING = 1
    OFF = 2
    HIT = 3
    
    @classmethod
    def get_sprites_amount(self, state: int):
        if state == self.IDLE:
            return 4
        if state == self.OFF:
            return 1
        if state == self.RUNNING:
            return 6
        if state == self.HIT:
            return 1
        return 0

class Bot(Entity):
    gravity = 0.05 * Game_constant.SCALE
    fall_speed_after_collision = 0.5 * Game_constant.SCALE
    moving_speed = 0.5 * Game_constant.SCALE
    stun_time = 180
    
    def __init__(self, playing, x, y, dir: Dir = Dir.LEFT) -> None:
        super().__init__()
        
        self.playing = playing
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, 16 * Game_constant.SCALE, 18 * Game_constant.SCALE)
        self.draw_offset_x = -8 * Game_constant.SCALE
        self.draw_offset_y = -13 * Game_constant.SCALE
        
        self.state = Bot_state.IDLE    
        
        self.animation_tick = 0
        self.animation_index = 0
        self.animations = load_bot_01_animations()
        self.animation_speed = 10
        self.is_alive = True
        self.moving = False
        
        self.air_speed = 0
        self.in_air = True
        self.dir = dir
        self.is_first =True
        self.is_stunned = False
        
    def update(self):
        if self.is_stunned:
            self.stun_tick += 1
            if self.stun_tick >= self.stun_time:
                self.is_stunned = False
            return
        self.update_pos()
        self.update_animation_tick()
        self.check_player()
        
    def first_update(self):
        if not self.in_air:
            if not is_entity_on_floor(self.hit_box, self.playing.level_manager.get_current_map()):
                self.in_air = True
        self.is_first = False
        
    def check_player(self):
        if self.is_stunned: return
        if self.hit_box.colliderect(self.playing.player.get_hit_box()):
            self.playing.player.to_die()
        
    def update_pos(self):
        self.moving = False
        
        if self.is_first:
            self.first_update()
        
        if self.in_air:
            if can_move_here(self.hit_box.x, self.hit_box.y + self.air_speed, self.hit_box.w, self.hit_box.h, self.playing.level_manager.get_current_map(), self.playing.level_manager.get_block_entities()):
                self.hit_box.y += self.air_speed
                self.air_speed += self.gravity
            else:
                self.hit_box.y = get_entity_y_pos_under_roof_of_above_floor(self.hit_box, self.air_speed)
                self.in_air = False
            return
        
        if self.dir == Dir.LEFT:
            self.update_pos_x(-self.moving_speed)
        else:
            self.update_pos_x(self.moving_speed)    
        self.set_state(Bot_state.RUNNING)   
                    
    def update_pos_x(self, x_speed):
        if can_move_here(self.hit_box.x + x_speed, self.hit_box.y, self.hit_box.w, self.hit_box.h, self.playing.level_manager.get_current_map(), self.playing.level_manager.get_block_entities()) and is_floor(self.hit_box, x_speed, self.playing.level_manager.get_current_map()):
            self.hit_box.x += x_speed
        else:
            self.dir = Dir.RIGHT if self.dir == Dir.LEFT else Dir.LEFT

            
    def update_animation_tick(self):
        self.animation_tick += 1
        if self.animation_tick > self.animation_speed:
            self.animation_tick = 0
            self.animation_index +=1
            if self.animation_index >= Bot_state.get_sprites_amount(self.state):
                self.animation_index = 0
                
    def hit(self, x, y, w, h):
        if self.is_stunned: return False
        if pygame.Rect(x, y + h + 2 * Game_constant.SCALE, w, 5 * Game_constant.SCALE
                    ).colliderect(self.hit_box.x, self.hit_box.y, self.hit_box.w, 8 * Game_constant.SCALE):
            self.stun()
            return True
        return False
        
    def stun(self):
        self.stun_tick = 0
        self.set_state(Bot_state.OFF)
        self.is_stunned = True    
        get_sound().play_sfx(get_sound().stun_bot)
                
    def set_state(self, state):
        if self.state != state:
            self.animation_index = 0
            self.animation_tick = 0
        self.state = state        
    
    def draw(self, surface: pygame.Surface):
        if self.dir == Dir.RIGHT:
            surface.blit(self.animations[self.state][self.animation_index], (self.hit_box.x + self.draw_offset_x, self.hit_box.y + self.draw_offset_y))
        else:
            surface.blit(pygame.transform.flip(self.animations[self.state][self.animation_index], flip_x=1, flip_y=0), (self.hit_box.x + self.draw_offset_x, self.hit_box.y + self.draw_offset_y))
            
    