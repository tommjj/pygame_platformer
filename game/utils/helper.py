import pygame

from game.entities.entity import Entity
from game.utils.constants.game_constant import Game_constant


def can_move_here(x, y, width, height ,map: list[list[int]], block_entities: list[Entity] = [] ):
    can_move = False
    
    if not is_solid(x, y, map):
        if not is_solid(x + width, y + height, map):
            if not is_solid(x + width, y, map):
                if not is_solid(x, y + height, map):
                    can_move = True
    
    for e in block_entities:
        if e.get_hit_box().colliderect(x, y, width, height):
            return False
    
    return can_move

def is_solid(x: float, y: float, map: list[list[int]] ):
    if (x < 0):
        return True    
    if (y < 0 or y >= Game_constant.GAME_HEIGHT):
        return True
    
    if x >= Game_constant.GAME_WIDTH:
        return False
    
    x_index = int(x / Game_constant.TILES_SIZE)
    y_index = int(y / Game_constant.TILES_SIZE)

    return is_tile_solid(x_index, y_index, map)
    
def is_tile_solid(x: int, y: int, map: list[list[int]]):
    value = map[y][x]
    
    return is_tiles(value)


def get_entity_y_pos_under_roof_of_above_floor(hit_box: pygame.Rect, air_speed):
    current_tile = int((hit_box.y + (hit_box.h/ 2)) / Game_constant.TILES_SIZE)
    
    if air_speed > 0: # fall
        tile_y_pos = current_tile * Game_constant.TILES_SIZE
        yOffset = int(Game_constant.TILES_SIZE - hit_box.height)
        return tile_y_pos + yOffset - 1
    else: # jump
        return current_tile * Game_constant.TILES_SIZE
    
def get_entity_x_pos_next_to_wall(hit_box: pygame.Rect, x_speed): 
    current_tile = int((hit_box.x + hit_box.w/2) / Game_constant.TILES_SIZE)
    
    if x_speed > 0: 
        tile_x_pos = current_tile * Game_constant.TILES_SIZE
        yOffset = int(Game_constant.TILES_SIZE - hit_box.width)
        return tile_x_pos + yOffset - 1
    else:
        return current_tile * Game_constant.TILES_SIZE
    

def is_entity_on_floor(hit_box: pygame.Rect, map: list[list[int]], block_entities: list[Entity] = []):
    
    if is_solid(hit_box.x + hit_box.width, hit_box.y + hit_box.height + 1 * Game_constant.SCALE, map):
        return True
    if is_solid(hit_box.x, hit_box.y + hit_box.height + 1 * Game_constant.SCALE, map): 
        return True
        
    for e in block_entities:
        if e.get_hit_box().colliderect(hit_box.x, hit_box.y, hit_box.width, hit_box.height + 2.5 * Game_constant.SCALE):
            return True
                    
    return False


def is_tiles(block) -> bool:
    return block > 0 and block < 82

