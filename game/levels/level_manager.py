import pygame

from game.entities.entity import Entity
from game.levels.background import draw_background
from game.levels.level import Game_level
from game.levels.levels_builder.level_builder import NUMBER_OF_LEVEL, get_level_builder
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import NUMBER_OF_TILES, load_blocks

class Levels_manager:
    level: Game_level = []
    layout: list[list[int]] = []
    current_level = 1

    def __init__(self, playing) -> None:
        self.playing = playing

        self.blocks = load_blocks()
        
        self.score = 120
        self.score_reduce_tick = 0
        self.score_reduce_speed = 120

    def get_current_map(self):
        return self.level.map

    def get_block_entities(self):
        return self.level.block_entities

    def get_bots(self):
        return self.level.bots
    
    def update(self):
        self.score_reduce_tick += 1
        if self.score_reduce_tick >= self.score_reduce_speed:
            if self.score > 0:
                self.score -= 1
            self.score_reduce_tick = 0    
        
        for entity in self.level.entities:
            entity.update()

    def draw_background(self, surface: pygame.Surface):
        draw_background(surface, self.playing.player.hit_box.x)

    def draw_tiles(self, surface: pygame.Surface):
        self.draw_layout(surface)

        for y, row in enumerate(self.level.map):
            if row != None:
                for x, block in enumerate(row):
                    if block <= NUMBER_OF_TILES and block > 0:
                        surface.blit(self.blocks[block], (Game_constant.TILES_SIZE * x,
                                     Game_constant.TILES_SIZE * y, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))

        for entity in self.level.entities:
            entity.draw(surface)

    def draw_layout(self, surface: pygame.Surface):
        for y, row in enumerate(self.layout):
            if row != None:
                for x, block in enumerate(row):
                    if block <= NUMBER_OF_TILES and block > 0:
                        surface.blit(self.blocks[block], (Game_constant.TILES_SIZE * x,
                                     Game_constant.TILES_SIZE * y, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))

    def reset(self):
        map, layout = get_level_builder(self.playing, self.current_level)
        self.layout = layout
        self.level = map

        x, y = self.level.get_player_spawn()
        self.playing.player.hit_box.x = x
        self.playing.player.hit_box.y = y
        
        self.score = 120
        self.score_reduce_tick = 0

        self.playing.player.to_alive()

    def next_level(self):
        self.current_level += 1
        if self.current_level > NUMBER_OF_LEVEL:
            self.current_level = 1
        self.reset()
