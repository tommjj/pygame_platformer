from pygame import Rect
import pygame
from game.entities.entity import Entity
from game.utils.constants.game_constant import Game_constant

class Die_zone(Entity): 
    
    def __init__(self, playing,  x, y, w, h, asTile: bool = True) -> None:
        self.playing = playing
        
        a = Game_constant.TILES_SIZE if asTile else 1
        self.hit_box = Rect(x * a, y * a, w * a, h * a)     

    def update(self):
        if self.hit_box.colliderect(self.playing.player.hit_box):
            self.playing.player.to_die()
