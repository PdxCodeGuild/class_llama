"""
This program allows the user to play a tic tac toe game.
Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid.
Whoever gets three in a row first wins.
"""

from os import system, name
from time import sleep

## create helper functions

# func that performs clear screen in terminal
def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('clear')
    # for unix
    else:
        _ = system('clear')

# func for ellipsis with pause to simulate computer thinking in terminal
def ellipsis(time=1):
    for i in range(3):
        print("... ")
        sleep(time)
    print()
    


# create class Player
class Player:
    # initialize
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def player(self):
        pass


# create class Player
class Game:

    def __init__(self):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' '],]

        self.board = board

    # define how board will be displayed using fstrings
    def __repr__(self):
        clear_screen()
        print("**************************")
        print("       TIC TACT TOE       ")
        print("**************************")
        print(f"        0    1    2")
        print()
        print(f"  0    {self.board[0][0]}  |  {self.board[0][1]}  | {self.board[0][2]} ")
        print(f"      ----|-----|---- ")
        print(f"  1    {self.board[1][0]}  |  {self.board[1][1]}  | {self.board[1][2]} ")
        print(f"      ----|-----|---- ")
        print(f"  2    {self.board[2][0]}  |  {self.board[2][1]}  | {self.board[2][2]} ")
        print()
        print()

    

    def move(self, x, y, player): # Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
        self.x = x
        self.y = y
        self.player = player



    def calc_winner(self): # what token character string has won or None if no one has.
        pass

    def is_full(self): # returns True if game board full
        pass

    def is_game_over(self): # returns true if the game board is full or a player has won.
        pass


# board = Game()
# board.__repr__()


## main function
if __name__ == "__main__":

    # show board at start of game
    board = Game()
    board.__repr__()

    # while loop for REPL
    while True:

        #prompt for users to choose X's or O's
        try:
            player_1_name = input("What is your name player 1: ")
            print(f"Hello, {player_1_name}")
            ellipsis()
            player_2_name = input("What is your name player 2: ")
            print(f"Hello, {player_2_name}")
            ellipsis()
            print(f"The battle for supreme ruler between {player_2_name} and {player_1_name} will now begin!")
            break
        
        except ValueError:
            print("Sorry, you entered something other than a name ")

        