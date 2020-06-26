''' 
lab 26: tic tac toe

Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. 
Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a function main that 
models gameplay taking in user inputs through REPL.

The Player class has the following properties:

name = player name
token = 'X' or 'O'
The Game class has the following properties:

board = your representation of the board
You can represent the board however you like, such as a 2D list, tuples, or dictionary.

The Game class has the following methods:

__repr__() Returns a pretty string representation of the game board

'''
#winning_combos = {}
#name = player 
token = 'X' or 'O'

class Game():
    def __init__(self):
        self.board = {"0,0": " " , "0,1": " " , "0,2": " " , 
        "0,3": " " , "0,4": " " , "0,5" : " " ,
        "0,6": " " , "0,7": " " , "0,8": " "}
    def __repr__(self): 
        return f'{self.board["0,0"]}|{self.board["0,1"]}|{self.board["0,2"]} \n{self.board["0,3"]}|{self.board["0,4"]}|{self.board["0,5"]} \n{self.board["0,6"]}|{self.board["0,7"]}|{self.board["0,8"]}
        print(board)
    def move(x, y, player):

    def calcwinner():
        if board = 

    def is_full():
        if board.isfull()
        return true

    def game_over():
        if board.game_over()
        return True
        elif board.game_over()
        return False 



class player(): 
    def __init__(self, name, token):
        self.name = name
        self.token = token 
    
#game1 = Game()
#print(game1)
def 

def main(): 
   














if __name__ == "__main__":
    pass




   


