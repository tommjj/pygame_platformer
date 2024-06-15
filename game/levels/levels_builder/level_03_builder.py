from game.entities.die_zone import Die_zone
from game.entities.trap import Nail_trap
from game.levels.level import Game_level


def level_03_builder(playing):
    map = Game_level()
    map.set_map([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 128, 0, 0, 0, 128, 0, 0, 0, 128, 0, 0, 0, 128, 0, 0, 0],
            [23, 23, 23, 23, 23, 23, 23, 8, 0, 0, 0, 0, 128, 0, 0, 0, 128, 0, 0, 0, 128, 0, 0, 0, 128, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 22, 23, 8, 0, 0, 71, 18, 18, 18, 71, 27, 27, 27, 71, 27, 27, 27, 71, 27, 27, 27],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23, 8, 0, 0, 0, 0, 128, 0, 82, 39, 128, 0, 0, 0, 128, 0, 0, 0],
            [110, 0, 0, 124,0 , 0, 0, 0, 0, 0, 0, 22, 23, 8, 0, 0, 128, 108, 0, 0, 128, 124, 0, 0, 128, 0, 0, 0],
            [5, 5, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23, 8, 71, 27, 27, 27, 71, 18, 18, 18, 71, 18, 18, 18],
            [0, 0, 0, 0, 16, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23, 8, 0, 0, 128, 82, 85, 0, 128, 0, 0, 0],
            [0, 0, 82, 84, 0, 36, 16, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23, 8, 128, 0, 0, 0, 128, 0, 0, 0],
            [0, 0, 0, 19, 0, 128, 0, 0, 16, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23, 8, 18, 18, 71, 18, 18, 18],
            [0, 0, 0, 19, 0, 128, 0, 0, 0, 0, 16, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 22, 23, 23, 23, 23, 23, 23],
            [27, 27, 27, 27, 27, 27, 0, 0, 0, 0, 0, 0, 16, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 107, 121, 0, 0, 0, 16, 5, 6, 0, 0, 0, 119, 122, 0, 126, 0, 0],
            [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    
    layout = [[21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 38, 29, 29, 39, 39, 29, 29, 29, 29, 29, 29, 29, 29],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [5, 5, 5, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 16, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 38, 29, 39, 39, 29, 29, 29, 29, 29],
            [29, 29, 39, 39, 21, 21, 16, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 16, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 16, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [20, 20, 20, 39, 20, 20, 20, 20, 20, 20, 20, 39, 16, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 21, 21, 16, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 21, 21, 21, 21, 16, 5, 6, 21, 21, 21, 21, 21, 21, 21, 21, 21],
            [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32],
            [41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41, 41]]
    
   
    map.set_player_spawn(0 , 4)

    map.add_entity(Nail_trap(playing, 4, 4))
    map.add_entity(Nail_trap(playing, 6, 5))
    map.add_entity(Nail_trap(playing, 8, 6))
    map.add_entity(Nail_trap(playing, 10, 7))
    map.add_entity(Nail_trap(playing, 12, 8))
    map.add_entity(Nail_trap(playing, 14, 9))
    map.add_entity(Nail_trap(playing, 16, 10))
    map.add_entity(Nail_trap(playing, 18, 11))
    map.add_entity(Nail_trap(playing, 20, 12))
    map.add_entity(Nail_trap(playing, 22, 12))
    
    return map, layout
