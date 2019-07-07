# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/6/16 18:35
    @Name: inventory
    @Project: rl_tutorial
"""
import tcod as libtcod
from game_messages import Message

class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def add_item(self, item):
        results = []
        if len(self.items) >= self.capacity:
            results.append({
            'item_added' : None,
            'message': Message('You cannott carry more, your inventory is full',libtcod.yellow)
            })
        else:
            results.append({
                'item_added': item,
                'message':Message('You pick up the {0}!'.format(item.name), libtcod.blue)
            })