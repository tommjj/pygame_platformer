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

def level_05_builder(playing):
    map = Game_level()
    map.set_map([
            [0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 0, 0, 25],
            [0, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 0, 0, 65],
            [0, 82, 86, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 82, 87, 0, 0, 0, 65],
            [0, 0, 124, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 108, 0, 0, 0, 123, 65],
            [27, 27, 27, 71, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71, 27, 18, 18, 18, 18, 65],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 65],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 126, 0, 0],
            [5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5],
            [0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0],
            [0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0]])
    
    layout = [[21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [29, 39, 39, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 39, 39, 29, 29, 39, 29],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 19, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 19, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 19, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 19, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 19, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 19, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 21, 19, 0],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 19, 21],
            [29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 39, 29],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]]
    
    map.set_player_spawn(0 , 3) 
    
    map.add_entity(Nail_trap(playing, 4 , 14))
    map.add_entity(Nail_trap(playing, 5 , 14))
    map.add_entity(Nail_trap(playing, 6 , 14))
    map.add_entity(Nail_trap(playing, 7 , 14))
    map.add_entity(Nail_trap(playing, 8 , 14))
    map.add_entity(Nail_trap(playing, 9 , 14))
    map.add_entity(Nail_trap(playing, 10 , 14))
    map.add_entity(Nail_trap(playing, 11 , 14))
    map.add_entity(Nail_trap(playing, 12 , 14))
    map.add_entity(Nail_trap(playing, 13 , 14))
    map.add_entity(Nail_trap(playing, 14 , 14))
    map.add_entity(Nail_trap(playing, 15 , 14))
    map.add_entity(Nail_trap(playing, 16 , 14))
    map.add_entity(Nail_trap(playing, 17 , 14))
    map.add_entity(Nail_trap(playing, 18 , 14))
    map.add_entity(Nail_trap(playing, 19 , 14))
    map.add_entity(Nail_trap(playing, 20 , 14))
    map.add_entity(Nail_trap(playing, 21 , 14))
    
    map.add_bot(Bot_screen(playing,26 ,3, Dir.RIGHT))
        
    card_01 = Card(playing, 26 , 3)
    card_02 = Card(playing, 2 , 11)
    
    map.add_block_entity(Crumbling_platform(playing, 8, 4))
    map.add_block_entity(Crumbling_platform(playing, 14, 4))
    
    map.add_block_entity(Crumbling_platform(playing, 9, 12))
    map.add_block_entity(Crumbling_platform(playing, 15, 12))
    
    entry = Entry(27, 10)
    
    entry.add_card(card_01)
    entry.add_card(card_02)
    map.add_block_entity(entry)
    map.add_entity(card_01)
    map.add_entity(card_02)
    
    return map, layout
