import pygame
from game.entities.entity import Entity


class Jumper(Entity):
    def __init__(self) -> None:
        super().__init__()