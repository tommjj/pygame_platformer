
import os
import pygame

from game.utils.constants.game_constant import Dir, Game_constant

NUMBER_OF_TILES = 128

player_scale = None
player_animations = None

bot_01_animations = None

card_animation = None
entry_animation = None
jumper_animation = None
platform_animation = None

shooter_animation = None
shooter_animation_left = None
shooter_animation_top = None
shooter_animation_down = None

bullet_animation = None
bullet_animation_left = None
bullet_animation_top = None
bullet_animation_down = None

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


def load_card_animation():
    global card_animation
    
    if card_animation == None:
        card_animation = []
        for i in range(8):
            card_animation.append(loader_with_scale(f'game/res/card/res_{i}.png', 24 * Game_constant.SCALE, 24 * Game_constant.SCALE))
            
    return card_animation

def load_entry_animation():
    global entry_animation
    
    if entry_animation == None:
        entry_animation = []
        for i in range(8):
            entry_animation.append(loader_with_scale(f'game/res/entry/e_{i}.png', Game_constant.TILES_SIZE, 2 * Game_constant.TILES_SIZE))
            
    return entry_animation  
    
def load_jumper_animation():
    global jumper_animation
    
    if jumper_animation == None:
        jumper_animation = []
        for i in range(6):
            jumper_animation.append(loader_with_scale(f'game/res/jumper/0{i}.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))
            
    return jumper_animation  


def load_shooter_animation(dir: Dir):
    global shooter_animation
    global shooter_animation_left 
    global shooter_animation_top 
    global shooter_animation_down 
    
    if shooter_animation == None:
        shooter_animation = []
        for i in range(5):
            shooter_animation.append(loader_with_scale(f'game/res/shooter/{i}.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))
            
    if dir == Dir.RIGHT:
        return shooter_animation
    
    if dir == Dir.LEFT:
        if shooter_animation_left == None:
            shooter_animation_left = []
            for i in range(5):
                shooter_animation_left.append(pygame.transform.rotate(shooter_animation[i], 180))
        return shooter_animation_left
    
    if dir == Dir.DOWN:
        if shooter_animation_down == None:
            shooter_animation_down = []
            for i in range(5):
                shooter_animation_down.append(pygame.transform.rotate(shooter_animation[i], -90))
        return shooter_animation_down
    
    if dir == Dir.TOP:
        if shooter_animation_top == None:
            shooter_animation_top = []
            for i in range(5):
                shooter_animation_top.append(pygame.transform.rotate(shooter_animation[i], 90))
        return shooter_animation_top

def load_bullet_animation(dir: Dir):
    global bullet_animation
    global bullet_animation_left
    global bullet_animation_top 
    global bullet_animation_down

    if bullet_animation == None:
        bullet_animation = []
        for i in range(4):
            bullet_animation.append(loader_with_scale(f'game/res/bullets/b_{i}.png', Game_constant.SCALE * 16, Game_constant.SCALE * 16))
    
    if dir == Dir.RIGHT:
        return bullet_animation
    
    if dir == Dir.LEFT:
        if bullet_animation_left == None:
            bullet_animation_left = []
            for i in range(4):
                bullet_animation_left.append(pygame.transform.rotate(bullet_animation[i], 180))
        return bullet_animation_left
    
    if dir == Dir.DOWN:
        if bullet_animation_down == None:
            bullet_animation_down = []
            for i in range(4):
                bullet_animation_down.append(pygame.transform.rotate(bullet_animation[i], -90))
        return bullet_animation_down
    
    if dir == Dir.TOP:
        if bullet_animation_top == None:
            bullet_animation_top = []
            for i in range(4):
                bullet_animation_top.append(pygame.transform.rotate(bullet_animation[i], 90))
        return bullet_animation_top
 
 
def load_bot_01_animations():
    global bot_01_animations
    
    if bot_01_animations == None:
        bot_01_animations = []
        
        bot_01_animations.append([loader_with_scale('game/res/sprite/robot-1/idle/i_0.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/idle/i_1.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/idle/i_2.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/idle/i_3.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE)])
        
        bot_01_animations.append([loader_with_scale('game/res/sprite/robot-1/walk/w_0.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/walk/w_1.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/walk/w_2.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/walk/w_3.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/walk/w_4.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE),
                                  loader_with_scale('game/res/sprite/robot-1/walk/w_5.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE)])
        
        bot_01_animations.append([loader_with_scale('game/res/sprite/robot-1/turn-off/0.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE)])
                            
        bot_01_animations.append([loader_with_scale('game/res/sprite/robot-1/hurt/00.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE)])
        
    return bot_01_animations
        
def load_platform_animation():
    global platform_animation
    
    if platform_animation == None:
        platform_animation = []
        for i in range(8):
            platform_animation.append(loader_with_scale(f'game/res/platform/p_{i}.png', Game_constant.TILES_SIZE, Game_constant.TILES_SIZE))
    return platform_animation
    