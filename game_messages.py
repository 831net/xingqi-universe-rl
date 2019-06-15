# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/6/16 00:02
    @Name: game_messages
    @Project: rl_tutorial
"""
import  tcod as libtcod
import textwrap

class Message:
    def __init__(self, text, color=libtcod.white):
        self.text = text
        self.color = color

class MessageLog:
    def __init__(self, x, width, height):
        self.messages = []
        self.x = x
        self.width = width
        self.height = height

    def add_message(self, message):
        new_mgs_lines = textwrap.wrap(message.text, self.width)
        for line in new_mgs_lines:
            if len(self.messages) == self.height:
                del self.messages[0]

            self.messages.append(Message(line, message.color))
