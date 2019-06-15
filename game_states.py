# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/5/14 23:21
    @Name: game_states
    @Project: rl_tutorial
"""
from enum import Enum
class GameStates(Enum):
    # TODO : use auto variables to control the game_states
    PLAYERS_TURN = 1
    ENEMY_TURN = 2
    PLAYER_DEAD = 3