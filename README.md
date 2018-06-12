# HashWars

## Overview
Hash Wars is a simple host that will allow AI vs. AI, Player vs. AI, or Player vs. Player games of tic-tac-toe to be played via a command-line interface.

## How to Use
Run `./hashwars.py -p1=simple.py -p2=simple.py -rounds=1 -unrated=true` in a shell.
The default value for `p1` and `p2` is a human player. If you specify a python file, it will load the file and run the play function.
The default value for `rounds` is 1. If there is more than 1 round, the player who goes first will be rotated each round.
If `unrated` has a value of `true`, the result of the game will not be appended to `game.log`.

## How to Create AI
All AI must be created in python3 files. There must be a function with the name `play` that takes exactly one argument named `first` of type `bool`, like this `def play(first):`. This function must accept input from the command line and print a single character per line representing its own moves. The function should return after receiving an input of `0`, which the host will send when it has observed that the game is over.

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
