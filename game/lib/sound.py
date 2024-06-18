import os
from pygame import mixer
import pygame

SOUND_END_EVENT = pygame.USEREVENT + 1

sound = None

class Sound:
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.08)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.2)

        self.allowSFX = True

        self.soundtrack = mixer.Sound(os.path.join( os.getcwd(), "game/res/audio/theme.ogg"))
        self.die = mixer.Sound(os.path.join( os.getcwd(), "game/res/audio/die.ogg"))
        self.jump = mixer.Sound("game/res/audio/jump.ogg")
        self.jumper = mixer.Sound("game/res/audio/jumper.ogg")
        self.card_collect = mixer.Sound("game/res/audio/card_collect.ogg")
        self.stun_bot = mixer.Sound("game/res/audio/stun_bot.ogg")
        self.open_doors = mixer.Sound("game/res/audio/open_doors.ogg")
        
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