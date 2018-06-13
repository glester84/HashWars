# -*- coding: utf-8 -*-

def play(grid, player_id):
    for i in range(1, 10):
        if grid[i] == 0:
            return i
    return 0
