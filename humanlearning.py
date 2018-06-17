# -*- coding: utf-8 -*-

moves = {
    #"grid_state:str": response:int,
}

learning_file = open('humanlearning.db', 'a+')
learning_file.seek(0)
for line in learning_file.readlines():
    state, response = line.split('-')
    moves[state] = int(response)

def grid_state(grid):
    return ''.join(str(x) for x in grid[1:])

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
    state = grid_state(grid)
    if state in moves.keys():
        print 'auto-move {} {}'.format(' xo'[player_id], moves[state])
        return moves[state]

    print str_grid(grid)
    while True:
        choice = raw_input('choose a box {}: '.format(' xo'[player_id]))
        try:
            choice = int(choice)
            moves[state] = choice
            learning_file.write('{}-{}\n'.format(state, choice))
            return choice
        except Exception:
            print 'not a valid choice'
