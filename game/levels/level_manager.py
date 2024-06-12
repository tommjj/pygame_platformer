import pygame

from game.entities.trap import Trap
from game.levels.background import draw_background
from game.levels.level import Game_level
from game.levels.levels_builder.level_builder import get_level_builder
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import load_blocks

class Levels_manager:
    level: Game_level = []
    traps: list[Trap] = []
    layout: list[list[int]] = []
    current_level = 1
    
    def __init__(self, playing) -> None:
        self.playing  = playing
        
        self.reset()
        
        self.blocks = load_blocks()
        
    
    def get_current_map(self):
        return self.level.map
    
    def update(self):
        for trap in self.level.traps:
            trap.update()
             
    def draw_background(self, surface: pygame.Surface):
        draw_background(surface, self.playing.player.hit_box.x)
             
    def draw_tiles(self, surface: pygame.Surface):
        self.draw_layout(surface)
         
        for y, row in enumerate(self.level.map):
            if row != None:
                for x, block in enumerate(row):
                    if block < 126 and block > 0:
                        surface.blit(self.blocks[block] , (Game_constant.TILES_SIZE * x, Game_constant.TILES_SIZE * y, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))

        for trap in self.level.traps:
            trap.draw(surface)
            
    def draw_layout(self, surface: pygame.Surface):
        for y, row in enumerate(self.layout):
            if row != None:
                for x, block in enumerate(row):
                    if block < 126 and block > 0:
                        surface.blit(self.blocks[block] , (Game_constant.TILES_SIZE * x, Game_constant.TILES_SIZE * y, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))

    def reset(self):
        map, layout = get_level_builder(self.playing, self.current_level)
        self.layout = layout
        self.level = map
        
        x, y = self.level.get_player_spawn()
        self.playing.player.hit_box.x = x
        self.playing.player.hit_box.y = y
        
        self.playing.player.to_alive()
        
    def next_level(self):
        self.current_level += 1
        self.reset()
        
    