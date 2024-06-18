from game.entities.bot import Bot_screen
from game.entities.card import Card
from game.entities.crumbling_platform import Crumbling_platform
from game.entities.die_zone import Die_zone
from game.entities.entry import Entry
from game.entities.jumper import Jumper
from game.entities.platform import Platform
from game.entities.shooter import Shooter
from game.entities.trap import Nail_trap
from game.levels.level import Game_level
from game.utils.constants.game_constant import Dir

def level_06_builder(playing):
    map = Game_level()
    map.set_map([[0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 13],
            [0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 13],
            [0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 13],
            [0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 0, 0, 0, 128, 0, 107, 0, 0, 128, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 5, 6, 0, 0, 4, 5, 6, 0, 0, 4, 5, 6, 0, 0, 4, 5, 6, 0, 0, 126, 0, 0, 0, 0],
            [5, 5, 5, 17, 0, 16, 5, 5, 17, 0, 16, 5, 5, 17, 0, 16, 5, 5, 17, 0, 16, 5, 5, 5, 5, 5, 5, 5],
            [0, 0, 82, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 82, 88, 0, 0]])
    
    layout = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 0],
            [27, 27, 27, 27, 71, 27, 27, 27, 27, 71, 27, 27, 27, 27, 71, 27, 27, 27, 27, 71, 27, 27, 27, 27, 71, 27, 27, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [29, 29, 39, 39, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 39, 39, 29, 29]]
    
    map.set_player_spawn(0 , 12) 
    
    map.add_entity(Nail_trap(playing, 6 , 12))
    map.add_entity(Nail_trap(playing, 7 , 12))
    
    map.add_entity(Nail_trap(playing, 8 , 11))
    map.add_entity(Nail_trap(playing, 9 , 11))
    map.add_entity(Nail_trap(playing, 10 , 11))
    
    map.add_entity(Nail_trap(playing, 11 , 12))
    map.add_entity(Nail_trap(playing, 12 , 12))
    map.add_entity(Nail_trap(playing, 13 , 11))
    map.add_entity(Nail_trap(playing, 14 , 11))
    map.add_entity(Nail_trap(playing, 15 , 11))
    map.add_entity(Nail_trap(playing, 16 , 12))
    map.add_entity(Nail_trap(playing, 17 , 12))
    map.add_entity(Nail_trap(playing, 18 , 11))
    map.add_entity(Nail_trap(playing, 19 , 11))
    map.add_entity(Nail_trap(playing, 20 , 11))
    map.add_entity(Nail_trap(playing, 21 , 12))
    map.add_entity(Nail_trap(playing, 22 , 12))
    
    map.add_bot(Bot_screen(playing,8 , 10, Dir.RIGHT))
    map.add_bot(Bot_screen(playing,14 ,10, Dir.RIGHT))
    map.add_bot(Bot_screen(playing,20 ,10, Dir.RIGHT))
        
    card_01 = Card(playing, 11 , 10)
    card_02 = Card(playing, 21 , 10)
    
    entry = Entry(27, 11)
    
    entry.add_card(card_01)
    entry.add_card(card_02)
    map.add_block_entity(entry)
    map.add_entity(card_01)
    map.add_entity(card_02)
    
    return map, layout
