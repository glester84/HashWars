# -*- coding: utf-8 -*-
import random

lines = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

def win(grid):
    for boxes in lines:
        val = grid[boxes[0]]
        if val != 0:
            hit = True
            for box in boxes:
                if grid[box] != val:
                    hit = False
                    break
            if hit:
                return val
    return 0

def pick_a_winner(grid, player_id):
    for i in range(1, 10):
        if grid[i] == 0:
            grid[i] = player_id
            if win(grid) == player_id:
                return i
            grid[i] = 0
    return None

def pick_a_blocker(grid, player_id):
    for i in range(1, 10):
        if grid[i] == 0:
            grid[i] = 3 - player_id
            if win(grid) == 3 - player_id:
                return i
            grid[i] = 0
    return None

def pick_something(grid, player_id):
    while True:
        i = random.randint(1, 9)
        if grid[i] == 0:
            return i
    return None

def play(grid, player_id):
    return (
        pick_a_winner(grid, player_id) or
        pick_a_blocker(grid, player_id) or
        pick_something(grid, player_id)
    )
