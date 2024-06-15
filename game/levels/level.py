import pygame

from game.entities.entity import Entity
from game.utils.constants.game_constant import Game_constant

# from ..utils.constants.game_constant import


class Game_level:
    def __init__(self) -> None:
        self.map: list[list[int]] = [[]]
        self.entities: list[Entity] = []
        self.block_entities: list[Entity] = []

    def set_player_spawn(self, x: int, y: int):
        self.player_spawn_x = x
        self.player_spawn_y = y

    def get_player_spawn(self):
        return self.player_spawn_x * Game_constant.TILES_SIZE, self.player_spawn_y * Game_constant.TILES_SIZE

    def set_map(self, map):
        self.map = map

    def add_entity(self, entity):
        self.entities.append(entity)
        
    def add_block_entity(self, entity):
        self.block_entities.append(entity)
        self.entities.append(entity)
