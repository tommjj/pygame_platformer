from game.levels.levels_builder.level_01_builder import level_01_builder
from game.levels.levels_builder.level_02_builder import level_02_builder
from game.levels.levels_builder.level_03_builder import level_03_builder
from game.levels.levels_builder.level_04_builder import level_04_builder
from game.levels.levels_builder.level_05_builder import level_05_builder

NUMBER_OF_LEVEL = 5

def get_level_builder(playing, level: int):
    if level == 1:
        return level_01_builder(playing)
    if level == 2:
        return level_02_builder(playing)
    if level == 3:
        return level_03_builder(playing)
    if level == 4:
        return level_04_builder(playing)
    if level == 5:
        return level_05_builder(playing)