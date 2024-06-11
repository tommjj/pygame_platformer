import os
from pygame import mixer
import pygame

SOUND_END_EVENT = pygame.USEREVENT + 1

sound = None

class Sound:
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.2)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.allowSFX = True

        self.soundtrack = mixer.Sound(os.path.join( os.getcwd(), "game/res/audio/soundtrack.ogg"))
        self.die = mixer.Sound(os.path.join( os.getcwd(), "game/res/audio/die.ogg"))
        self.jump = mixer.Sound("game/res/audio/jump.ogg")
        
     
        # self.coin = mixer.Sound("./sfx/coin.ogg")
        # self.bump = mixer.Sound("./sfx/bump.ogg")
        # self.stomp = mixer.Sound("./sfx/stomp.ogg")
        # self.jump = mixer.Sound("./sfx/small_jump.ogg")
        # self.death = mixer.Sound("./sfx/death.wav")
        # self.kick = mixer.Sound("./sfx/kick.ogg")
        # self.brick_bump = mixer.Sound("./sfx/brick-bump.ogg")
        # self.powerup = mixer.Sound('./sfx/powerup.ogg')
        # self.powerup_appear = mixer.Sound('./sfx/powerup_appears.ogg')
        # self.pipe = mixer.Sound('./sfx/pipe.ogg')
        

    def play_sfx(self, sfx):
        if self.allowSFX:
            self.sfx_channel.play(sfx)

    def play_music(self, music):
        self.music_channel.play(music)
        self.music_channel.set_endevent(SOUND_END_EVENT)
        
        
def get_sound() -> Sound:
    global sound
    if sound == None:
        sound = Sound()
    return sound