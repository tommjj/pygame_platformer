
import os
import pygame

from game.utils.constants.game_constant import Game_constant

NUMBER_OF_TILES = 128

player_scale = None
player_animations = None

blocks = None

def res_path(path):
    return os.path.join( os.getcwd(), f'game/res/{path}')

def loader(path):
    return pygame.image.load(os.path.join( os.getcwd(), path))

def loader_with_scale(path, w, h):
    return pygame.transform.scale(loader(path), (w, h))

def load_player_animations(w):
    global player_scale
    global player_animations
    
    player_scale = w
    if player_animations == None:
        player_animations = [[pygame.transform.scale(loader('game/res/player02/idle/00.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/01.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/02.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/03.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/04.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/05.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/06.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/07.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/08.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/09.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/010.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/011.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/012.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/013.png'), (w,w))], 
            [pygame.transform.scale(loader('game/res/player02/running/00.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/running/01.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/running/02.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/03.png'), (w, w)),  pygame.transform.scale(loader('game/res/player02/running/04.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/05.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/06.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/07.png'), (w, w))],
            [pygame.transform.scale(loader('game/res/player02/jump/01.png'), (w, w))],
            [pygame.transform.scale(loader('game/res/player02/jump/05.png'), (w, w))], 
            [ pygame.transform.scale(loader('game/res/player02/die/08.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/09.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/010.png'), (w, w))
            , pygame.transform.scale(loader('game/res/player02/die/011.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/012.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/013.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/014.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/015.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/016.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/017.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/018.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/019.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/020.png'), (w, w))]]
    elif player_scale != w:
        player_animations = [[pygame.transform.scale(loader('game/res/player02/idle/00.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/01.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/02.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/03.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/04.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/05.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/06.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/07.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/08.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/09.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/010.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/011.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/idle/012.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/idle/013.png'), (w,w))], 
            [pygame.transform.scale(loader('game/res/player02/running/00.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/running/01.png'), (w, w)),pygame.transform.scale(loader('game/res/player02/running/02.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/03.png'), (w, w)),  pygame.transform.scale(loader('game/res/player02/running/04.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/05.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/06.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/running/07.png'), (w, w))],
            [pygame.transform.scale(loader('game/res/player02/jump/01.png'), (w, w))],
            [pygame.transform.scale(loader('game/res/player02/jump/05.png'), (w, w))], 
            [pygame.transform.scale(loader('game/res/player02/die/08.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/09.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/010.png'), (w, w))
            , pygame.transform.scale(loader('game/res/player02/die/011.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/012.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/013.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/014.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/015.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/016.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/017.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/018.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/019.png'), (w, w)), pygame.transform.scale(loader('game/res/player02/die/020.png'), (w, w))]]
    return player_animations


def tile_loader(name: str) -> pygame.Surface:
    return pygame.transform.scale(loader(f'game/res/Tiles/{name}.png'), (Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))

def load_blocks():
    global blocks
    
    if blocks == None:
        blocks = [None]
        for i in range(1, NUMBER_OF_TILES+1):
            blocks.append(tile_loader(i))
    
    return blocks