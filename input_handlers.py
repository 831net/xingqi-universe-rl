# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/5/14 13:42
    @Name: input_handlers
    @Project: rl_tutorial
"""
import tcod as libtcod


def handle_keys(key):
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
    # elif key.vk == libtcod.KEY_CHAR:
    #    if key.c == ord('w'):
    #        return {'move' : (0, -1)}
    #    elif key.c == ord('s'):
    #        return {'move': (0, 1)}
    #    elif key.c == ord('a'):
    #        return {'move': (-1, 0)}
    #    elif key.c == ord('d'):
    #        return {'move': (1, 0)}

    # TODO: add oblique movement key control
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif key.vk == libtcod.KEY_ESCAPE:
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}
