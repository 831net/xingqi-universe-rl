# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/5/14 14:52
    @Name: tile
    @Project: rl_tutorial
"""

class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """

    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked
        self.explored = False

        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight