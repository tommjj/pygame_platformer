import pygame

from game.entities.card import Card
from game.entities.entity import Entity
from game.utils.constants.game_constant import Game_constant
from game.utils.loader import load_entry_animation

class Entry(Entity):  
    def __init__(self, x, y) -> None:
        super().__init__()
        
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, Game_constant.TILES_SIZE, 2 * Game_constant.TILES_SIZE)
        
        self.is_open = False
        self.animation_tick = 0
        self.animation_index = 0
        self.animation = load_entry_animation()
        self.animation_len = len(self.animation)
        self.animation_speed = 16
        self.cards: list[Card] = []
        
    def get_hit_box(self):
        if self.is_open:
            return pygame.Rect(0, 0, 0, 0)
        return self.hit_box
    
    def set_pos(self, x, y):
        self.hit_box = pygame.Rect(x * Game_constant.TILES_SIZE, y * Game_constant.TILES_SIZE, Game_constant.TILES_SIZE, 2 * Game_constant.TILES_SIZE)
    
    def add_card(self, card):
        self.cards.append(card)
        
    def set_card(self, cards: list[Card]):
        self.cards = cards
    
    def update(self):
        are_all_cards_not_alive = False
        for card in self.cards:
            if card.is_alive:
                are_all_cards_not_alive = True
                break
        
        self.is_open = not are_all_cards_not_alive
        
        self.update_animation()
        
    
    def update_animation(self):
        self.animation_tick += 1
             
        if self.animation_tick >= self.animation_speed:
            self.animation_tick = 0
            
            if self.is_open and self.animation_index < 4:
                self.animation_index += 1
            elif not self.is_open and self.animation_index > 0:    
                self.animation_index += 1
                if self.animation_index >= self.animation_len:
                    self.animation_index = 0
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.animation[self.animation_index], self.hit_box)
    