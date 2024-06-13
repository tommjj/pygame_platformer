from xml.dom.minidom import Entity
import pygame

from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader

BOTTOM_NAIL_TRAP_IMAGE = pygame.transform.scale(loader('game/res/trap/00.png'), (Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))
RIGHT_NAIL_TRAP_IMAGE = pygame.transform.rotate(BOTTOM_NAIL_TRAP_IMAGE, 90)
TOP_NAIL_TRAP_IMAGE = pygame.transform.rotate(BOTTOM_NAIL_TRAP_IMAGE, 180)
LEFT_NAIL_TRAP_IMAGE =  pygame.transform.rotate(BOTTOM_NAIL_TRAP_IMAGE, -90)

class Nail_trap(Entity):
    TOP = 'TOP'
    BOTTOM = 'BOTTOM'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    
    def __init__(self, playing, x, y, dir = 'BOTTOM') -> None:
        self.playing = playing
        
        self.dir = dir
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, Game_constant.TILES_SIZE, 5 * Game_constant.SCALE)
        
        if dir == self.BOTTOM:
            self.hit_box_trap = pygame.Rect(x * Game_constant.TILES_SIZE, (y * Game_constant.TILES_SIZE) + (26 * Game_constant.SCALE), Game_constant.TILES_SIZE, 5 * Game_constant.SCALE)
            self.img = BOTTOM_NAIL_TRAP_IMAGE
            
        if dir == self.RIGHT:
            self.hit_box_trap = pygame.Rect(x * Game_constant.TILES_SIZE + 26 * Game_constant.SCALE, (y * Game_constant.TILES_SIZE), 5 * Game_constant.SCALE, Game_constant.TILES_SIZE)
            self.img = RIGHT_NAIL_TRAP_IMAGE
            
        if dir == self.TOP:
            self.hit_box_trap = pygame.Rect(x * Game_constant.TILES_SIZE, (y * Game_constant.TILES_SIZE) , Game_constant.TILES_SIZE, 5 * Game_constant.SCALE)
            self.img = TOP_NAIL_TRAP_IMAGE
            
        if dir == self.LEFT:
            self.hit_box_trap = pygame.Rect(x * Game_constant.TILES_SIZE, (y * Game_constant.TILES_SIZE), 5 * Game_constant.SCALE, Game_constant.TILES_SIZE)
            self.img = LEFT_NAIL_TRAP_IMAGE
            

    def update(self):
        if self.hit_box_trap.colliderect(self.playing.player.hit_box):
            self.playing.player.to_die()

    def draw(self, surface: pygame.Surface):
        surface.blit(self.img, (self.hit_box.x, self.hit_box.y, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))
    