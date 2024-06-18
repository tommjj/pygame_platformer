class Game_state:
    playing = "PLAYING"
    menu = "MENU"
    high_score = "HIGH_SCORE"

class State_control:
    def set_state(self, game_state: Game_state):
        pass
    
class Playing_state:
    PLAY = "PLAY"
    PAUSE = "PAUSE" 
    RESULT = "RESULT"
    
class Playing_state_control:
    def set_state(self, game_state: Playing_state):
        pass