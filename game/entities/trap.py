import pygame

from game.utils.constants.game_constant import Game_constant
from game.utils.loader import loader


class Trap:
    def __init__(self, playing , x, y) -> None:
        self.playing = playing
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, Game_constant.TILES_SIZE, 5 * Game_constant.SCALE)
        self.hit_box_trap = pygame.Rect(x * Game_constant.TILES_SIZE, (y * Game_constant.TILES_SIZE) + (26 * Game_constant.SCALE), Game_constant.TILES_SIZE, 5 * Game_constant.SCALE)
        self.img = pygame.transform.scale(loader('game/res/trap/00.png'), (Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))
    
    def update(self):
        
        if self.hit_box_trap.colliderect(self.playing.player.hit_box):
            self.playing.player.to_die()
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.img , (self.hit_box.x, self.hit_box.y, Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))
        