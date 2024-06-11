from enum import Enum

IDLE = 0
RUNNING = 1
JUMP = 2
FALLING = 3
DEAD = 4
# ATTACK = 4
HIT = 5

def get_sprites_amount(player_action):
    if player_action == IDLE:
        return 14
    if player_action == RUNNING:
        return 8
    if player_action == JUMP:
        return 1
    if player_action == FALLING:
        return 1
    if player_action == DEAD:
        return 13
    return 0