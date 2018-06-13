# -*- coding: utf-8 -*-

def play(grid, player_id):
    while True:
        choice = raw_input('choose a box: ')
        try:
            choice = int(choice)
            return choice
        except Exception:
            print 'not a valid choice'
