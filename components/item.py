# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/6/16 18:36
    @Name: item
    @Project: rl_tutorial
"""
class Item:
    def __init__(self, use_function=None, **kwargs):
        self.use_function = use_function
        self.function_kwargs = kwargs
        

