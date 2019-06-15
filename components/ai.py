# -*- coding: utf-8 -*-
"""
    @Author: Xingqi Tang
    @Created: 2019/5/15 14:16
    @Name: ai
    @Project: rl_tutorial
"""
import tcod as libtcod
class BasicMonster:
    def take_turn(self, target, fov_map, game_map,  entities):
        results = []
        monster = self.owner

        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):

            if monster.distance_to(target)>=2:
                monster.move_astar(target, entities, game_map)

            elif target.fighter.hp > 0:

                attack_results = monster.fighter.attack(target)
                results.extend(attack_results)
                # print('The {0} hurts you! Care!'.format(monster.name))
        return results