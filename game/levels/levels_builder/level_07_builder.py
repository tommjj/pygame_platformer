from game.entities.bot import Bot_screen
from game.entities.card import Card
from game.entities.crumbling_platform import Crumbling_platform
from game.entities.entry import Entry
from game.entities.platform import Platform
from game.entities.shooter import Shooter
from game.entities.trap import Nail_trap
from game.levels.level import Game_level
from game.utils.constants.game_constant import Dir

def level_07_builder(playing):
    map = Game_level()
    map.set_map([ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 126, 0, 0, 0, 109, 110, 110, 111, 0, 0, 0, 109, 110, 110, 111, 0, 0, 0, 109, 110, 110, 111, 0, 0, 13],
            [5, 5, 5, 6, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 4, 5, 5, 6, 0, 0, 13],
            [0, 0, 0, 15, 0, 0, 0, 13, 0, 0, 15, 0, 0, 0, 13, 0, 0, 15, 0, 0, 0, 13, 0, 0, 15, 0, 0, 13],
            [82, 88, 0, 15, 0, 0, 0, 13, 0, 0, 15, 0, 0, 0, 13, 0, 0, 15, 0, 0, 0, 13, 0, 0, 15, 0, 125, 13],
            [0, 0, 0, 16, 6, 0, 4, 17, 0, 0, 16, 5, 5, 5, 17, 0, 0, 16, 5, 5, 5, 17, 0, 0, 16, 5, 5, 17],
            [0, 0, 0, 0, 15, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 15, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 82, 89, 0, 0],
            [0, 0, 7, 23, 24, 0, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23],
            [0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 126, 0, 0, 0, 0, 0],
            [0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 6, 0, 0, 0, 31, 32, 33, 0, 0, 0, 4],
            [0, 0, 16, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 17, 0, 0, 0, 15, 0, 0, 0, 40, 0, 42, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 40, 0, 42, 0, 0, 0, 13]])
    
    layout = [[21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [21, 21, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0],
            [39, 39, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0],
            [21, 19, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0, 0, 21, 21, 0, 0, 0, 0],
            [21, 19, 21, 21, 0, 0, 0, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 19, 21, 21, 0, 0, 0, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 38, 29, 29, 29, 29, 29, 29, 39, 39, 29, 29],
            [21, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [21, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21],
            [21, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21],
            [21, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [21, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 21, 21, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0],
            [21, 19, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0]]
    
    map.set_player_spawn(0 , 2) 
    
    map.add_entity(Nail_trap(playing, 4 , 5))
    map.add_entity(Nail_trap(playing, 6 , 5))
    
    map.add_entity(Nail_trap(playing, 9 , 12))
    map.add_entity(Nail_trap(playing, 8 , 12))
    
    map.add_entity(Nail_trap(playing, 8 , 2))
    map.add_entity(Nail_trap(playing, 9 , 2))
    map.add_entity(Nail_trap(playing, 11 , 5))
    map.add_entity(Nail_trap(playing, 12 , 5))
    map.add_entity(Nail_trap(playing, 13 , 5))
    
    
    map.add_entity(Nail_trap(playing, 15 , 2))
    map.add_entity(Nail_trap(playing, 16 , 2))
    
    map.add_entity(Nail_trap(playing, 18 , 5))
    map.add_entity(Nail_trap(playing, 19 , 5))
    map.add_entity(Nail_trap(playing, 20 , 5))
    
    map.add_entity(Nail_trap(playing, 22 , 2))
    map.add_entity(Nail_trap(playing, 23 , 2))
    map.add_entity(Nail_trap(playing, 25 , 5))
    map.add_entity(Nail_trap(playing, 26 , 5))
    
    
    map.add_bot(Bot_screen(playing,8 , 10, Dir.RIGHT))
    
    map.add_entity(Nail_trap(playing, 18 , 14))
    map.add_entity(Nail_trap(playing, 19 , 14))
    map.add_entity(Nail_trap(playing, 20 , 14))
    
    map.add_entity(Nail_trap(playing, 24 , 14))
    map.add_entity(Nail_trap(playing, 25 , 14))
    map.add_entity(Nail_trap(playing, 26 , 14))
    
    map.add_entity(Shooter(playing, 5, 0, Dir.DOWN, 0, 240))
    map.add_entity(Shooter(playing, 12, 0, Dir.DOWN, 0, 240))
    map.add_entity(Shooter(playing, 19, 0, Dir.DOWN, 0, 240))
    
        
    card_01 = Card(playing, 25 , 1)
    
    entry = Entry(27, 10)
    
    entry.add_card(card_01)
    map.add_block_entity(entry)
    map.add_entity(card_01)
    
    return map, layout
