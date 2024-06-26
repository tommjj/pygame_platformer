from game.entities.card import Card
from game.entities.die_zone import Die_zone
from game.entities.entry import Entry
from game.entities.trap import Nail_trap
from game.levels.level import Game_level
from game.utils.constants.game_constant import Dir


def level_02_builder(playing):
    map = Game_level()
    map.set_map([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 13, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71, 0, 0, 71, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 13, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 13, 21],
            [110, 110, 110, 0, 124, 0, 0, 0, 0, 0, 128, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 13, 21],
            [27, 27, 27, 27, 71, 0, 0, 0, 0, 0, 128, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 71, 18, 18, 18, 13, 21],
            [0, 0, 0, 0, 0, 0, 124, 110, 0, 0, 128, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 82, 84, 0, 13, 21],
            [0, 0, 0, 0, 0, 0, 27, 27, 0, 0, 128, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 21],
            [0, 0, 82, 83, 0, 0, 0, 0, 0, 0, 128, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27, 0, 0, 128, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71, 0, 0, 109, 110, 110, 110, 111, 126, 0, 96, 0, 97, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [0, 96, 93, 0, 0, 108, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [5, 5, 5, 5, 5, 6, 27, 27, 27, 0, 0, 0, 0, 0, 0, 27, 13, 21, 39, 29, 29, 29, 29, 29, 29, 29, 29, 29],
            [29, 29, 29, 29, 39, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 21, 19, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 19, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 21, 19, 21, 21, 21, 21, 21, 21, 21, 21, 21]])
    
    layout = [[21, 21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21],
            [29, 29, 29, 29, 29, 29, 29, 29, 29, 25, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 25, 29, 29, 29, 29, 29, 29, 29],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 29, 29, 29, 29, 29, 29, 29, 29, 29],
            [21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 122, 21, 21, 21],
            [29, 29, 29, 29, 29, 29, 29, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 2, 110, 0, 0, 0, 0, 0, 0, 111, 61, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 2, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],
            [21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]]
    
   
    map.set_player_spawn(0 , 11)

    map.add_entity(Nail_trap(playing, 15, 10, Dir.RIGHT))
    map.add_entity(Nail_trap(playing, 6, 5))
    map.add_entity(Nail_trap(playing, 3, 3))
    map.add_entity(Nail_trap(playing, 13, 10, Dir.TOP))
    
    map.add_entity(Die_zone(playing, 6, 14, 10, 1))
    
    card = Card(playing, 2 , 3)
    entry = Entry(27, 8)
    
    entry.add_card(card)
    map.add_block_entity(entry)
    map.add_entity(card)
    
    return map, layout
