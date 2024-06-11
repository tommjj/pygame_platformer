import pygame
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader_with_scale


BG_IMAGE_1 = loader_with_scale('game/res/Background/2.png', Game_constant.GAME_WIDTH , Game_constant.GAME_HEIGHT)
BG_IMAGE_2 = loader_with_scale('game/res/Background/3.png', Game_constant.GAME_WIDTH , Game_constant.GAME_HEIGHT)
BG_IMAGE_3 = loader_with_scale('game/res/Background/4.png', Game_constant.GAME_WIDTH , Game_constant.GAME_HEIGHT)
BG_IMAGE_4 = loader_with_scale('game/res/Background/5.png', Game_constant.GAME_WIDTH , Game_constant.GAME_HEIGHT)

MAX_OFFSET = 250

def draw_background(surface: pygame.Surface, x) -> None:
    offset = MAX_OFFSET - (Game_constant.GAME_WIDTH - x) / Game_constant.GAME_WIDTH * MAX_OFFSET
        
    surface.fill('#CAF4FF')
    
    surface.blit(BG_IMAGE_1, (-offset * 0.2, 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
    surface.blit(BG_IMAGE_1, (Game_constant.GAME_WIDTH + (-offset * 0.2), 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
    
    surface.blit(BG_IMAGE_2, (-offset * 0.38, 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
    surface.blit(BG_IMAGE_2, (Game_constant.GAME_WIDTH+(-offset * 0.38), 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
    
    surface.blit(BG_IMAGE_3, (-offset * 0.7, 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
    surface.blit(BG_IMAGE_3, (Game_constant.GAME_WIDTH+(-offset * 0.7), 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
    
    surface.blit(BG_IMAGE_4, (-offset, 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))
    surface.blit(BG_IMAGE_4, (Game_constant.GAME_WIDTH - offset, 0, Game_constant.GAME_WIDTH, Game_constant.GAME_HEIGHT))