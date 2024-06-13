from game.levels.levels_builder.level_01_builder import level_01_builder
from game.levels.levels_builder.level_02_builder import level_02_builder

NUMBER_OF_LEVEL = 2

def get_level_builder(playing, level: int):
    if level == 1:
        return level_01_builder(playing)
    if level == 2:
        return level_02_builder(playing)