from enum import Enum

class Game_constant():
    TILES_DEFAULT_SIZE = 32
    SCALE = 1.5
    TILES_IN_WIDTH = 28
    TILES_IN_HEIGHT = 15
    TILES_SIZE = int(TILES_DEFAULT_SIZE * SCALE)
    GAME_WIDTH = TILES_SIZE * TILES_IN_WIDTH
    GAME_HEIGHT = TILES_SIZE * TILES_IN_HEIGHT



class Game_state(Enum):
    PLAYING = "PLAYING"
    MENU = "MENU"
    SELECT_LEVEL="SELECT_LEVEL"
    PAUSE = "PAUSE"
    
    