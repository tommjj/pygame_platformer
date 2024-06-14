import pygame

from game.entities.player import Player
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale

LIFE_POINT_IMAGE_0 = loader_with_scale('game/res/ui/life_point_00.png', 28 * Game_constant.SCALE, 28 * Game_constant.SCALE)
LIFE_POINT_IMAGE_1 = loader_with_scale('game/res/ui/life_point_01.png', 16 * Game_constant.SCALE, 28 * Game_constant.SCALE)

class Life_bar():
    offset_top = 12 * Game_constant.SCALE
    offset_left = 12 * Game_constant.SCALE
    
    def __init__(self, player: Player) -> None:
        self.player = player
    
    def draw(self, surface: pygame.Surface):
        for i in range(self.player.life_points):
            if i == 0:
                surface.blit(LIFE_POINT_IMAGE_0, ( 30 * Game_constant.SCALE * i + self.offset_left ,self.offset_top, 18 * Game_constant.SCALE, 18 * Game_constant.SCALE))
            else:
                surface.blit(LIFE_POINT_IMAGE_1, ( 20 * Game_constant.SCALE * i + self.offset_left + 19 ,self.offset_top, 18 * Game_constant.SCALE, 18 * Game_constant.SCALE))