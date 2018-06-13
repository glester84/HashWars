# -*- coding: utf-8 -*-

def play(grid, player_id):
    g = grid[1:]
    p = player_id
    t = 3 - p
    if player_id == 1:
        # first move
        if g == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
            return 1
        # third move
        elif g == [1, 2, 0, 0, 0, 0, 0, 0, 0]:
            return 5
        elif g == [1, 0, 2, 0, 0, 0, 0, 0, 0]:
            return 5
        elif g == [1, 0, 0, 2, 0, 0, 0, 0, 0]:
            return 5
        elif g == [1, 0, 0, 0, 2, 0, 0, 0, 0]:
            return 9
        elif g == [1, 0, 0, 0, 0, 2, 0, 0, 0]:
            return 5
        elif g == [1, 0, 0, 0, 0, 0, 2, 0, 0]:
            return 5
        elif g == [1, 0, 0, 0, 0, 0, 0, 2, 0]:
            return 5
        elif g == [1, 0, 0, 0, 0, 0, 0, 0, 2]:
            return 3
        # fifth move
        elif g == [1, 2, 2, 0, 1, 0, 0, 0, 0]:
            return 9 # win
        elif g == [1, 2, 0, 2, 1, 0, 0, 0, 0]:
            return 9 # win
        elif g == [1, 2, 0, 0, 1, 2, 0, 0, 0]:
            return 9 # win
        elif g == [1, 2, 0, 0, 1, 0, 2, 0, 0]:
            return 9 # win
        elif g == [1, 2, 0, 0, 1, 0, 0, 2, 0]:
            return 9 # win
        elif g == [1, 2, 0, 0, 1, 0, 0, 0, 2]:
            return 3
        elif g == [1, 0, 2, 2, 1, 0, 0, 0, 0]:
            return 9 # win
        elif g == [1, 0, 2, 0, 1, 2, 0, 0, 0]:
            return 9 # win
        elif g == [1, 0, 2, 0, 1, 0, 2, 0, 0]:
            return 9 # win
        elif g == [1, 0, 2, 0, 1, 0, 0, 2, 0]:
            return 9 # win
        elif g == [1, 0, 2, 0, 1, 0, 0, 0, 2]:
            return 6
        elif g == [1, 0, 0, 2, 1, 2, 0, 0, 0]:
            return 9 # win
        elif g == [1, 0, 0, 2, 1, 0, 2, 0, 0]:
            return 9 # win
        elif g == [1, 0, 0, 2, 1, 0, 0, 2, 0]:
            return 9 # win
        elif g == [1, 0, 0, 2, 1, 0, 0, 0, 2]:
            return 3
        elif g == [1, 2, 0, 0, 2, 0, 0, 0, 1]:
            return 8
        elif g == [1, 0, 2, 0, 2, 0, 0, 0, 1]:
            return 7
        elif g == [1, 0, 0, 2, 2, 0, 0, 0, 1]:
            return 6
        elif g == [1, 0, 0, 0, 2, 2, 0, 0, 1]:
            return 4
        elif g == [1, 0, 0, 0, 2, 0, 2, 0, 1]:
            return 3
        elif g == [1, 0, 0, 0, 2, 0, 0, 2, 1]:
            return 2
        elif g == [1, 0, 0, 0, 1, 2, 2, 0, 0]:
            return 9 # win
        elif g == [1, 0, 0, 0, 1, 2, 0, 2, 0]:
            return 9 # win
        elif g == [1, 0, 0, 0, 1, 2, 0, 0, 2]:
            return 3
        elif g == [1, 0, 0, 0, 1, 0, 2, 2, 0]:
            return 9 # win
        elif g == [1, 0, 0, 0, 1, 0, 2, 0, 2]:
            return 8
        elif g == [1, 0, 0, 0, 1, 0, 0, 2, 2]:
            return 7
        elif g == [1, 2, 1, 0, 0, 0, 0, 0, 2]:
            return 5
        elif g == [1, 0, 1, 2, 0, 0, 0, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 0, 2, 0, 0, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 0, 0, 2, 0, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 0, 0, 0, 2, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 0, 0, 0, 0, 2, 2]:
            return 2 # win
        # seventh move
        elif g == [1, 2, 1, 2, 1, 0, 0, 0, 2]:
            return 7 # win
        elif g == [1, 2, 1, 0, 1, 2, 0, 0, 2]:
            return 7 # win
        elif g == [1, 2, 1, 0, 1, 0, 2, 0, 2]:
            return 8
        elif g == [1, 2, 1, 0, 1, 0, 0, 2, 2]:
            return 7 # win
        elif g == [1, 2, 2, 0, 1, 1, 0, 0, 2]:
            return 4 # win
        elif g == [1, 0, 2, 2, 1, 1, 0, 0, 2]:
            return 8
        elif g == [1, 0, 2, 0, 1, 1, 2, 0, 2]:
            return 4 # win
        elif g == [1, 0, 2, 0, 1, 1, 0, 2, 2]:
            return 4 # win
        elif g == [1, 0, 1, 2, 1, 2, 0, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 2, 1, 0, 2, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 2, 1, 0, 0, 2, 2]:
            return 2 # win
        elif g == [1, 2, 2, 0, 2, 0, 0, 1, 1]:
            return 7 # win
        elif g == [1, 2, 0, 2, 2, 0, 0, 1, 1]:
            return 7 # win
        elif g == [1, 2, 0, 0, 2, 2, 0, 1, 1]:
            return 7 # win
        elif g == [1, 2, 0, 0, 2, 0, 2, 1, 1]:
            return 3
        elif g == [1, 2, 2, 0, 2, 0, 1, 0, 1]:
            return 8 # win
        elif g == [1, 0, 2, 2, 2, 0, 1, 0, 1]:
            return 8 # win
        elif g == [1, 0, 2, 0, 2, 2, 1, 0, 1]:
            return 8 # win
        elif g == [1, 0, 2, 0, 2, 0, 1, 2, 1]:
            return 2
        elif g == [1, 2, 0, 2, 2, 1, 0, 0, 1]:
            return 3 # win
        elif g == [1, 0, 2, 2, 2, 1, 0, 0, 1]:
            return 8
        elif g == [1, 0, 0, 2, 2, 1, 2, 0, 1]:
            return 3 # win
        elif g == [1, 0, 0, 2, 2, 1, 0, 2, 1]:
            return 3 # win
        elif g == [1, 2, 0, 1, 2, 2, 0, 0, 1]:
            return 7 # win
        elif g == [1, 0, 2, 1, 2, 2, 0, 0, 1]:
            return 7 # win
        elif g == [1, 0, 0, 1, 2, 2, 2, 0, 1]:
            return 3
        elif g == [1, 0, 0, 1, 2, 2, 0, 2, 1]:
            return 7 # win
        elif g == [1, 2, 1, 0, 2, 0, 2, 0, 1]:
            return 6 # win
        elif g == [1, 0, 1, 0, 2, 0, 2, 0, 1]:
            return 2 # win
        elif g == [1, 0, 1, 0, 2, 0, 2, 0, 1]:
            return 2 # win
        elif g == [1, 0, 1, 0, 2, 0, 2, 0, 1]:
            return 2 # win
        elif g == [1, 1, 2, 0, 2, 0, 0, 2, 1]:
            return 7
        elif g == [1, 1, 0, 2, 2, 0, 0, 2, 1]:
            return 3 # win
        elif g == [1, 1, 0, 0, 2, 2, 0, 2, 1]:
            return 3 # win
        elif g == [1, 1, 0, 0, 2, 0, 2, 2, 1]:
            return 3 # win
        elif g == [1, 2, 1, 0, 1, 2, 0, 0, 2]:
            return 7 # win
        elif g == [1, 0, 1, 2, 1, 2, 0, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 0, 1, 2, 2, 0, 2]:
            return 2 # win
        elif g == [1, 0, 1, 0, 1, 2, 0, 2, 2]:
            return 2 # win
        elif g == [1, 2, 0, 0, 1, 0, 2, 1, 2]:
            return 6
        elif g == [1, 0, 2, 0, 1, 0, 2, 1, 2]:
            return 2 # win
        elif g == [1, 0, 0, 2, 1, 0, 2, 1, 2]:
            return 2 # win
        elif g == [1, 0, 0, 0, 1, 2, 2, 1, 2]:
            return 2 # win
        elif g == [1, 2, 0, 0, 1, 0, 1, 2, 2]:
            return 3 # win
        elif g == [1, 0, 2, 0, 1, 0, 1, 2, 2]:
            return 6
        elif g == [1, 0, 0, 2, 1, 0, 1, 2, 2]:
            return 3 # win
        elif g == [1, 0, 0, 0, 1, 2, 1, 2, 2]:
            return 3 # win
        elif g == [1, 2, 1, 2, 1, 0, 0, 0, 2]:
            return 7 # win
        elif g == [1, 2, 1, 0, 1, 2, 0, 0, 2]:
            return 7 # win
        elif g == [1, 2, 1, 0, 1, 0, 2, 0, 2]:
            return 8
        elif g == [1, 2, 1, 0, 1, 0, 0, 2, 2]:
            return 7 # win
    else:
        # second move
        if g == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
            return 5
        elif g == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            return 5
        elif g == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
            return 5
        elif g == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
            return 5
        elif g == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            return 1
        elif g == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            return 5
        elif g == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
            return 5
        elif g == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
            return 5
        elif g == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
            return 5
        # fourth move
        elif g == [1, 1, 0, 0, 2, 0, 0, 0, 0]:
            return 3
        elif g == [1, 0, 1, 0, 2, 0, 0, 0, 0]:
            return 2
        elif g == [1, 0, 0, 1, 2, 0, 0, 0, 0]:
            return 7
        elif g == [1, 0, 0, 0, 2, 1, 0, 0, 0]:
            return 3
        elif g == [1, 0, 0, 0, 2, 0, 1, 0, 0]:
            return 4
        elif g == [1, 0, 0, 0, 2, 0, 0, 1, 0]:
            return 7
        elif g == [1, 0, 0, 0, 2, 0, 0, 0, 1]:
            return 2
        elif g == [0, 1, 1, 0, 2, 0, 0, 0, 0]:
            return 1
        elif g == [0, 1, 0, 1, 2, 0, 0, 0, 0]:
            return 1
        elif g == [0, 1, 0, 0, 2, 1, 0, 0, 0]:
            return 1
        elif g == [0, 1, 0, 0, 2, 0, 1, 0, 0]:
            return 1
        elif g == [0, 1, 0, 0, 2, 0, 0, 1, 0]:
            return 1
        elif g == [0, 1, 0, 0, 2, 0, 0, 0, 1]:
            return 1
        elif g == [0, 0, 1, 1, 2, 0, 0, 0, 0]:
            return 1
        elif g == [0, 0, 1, 0, 2, 1, 0, 0, 0]:
            return 9
        elif g == [0, 0, 1, 0, 2, 0, 1, 0, 0]:
            return 2
        elif g == [0, 0, 1, 0, 2, 0, 0, 1, 0]:
            return 1
        elif g == [0, 0, 1, 0, 2, 0, 0, 0, 1]:
            return 6
        elif g == [0, 0, 0, 1, 2, 1, 0, 0, 0]:
            return 1
        elif g == [0, 0, 0, 1, 2, 0, 1, 0, 0]:
            return 1
        elif g == [0, 0, 0, 1, 2, 0, 0, 1, 0]:
            return 1
        elif g == [0, 0, 0, 1, 2, 0, 0, 0, 1]:
            return 1
        elif g == [2, 1, 0, 0, 1, 0, 0, 0, 0]:
            return 8
        elif g == [2, 0, 1, 0, 1, 0, 0, 0, 0]:
            return 7
        elif g == [2, 0, 0, 1, 1, 0, 0, 0, 0]:
            return 6
        elif g == [2, 0, 0, 0, 1, 1, 0, 0, 0]:
            return 4
        elif g == [2, 0, 0, 0, 1, 0, 1, 0, 0]:
            return 3
        elif g == [2, 0, 0, 0, 1, 0, 0, 1, 0]:
            return 2
        elif g == [2, 0, 0, 0, 1, 0, 0, 0, 1]:
            return 3
        elif g == [0, 0, 0, 0, 2, 1, 1, 0, 0]:
            return 9
        elif g == [0, 0, 0, 0, 2, 1, 0, 1, 0]:
            return 9
        elif g == [0, 0, 0, 0, 2, 1, 0, 0, 1]:
            return 3
        elif g == [0, 0, 0, 0, 2, 0, 1, 1, 0]:
            return 9
        elif g == [0, 0, 0, 0, 2, 0, 1, 0, 1]:
            return 8
        elif g == [0, 0, 0, 0, 2, 0, 0, 1, 1]:
            return 7
        # sixth move
        elif g == [1, 1, 2, 1, 2, 0, 0, 0, 0]:
            return 7 # win
        elif g == [1, 1, 2, 0, 2, 1, 0, 0, 0]:
            return 7 # win
        elif g == [1, 1, 2, 0, 2, 0, 1, 0, 0]:
            return 4
        elif g == [1, 1, 2, 0, 2, 0, 0, 1, 0]:
            return 7 # win
        elif g == [1, 1, 2, 0, 2, 0, 0, 0, 1]:
            return 7 # win
        elif g == [1, 2, 1, 1, 2, 0, 0, 0, 0]:
            return 8 # win
        elif g == [1, 2, 1, 0, 2, 1, 0, 0, 0]:
            return 8 # win
        elif g == [1, 2, 1, 0, 2, 0, 1, 0, 0]:
            return 8 # win
        elif g == [1, 2, 1, 0, 2, 0, 0, 1, 0]:
            return 6 # cat
        elif g == [1, 2, 1, 0, 2, 0, 0, 0, 1]:
            return 8 # win
        elif g == [1, 1, 0, 1, 2, 0, 2, 0, 0]:
            return 3 # win
        elif g == [1, 0, 1, 1, 2, 0, 2, 0, 0]:
            return 2
        elif g == [1, 0, 0, 1, 2, 1, 2, 0, 0]:
            return 3 # win
        elif g == [1, 0, 0, 1, 2, 0, 2, 1, 0]:
            return 3 # win
        elif g == [1, 0, 0, 1, 2, 0, 2, 0, 1]:
            return 3 # win
        elif g == [1, 1, 2, 0, 2, 1, 0, 0, 0]:
            return 7 # win
        elif g == [1, 0, 2, 1, 2, 1, 0, 0, 0]:
            return 7 # win
        elif g == [1, 0, 2, 0, 2, 1, 1, 0, 0]:
            return 4
        elif g == [1, 0, 2, 0, 2, 1, 0, 1, 0]:
            return 7 # win
        elif g == [1, 0, 2, 0, 2, 1, 0, 0, 1]:
            return 7 # win
        elif g == [1, 1, 0, 2, 2, 0, 1, 0, 0]:
            return 6 # win
        elif g == [1, 0, 1, 2, 2, 0, 1, 0, 0]:
            return 6 # win
        elif g == [1, 0, 0, 2, 2, 1, 1, 0, 0]:
            return 9 # cat
        elif g == [1, 0, 0, 2, 2, 0, 1, 1, 0]:
            return 6 # win
        elif g == [1, 0, 0, 2, 2, 0, 1, 0, 1]:
            return 6 # win
        elif g == [1, 1, 0, 0, 2, 0, 2, 1, 0]:
            return 3 # win
        elif g == [1, 0, 1, 0, 2, 0, 2, 1, 0]:
            return 2
        elif g == [1, 0, 0, 1, 2, 0, 2, 1, 0]:
            return 3 # win
        elif g == [1, 0, 0, 0, 2, 1, 2, 1, 0]:
            return 3 # win
        elif g == [1, 0, 0, 0, 2, 0, 2, 1, 1]:
            return 3 # win
        elif g == [1, 2, 1, 0, 2, 0, 0, 0, 1]:
            return 8 # win
        elif g == [1, 2, 0, 1, 2, 0, 0, 0, 1]:
            return 8 # win
        elif g == [1, 2, 0, 0, 2, 1, 0, 0, 1]:
            return 8 # win
        elif g == [1, 2, 0, 0, 2, 0, 1, 0, 1]:
            return 8 # win
        elif g == [1, 2, 0, 0, 2, 0, 0, 1, 1]:
            return 7
        elif g == [2, 1, 1, 1, 2, 0, 0, 0, 0]:
            return 9 # win
        elif g == [2, 1, 1, 0, 2, 1, 0, 0, 0]:
            return 9 # win
        elif g == [2, 1, 1, 0, 2, 0, 1, 0, 0]:
            return 9 # win
        elif g == [2, 1, 1, 0, 2, 0, 0, 1, 0]:
            return 9 # win
        elif g == [2, 1, 1, 0, 2, 0, 0, 0, 1]:
            return 6
        elif g == [2, 1, 0, 1, 2, 1, 0, 0, 0]:
            return 9 # win
        elif g == [2, 1, 0, 1, 2, 0, 1, 0, 0]:
            return 9 # win
        elif g == [2, 1, 0, 1, 2, 0, 0, 1, 0]:
            return 9 # win
        elif g == [2, 1, 0, 1, 2, 0, 0, 0, 1]:
            return 7 # cat
        elif g == [2, 1, 1, 0, 2, 1, 0, 0, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 1, 1, 0, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 1, 0, 1, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 1, 0, 0, 1]:
            return 3
        elif g == [2, 1, 1, 0, 2, 0, 1, 0, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 1, 1, 0, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 0, 1, 1, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 0, 1, 0, 1]:
            return 8
        elif g == [2, 1, 0, 0, 2, 1, 0, 1, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 0, 1, 1, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 0, 0, 1, 1]:
            return 7
        elif g == [2, 1, 0, 0, 2, 1, 0, 1, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 0, 1, 1, 0]:
            return 9 # win
        elif g == [2, 1, 0, 0, 2, 0, 0, 1, 1]:
            return 7
        elif g == [2, 0, 1, 1, 2, 1, 0, 0, 0]:
            return 9 # win
        elif g == [2, 0, 1, 1, 2, 0, 1, 0, 0]:
            return 9 # win
        elif g == [2, 0, 1, 1, 2, 0, 0, 1, 0]:
            return 9 # win
        elif g == [2, 0, 1, 1, 2, 0, 0, 0, 1]:
            return 6
        elif g == [1, 0, 1, 0, 2, 1, 0, 0, 2]:
            return 2
        elif g == [0, 1, 1, 0, 2, 1, 0, 0, 2]:
            return 1 # win
        elif g == [0, 0, 1, 1, 2, 1, 0, 0, 2]:
            return 1 # win
        elif g == [0, 0, 1, 0, 2, 1, 1, 0, 2]:
            return 1 # win
        elif g == [0, 0, 1, 0, 2, 1, 0, 1, 2]:
            return 1 # win
        elif g == [1, 2, 1, 0, 2, 0, 1, 0, 0]:
            return 8 # win
        elif g == [0, 2, 1, 1, 2, 0, 1, 0, 0]:
            return 8 # win
        elif g == [0, 2, 1, 0, 2, 1, 1, 0, 0]:
            return 8 # win
        elif g == [0, 2, 1, 0, 2, 0, 1, 1, 0]:
            return 9
        elif g == [0, 2, 1, 0, 2, 0, 1, 0, 1]:
            return 8 # win
        elif g == [2, 0, 1, 0, 2, 1, 0, 1, 0]:
            return 9 # win
        elif g == [2, 0, 1, 0, 2, 0, 1, 1, 0]:
            return 9 # win
        elif g == [2, 0, 1, 0, 2, 0, 0, 1, 1]:
            return 7
        elif g == [1, 0, 1, 0, 2, 2, 0, 0, 1]:
            return 4 # win
        elif g == [0, 1, 1, 0, 2, 2, 0, 0, 1]:
            return 4 # win
        elif g == [0, 0, 1, 1, 2, 2, 0, 0, 1]:
            return 8 # cat
        elif g == [0, 0, 1, 0, 2, 2, 1, 0, 1]:
            return 4 # win
        elif g == [0, 0, 1, 0, 2, 2, 0, 1, 1]:
            return 4 # win
        elif g == [2, 0, 0, 1, 2, 1, 1, 0, 0]:
            return 9 # win
        elif g == [2, 0, 0, 1, 2, 1, 0, 1, 0]:
            return 9 # win
        elif g == [2, 0, 0, 1, 2, 1, 0, 0, 1]:
            return 3
        elif g == [2, 0, 0, 1, 2, 0, 1, 1, 0]:
            return 9 # win
        elif g == [2, 0, 0, 1, 2, 0, 1, 0, 1]:
            return 8
        elif g == [2, 0, 0, 1, 2, 0, 0, 1, 1]:
            return 7
        elif g == [2, 1, 1, 0, 1, 0, 0, 2, 0]:
            return 7
        elif g == [2, 1, 0, 1, 1, 0, 0, 2, 0]:
            return 6
        elif g == [2, 1, 0, 0, 1, 1, 0, 2, 0]:
            return 4
        elif g == [2, 1, 0, 0, 1, 0, 1, 2, 0]:
            return 3
        elif g == [2, 1, 0, 0, 1, 0, 0, 2, 1]:
            return 6
        elif g == [2, 1, 1, 0, 1, 0, 2, 0, 0]:
            return 4 # win
        elif g == [2, 0, 1, 1, 1, 0, 2, 0, 0]:
            return 6
        elif g == [2, 0, 1, 0, 1, 1, 2, 0, 0]:
            return 4 # win
        elif g == [2, 0, 1, 0, 1, 0, 2, 1, 0]:
            return 4 # win
        elif g == [2, 0, 1, 0, 1, 0, 2, 0, 1]:
            return 4 # win
        elif g == [2, 1, 0, 1, 1, 2, 0, 0, 0]:
            return 8
        elif g == [2, 0, 1, 1, 1, 2, 0, 0, 0]:
            return 7
        elif g == [2, 0, 0, 1, 1, 2, 1, 0, 0]:
            return 3
        elif g == [2, 0, 0, 1, 1, 2, 0, 1, 0]:
            return 2
        elif g == [2, 0, 0, 1, 1, 2, 0, 0, 1]:
            return 8
        elif g == [2, 1, 0, 2, 1, 1, 0, 0, 0]:
            return 7 # win
        elif g == [2, 0, 1, 2, 1, 1, 0, 0, 0]:
            return 7 # win
        elif g == [2, 0, 0, 2, 1, 1, 1, 0, 0]:
            return 3
        elif g == [2, 0, 0, 2, 1, 1, 0, 1, 0]:
            return 7 # win
        elif g == [2, 0, 0, 2, 1, 1, 0, 0, 1]:
            return 7 # win
        elif g == [2, 1, 2, 0, 1, 0, 1, 0, 0]:
            return 8
        elif g == [2, 0, 2, 1, 1, 0, 1, 0, 0]:
            return 2 # win
        elif g == [2, 0, 2, 0, 1, 1, 1, 0, 0]:
            return 2 # win
        elif g == [2, 0, 2, 0, 1, 0, 1, 1, 0]:
            return 2 # win
        elif g == [2, 0, 2, 0, 1, 0, 1, 0, 1]:
            return 2 # win
        elif g == [2, 2, 1, 0, 1, 0, 0, 1, 0]:
            return 7
        elif g == [2, 2, 0, 1, 1, 0, 0, 1, 0]:
            return 3 # win
        elif g == [2, 2, 0, 0, 1, 1, 0, 1, 0]:
            return 3 # win
        elif g == [2, 2, 0, 0, 1, 0, 1, 1, 0]:
            return 3 # win
        elif g == [2, 2, 0, 0, 1, 0, 0, 1, 1]:
            return 3 # win
        elif g == [2, 1, 2, 0, 1, 0, 0, 0, 1]:
            return 8
        elif g == [2, 0, 2, 1, 1, 0, 0, 0, 1]:
            return 2 # win
        elif g == [2, 0, 2, 0, 1, 1, 0, 0, 1]:
            return 2 # win
        elif g == [2, 0, 2, 0, 1, 0, 1, 0, 1]:
            return 2 # win
        elif g == [2, 0, 2, 0, 1, 0, 0, 1, 1]:
            return 2 # win
        elif g == [1, 0, 0, 0, 2, 1, 1, 0, 2]:
            return 4
        elif g == [0, 1, 0, 0, 2, 1, 1, 0, 2]:
            return 1 # win
        elif g == [0, 0, 1, 0, 2, 1, 1, 0, 2]:
            return 1 # win
        elif g == [0, 0, 0, 1, 2, 1, 1, 0, 2]:
            return 1 # win
        elif g == [0, 0, 0, 0, 2, 1, 1, 1, 2]:
            return 1 # win
        elif g == [1, 0, 0, 0, 2, 1, 0, 1, 2]:
            return 7 # cat
        elif g == [0, 1, 0, 0, 2, 1, 0, 1, 2]:
            return 1 # win
        elif g == [0, 0, 1, 0, 2, 1, 0, 1, 2]:
            return 1 # win
        elif g == [0, 0, 0, 1, 2, 1, 0, 1, 2]:
            return 1 # win
        elif g == [1, 0, 2, 0, 2, 1, 0, 0, 1]:
            return 7 # win
        elif g == [0, 1, 2, 0, 2, 1, 0, 0, 1]:
            return 7 # win
        elif g == [0, 0, 2, 1, 2, 1, 0, 0, 1]:
            return 7 # win
        elif g == [0, 0, 2, 0, 2, 1, 1, 0, 1]:
            return 8
        elif g == [0, 0, 2, 0, 2, 1, 0, 1, 1]:
            return 7 # win
        elif g == [1, 0, 0, 0, 2, 0, 1, 1, 2]:
            return 4
        elif g == [0, 1, 0, 0, 2, 0, 1, 1, 2]:
            return 1 # win
        elif g == [0, 0, 1, 0, 2, 0, 1, 1, 2]:
            return 1 # win
        elif g == [0, 0, 0, 1, 2, 0, 1, 1, 2]:
            return 1 # win
        elif g == [1, 0, 0, 0, 2, 0, 1, 2, 1]:
            return 2 # win
        elif g == [0, 1, 0, 0, 2, 0, 1, 2, 1]:
            return 3 # cat
        elif g == [0, 0, 1, 0, 2, 0, 1, 2, 1]:
            return 2 # win
        elif g == [0, 0, 0, 1, 2, 0, 1, 2, 1]:
            return 2 # win
        elif g == [0, 0, 0, 0, 2, 1, 1, 2, 1]:
            return 2 # win
        elif g == [1, 0, 0, 0, 2, 0, 2, 1, 1]:
            return 3 # win
        elif g == [0, 1, 0, 0, 2, 0, 2, 1, 1]:
            return 3 # win
        elif g == [0, 0, 1, 0, 2, 0, 2, 1, 1]:
            return 6
        elif g == [0, 0, 0, 1, 2, 0, 2, 1, 1]:
            return 3 # win
        elif g == [0, 0, 0, 0, 2, 1, 2, 1, 1]:
            return 3 # win

    for i in range(1, 10):
        if grid[i] == 0:
            return i
    return 9
