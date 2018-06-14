# -*- coding: utf-8 -*-

import sys
import importlib
from datetime import datetime

if __file__ in sys.argv[0]:
    sys.argv = sys.argv[1:]

grid = [0] * 10

args = {
    'p1': 'human',
    'p2': 'human',
    'rounds': 1,
    'unrated': False,
}

printable = {
    0: ' ',
    1: 'x',
    2: 'o',
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
        args[var] = val


player1 = importlib.import_module(args['p1'])
player2 = importlib.import_module(args['p2'])

def game_is_over():
    for line_name, boxes in lines.items():
        val = grid[boxes[0]]
        if val != 0:
            hit = True
            for box in boxes:
                if grid[box] != val:
                    hit = False
                    break
            if hit:
                return (True, val, line_name)

    tie = True
    for i in range(1, 10):
        if grid[i] == 0:
            tie = False
            break
    if tie:
        return (True, 0, 'tie')

    return (False, grid[0], '(?)')

def str_grid():
    str = ' {} | {} | {} \n'.format(
        printable.get(grid[1], ' '),
        printable.get(grid[2], ' '),
        printable.get(grid[3], ' '))
    str = str + '---+---+---\n'
    str = str + ' {} | {} | {} \n'.format(
        printable.get(grid[4], ' '),
        printable.get(grid[5], ' '),
        printable.get(grid[6], ' '))
    str = str + '---+---+---\n'
    str = str + ' {} | {} | {} \n'.format(
        printable.get(grid[7], ' '),
        printable.get(grid[8], ' '),
        printable.get(grid[9], ' '))
    return str

def player_name(id):
    key = 'p{}'.format(id)
    return '{} {}'.format(id, args.get(key, id))

winner = 0
line = '(?)'
with open('game.log', 'a') as logfile:
    logfile.write('\n{} vs {} @ {}\n'.format(
        player_name(1), player_name(2), datetime.now()))
    allmoves = []
    while True:
        choice = player1.play(list(grid), 1)
        allmoves.append(choice)
        if choice > 0 and choice < 10 and grid[choice] == 0:
            grid[choice] = 1
        else:
            grid[0] = 2
            break

        print str_grid()

        over, winner, line = game_is_over()
        if over:
            break

        choice = player2.play(list(grid), 2)
        allmoves.append(choice)
        if choice > 0 and choice < 10 and grid[choice] == 0:
            grid[choice] = 2
        else:
            grid[0] = 1
            break

        print str_grid()

        over, winner, line = game_is_over()
        if over:
            break

    outcome = 'Player {} wins by {}\n'.format(player_name(winner), line)
    print outcome
    logfile.write(str(allmoves) + '\n')
    logfile.write(outcome)
    logfile.write(str_grid())
