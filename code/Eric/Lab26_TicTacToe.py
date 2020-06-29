# Tic Tac Toe Game

import random

my_game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(game_grid, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_grid[row][column] = player
        for count, row in enumerate(game_grid):
            print(count, row)
        return game_grid
    except IndexError:
        print("You have played a row or column outside the range of 0,1 or 2!!! ")
        return False


my_game = game_board(my_game, player=1, row=3, column=1)





