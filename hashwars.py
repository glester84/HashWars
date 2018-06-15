# -*- coding: utf-8 -*-

import sys
import importlib
from datetime import datetime
from itertools import cycle

if __file__ in sys.argv[0]:
    sys.argv = sys.argv[1:]

argv = {
    'p1': 'human',
    'p2': 'human',
    'v': False,
    'rounds': 1,
}

lines = {
    'top': [1, 2, 3],
    'middle': [4, 5, 6],
    'bottom': [7, 8, 9],
    'left': [1, 4, 7],
    'center': [2, 5, 8],
    'right': [3, 6, 9],
    'slash down': [1, 5, 9],
    'slash up': [3, 5, 7],
}

for arg in sys.argv:
    if '=' in arg:
        var, val = arg.split('=')
        var = var.replace('-', '')
        argv[var] = val

argv['rounds'] = int(argv['rounds'])

player1 = importlib.import_module(argv['p1'])
player2 = importlib.import_module(argv['p2'])

def check_game_over(grid):
    for line_name, boxes in lines.items():
        val = grid[boxes[0]]
        if val != 0:
            hit = True
            for box in boxes:
                if grid[box] != val:
                    hit = False
                    break
            if hit:
                grid[0] = val

    tie = True
    for i in range(1, 10):
        if grid[i] == 0:
            tie = False
            break
    if tie:
        grid[0] = 3

def is_game_over(grid):
    return grid[0] != 0

def player_name(id):
    key = 'p{}'.format(id)
    return '{} {}'.format(id, argv.get(key, id))

def play_1_turn(grid, player, player_id):
    choice = player.play(list(grid), player_id)
    if choice > 0 and choice < 10 and grid[choice] == 0:
        grid[choice] = player_id
    else:
        choice = None
        grid[0] = 3 - player_id

    check_game_over(grid)
    return choice

def play_1_game(player1, player2):
    allmoves = []
    grid = [0] * 10
    players = {
        1: player1,
        2: player2,
    }
    iter = cycle(players.iteritems())
    while not is_game_over(grid):
        player_id, player = iter.next()
        choice = play_1_turn(grid, player, player_id)
        allmoves.append(choice)

    logfile.write(str(allmoves) + '\n')
    return players.get(grid[0], None)


with open('game.log', 'a') as logfile:
    logfile.write('\n{} vs {} @ {}\n'.format(
        player_name(1), player_name(2), datetime.now()))

    current_game = 1
    turn_order = [
        [player1, player2],
        [player2, player1],
    ]
    player_order = cycle(turn_order)
    results = {
        player1: 0,
        player2: 0,
        None: 0,
    }
    while current_game <= argv['rounds']:
        temp_p1, temp_p2 = player_order.next()
        winner = play_1_game(temp_p1, temp_p2)
        results[winner] += 1
        current_game += 1

    print player1.__name__, results.get(player1, 0)
    print player2.__name__, results.get(player2, 0)
    print 'tie', results.get(None, 0)
