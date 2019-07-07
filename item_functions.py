# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/7/7 22:23
    @Name: item_functions
    @Project: rl_tutorial
"""
import tcod as libtcod
from game_states import GameStates

def heal(*args, **kwargs):
    entity = args[0]
    amount = kwargs.get('amount')
    results = []
    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at full health', libtcod.yellow)})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('Your wounds start to feel better!', libtcod.green)})

    return results