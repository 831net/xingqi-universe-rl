# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/5/14 13:42
    @Name: input_handlers
    @Project: rl_tutorial
"""
import tcod as libtcod
from game_states import GameStates

def handle_keys(key, game_state):
    if game_state ==  GameStates.PLAYERS_TURN:
        return handle_player_turn_keys(key)
    elif game_state == GameStates.PLAYER_DEAD:
        return handle_player_dead_keys(key)
    elif game_state == GameStates.SHOW_INVENTORY:
        return handle_inventory_keys(key)
    return {}


def handle_player_turn_keys(key):
    key_char = chr(key.c)
    # Movement keys
    if key.vk == libtcod.KEY_UP or key_char == 'j' or key_char == 'w':
        return {'move': (0, -1)}
    elif key.vk == libtcod.KEY_DOWN or key_char == 'k' or key_char == 's':
        return {'move': (0, 1)}
    elif key.vk == libtcod.KEY_LEFT or key_char == 'h' or key_char == 'a':
        return {'move': (-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT or key_char == 'l' or key_char == 'd':
        return {'move': (1, 0)}


    elif key_char == 'y' or key_char == 'q':
        return {'move': (-1, -1)}
    elif key_char == 'u'or key_char == 'e':
        return {'move': (1, -1)}
    elif key_char == 'b'or key_char == 'z':
        return {'move': (-1, 1)}
    elif key_char == 'n' or key_char == 'c':
        return {'move': (1, 1)}

    if key_char =='g':
        return {'pickup': True}

    return {}

def handle_player_dead_keys(key):
    key_char = chr(key.c)
    if key_char == 'i':
        return {'show_inventory': True}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    # No key was pressed
    return {}

def handle_inventory_keys(key):
    index = key.c - ord('a')
    if index >= 0:
        return {'inventory_index': index}

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}
    # No key was pressed
    return {}