# HashWars

## Overview
Hash Wars is a simple host that will allow AI vs. AI, Player vs. AI, or Player vs. Player games of tic-tac-toe to be played via a command-line interface.

## How to Use
Run `python hashwars.py -p1=simple -p2=brute` in a shell.
The default value for `p1` and `p2` is a human player. If you specify a python file, it will load the file and run the play function.

## How to Create AI
All AI must be created in python files (python 2.7 compatible). There must be a function with the name `play` that takes two argument named `grid` and `player_id`, like this `def play(grid, player_id):`. This function must return an integer representing its move.

## Technical Specs
The board is logically laid out in this way:
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```
The host will be responsible to print out the game state after each turn and keep records of all moves and Win/Loss/Tie results.
