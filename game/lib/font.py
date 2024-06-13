import pygame

from game.utils.loader import res_path
from game.utils.constants.game_constant import Game_constant

class Game_font(pygame.font.Font):
    def __init__(self, size: int = Game_constant.TILES_SIZE) -> None:
        super().__init__(res_path('font/m6x11.ttf'), size)
