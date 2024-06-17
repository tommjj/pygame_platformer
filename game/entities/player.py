import pygame

from game.entities.entity import Entity
from game.lib.sound import get_sound
from game.utils.constants import player_constant
from game.utils.constants.game_constant import Game_constant
from game.utils.helper import can_move_here, get_entity_x_pos_next_to_wall, get_entity_y_pos_under_roof_of_above_floor, is_entity_on_floor
from game.utils.loader import load_player_animations

MAX_LIFE_POINT = 5

class Player(Entity):
    ani_tick = 0
    ani_index = 0
    ani_speed = 15
    player_action = player_constant.IDLE
    animations = [[]]
    
    moving = False
    attacking = False 
    double_jump = False
    left = False
    right = False
    jump = False
    
    die = False
    dead = False
    
    x_draw_off_set = 30 * Game_constant.SCALE 
    y_draw_off_set = 29 * Game_constant.SCALE 
    
    player_speed = 1.1 * Game_constant.SCALE
    
    air_speed = 0.0
    gravity = 0.05 * Game_constant.SCALE
    jump_speed = -2 * Game_constant.SCALE
    fall_speed_after_collision = 0.5 * Game_constant.SCALE
    in_air = True
    
    flip_x = 0
    flip_w = 1
    
    hit_box = pygame.Rect(0 , 0, 19 * Game_constant.SCALE, 28 * Game_constant.SCALE)
    
    life_points = MAX_LIFE_POINT
        
    def __init__(self, playing) -> None:
        self.playing = playing
        self.load_animation()

    def load_animation(self):
        w = 85 * Game_constant.SCALE
        self.animations = load_player_animations(w)
    
    def update(self):
        self.update_pos()
        self.set_animation()
        self.update_animation()
        
        if not self.dead: return
        if self.life_points <= 0:
            self.playing.game_over()
        else:
            self.playing.level_manager.reset()
    
    def jump_handler(self):
        if self.jump_speed > self.air_speed:
            self.jump = False
            return
        
        if self.in_air and not self.double_jump:
            self.air_speed = self.jump_speed
            self.double_jump = True
            get_sound().play_sfx(get_sound().jump)
        elif self.in_air: 
            self.jump = False
            return
        
        self.in_air = True
        self.air_speed = self.jump_speed
        get_sound().play_sfx(get_sound().jump)
        self.jump = False
        
    def is_alive(self):
        return not self.die
        
    def set_animation(self):
        priv_ani = self.player_action
        
        if self.moving:
            self.player_action = player_constant.RUNNING
        else:
            self.player_action = player_constant.IDLE
  
        if self.in_air:
            if self.air_speed > 0:
                self.player_action = player_constant.FALLING
            else:
                self.player_action = player_constant.JUMP
        
        if self.die:
            self.player_action = player_constant.DEAD
            
        if priv_ani != self.player_action:
            self.ani_index = 0
            self.ani_tick = 0
    
        
    def update_animation(self):
        self.ani_tick += 1
        
        if self.ani_tick > self.ani_speed:
            if self.player_action == player_constant.DEAD:
                is_last_f = self.ani_index >= player_constant.get_sprites_amount(self.player_action) - 1
                
                self.ani_index = player_constant.get_sprites_amount(self.player_action) - 1 if is_last_f else self.ani_index + 1
                if is_last_f: self.dead = True
            
            elif self.player_action == player_constant.JUMP:
                self.ani_index = self.ani_index - 1 if self.ani_index >= player_constant.get_sprites_amount(self.player_action) - 1 else self.ani_index + 1
                return
            else:  
                self.ani_index = 0 if self.ani_index >= player_constant.get_sprites_amount(self.player_action) - 1 else self.ani_index + 1
            self.ani_tick = 0
    
    def update_pos(self):
        if self.hit_box.x > Game_constant.GAME_WIDTH:
            self.win()
            return
        
        self.moving = False
        
        if self.jump:
            if not self.die:
                self.jump_handler()
        
        if not self.in_air:
            if not self.left and not self.right or self.left and self.right:
                return
        
        x_speed = 0
        if self.left:
            x_speed -= self.player_speed
            self.flip_x = 60
            self.flip_w = -1
            
        if self.right:
            x_speed += self.player_speed
            self.flip_x = 0
            self.flip_w = 1
            
        if not self.in_air:
            if not is_entity_on_floor(self.hit_box, self.playing.level_manager.get_current_map()):
                self.in_air = True
    
        if self.in_air:
            self.check_attack()
            
            if can_move_here(self.hit_box.x , self.hit_box.y + self.air_speed, self.hit_box.width - 1, self.hit_box.height - 1, self.playing.level_manager.get_current_map(), self.playing.level_manager.get_block_entities()):
                self.hit_box.y += self.air_speed
                self.air_speed += self.gravity
                self.update_x_pos(x_speed)
            else:
                self.hit_box.y = get_entity_y_pos_under_roof_of_above_floor(self.hit_box, self.air_speed)
                if self.air_speed > 0:
                    self.in_air = False
                    self.air_speed = 0
                    self.double_jump = False
                else:
                    self.air_speed = self.fall_speed_after_collision
                self.update_x_pos(x_speed)
        else:
            self.update_x_pos(x_speed)
        
        self.moving = True
    
    def update_x_pos(self, x_speed):
        if self.die: return
        
        if can_move_here(self.hit_box.x + x_speed , self.hit_box.y , self.hit_box.width, self.hit_box.height -1.5, self.playing.level_manager.get_current_map(), self.playing.level_manager.get_block_entities()):
            self.hit_box.x += x_speed
        else:
            self.hit_box.x = get_entity_x_pos_next_to_wall(self.hit_box, x_speed)
    
    def draw(self, surface: pygame.Surface):        
        
        # pygame.draw.rect(surface,(255, 0, 0), self.hit_box, 2)
        
        surface.blit(pygame.transform.flip(self.animations[self.player_action][self.ani_index], flip_x=self.flip_x, flip_y=0) , (self.hit_box.x - self.x_draw_off_set, self.hit_box.y - self.y_draw_off_set))  
          
        
    def key_down(self ,event: pygame.event.Event):
        if event.key == pygame.K_d:
            self.right = True
        if event.key == pygame.K_a:
            self.left = True
        if event.key == pygame.K_SPACE:
            self.jump = True
        if event.key == pygame.K_r:
            self.die = True
            
    def check_attack(self):
        if self.air_speed <= 0: return
        
        for bot in self.playing.level_manager.get_bots():
            if bot.hit(self.hit_box.x, self.hit_box.y + self.air_speed, self.hit_box.w, self.hit_box.h):
                self.air_speed = -1.5
                self.in_air = True
            
    def key_up(self ,event: pygame.event.Event):
        if event.key == pygame.K_d:
            self.right = False
        if event.key == pygame.K_a:
            self.left = False 
            
    def to_die(self):
        if not self.die:
            self.die = True
            get_sound().play_sfx(get_sound().die)
            self.life_points -= 1
            
    def to_alive(self):
        if  self.die:
            self.die = False
            self.dead = False
            self.air_speed = 0
            self.jump = False
            
            if not self.in_air:
                if not is_entity_on_floor(self.hit_box, self.playing.level_manager.get_current_map()):
                    self.in_air = True
                    
    def win(self):
        self.playing.level_manager.next_level()
        
    def reset(self):
        self.life_points = MAX_LIFE_POINT
        self.in_air = True
        self.die = False
        self.dead = False
        self.jump = False
        self.air_speed = 0