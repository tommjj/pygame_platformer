from game.entities.die_zone import Die_zone
from game.entities.trap import Nail_trap
from game.levels.level import Game_level


def level_02_builder(playing):
    map = Game_level()
    map.set_map([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [110, 110, 110, 110, 110, 124, 0, 110, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [27, 27, 27, 27, 71, 18, 0, 18, 71, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 82, 84, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 82, 83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 109, 110, 110, 110, 111, 126, 0, 96, 0, 97, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [0, 96, 93, 0, 0, 108, 124, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [5, 5, 5, 5, 5, 6, 27, 27, 27, 27, 0, 0, 0, 0, 0, 27, 13, 21, 39, 29, 29, 29, 29, 29, 29, 29, 29, 29],
            [29, 29, 29, 29, 39, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 21, 19, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 19, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 21, 19, 21, 21, 21, 21, 21, 21, 21, 21, 21]])
    
    layout = [[21, 21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21],
            [29, 29, 29, 29, 29, 29, 29, 29, 29, 2, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 2, 29, 29, 29, 29, 29, 29, 29],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 4, 5],
            [21, 21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 13, 14],
            [21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 29, 29, 29, 29, 29, 29, 29, 13, 14],
            [21, 21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 122, 21, 13, 14],
            [29, 29, 29, 29, 29, 29, 29, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 2, 110, 0, 0, 0, 0, 0, 0, 111, 61, 0, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 2, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29],
            [21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 2, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]]
    
   
    map.set_player_spawn(0 , 11)

    map.add_trap(Nail_trap(playing, 15, 10, Nail_trap.RIGHT))
    map.add_trap(Die_zone(playing, 6, 14, 10, 1))
    
    return map, layout
