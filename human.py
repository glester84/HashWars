# -*- coding: utf-8 -*-

def str_grid(grid):
    printable = ' xo'
    str = ' {} | {} | {} \n'.format(
        printable[grid[1]],
        printable[grid[2]],
        printable[grid[3]])
    str = str + '---+---+---\n'
    str = str + ' {} | {} | {} \n'.format(
        printable[grid[4]],
        printable[grid[5]],
        printable[grid[6]])
    str = str + '---+---+---\n'
    str = str + ' {} | {} | {} \n'.format(
        printable[grid[7]],
        printable[grid[8]],
        printable[grid[9]])
    return str

def play(grid, player_id):
    print str_grid(grid)
    while True:
        choice = raw_input('choose a box: ')
        try:
            choice = int(choice)
            return choice
        except Exception:
            print 'not a valid choice'
