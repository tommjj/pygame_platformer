
import pygame
from game.entities.entity import Entity
from game.utils.constants.game_constant import Game_constant
from game.utils.helper import is_tile_solid


def is_solid(x: float, y: float, map: list[list[int]] ):
    if (x < 0 or x >=  Game_constant.GAME_WIDTH):
        return False    
    if (y < 0 or y >= Game_constant.GAME_HEIGHT):
        return False
    
    x_index = int(x / Game_constant.TILES_SIZE)
    y_index = int(y / Game_constant.TILES_SIZE)

    return is_tile_solid(x_index, y_index, map)

def is_floor(hit_box: pygame.Rect, speed: float, map: list[list[int]]):
    if speed > 0:
        return is_solid(hit_box.x + hit_box.w + speed , hit_box.y + hit_box.h + 2, map)
    return is_solid(hit_box.x + speed , hit_box.y + hit_box.h + 2, map)