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
#token = 'X' or 'O'

class Player(): 
    def __init__(self, name, token):
        self.name = name
        self.token = token 

class Game():
    def __init__(self):
        self.board = {"0,0": " " , "0,1": " " , "0,2": " " , 
        "0,3": " " , "0,4": " " , "0,5" : " " ,
        "0,6": " " , "0,7": " " , "0,8": " "}
    def __repr__(self): 
        return f'{self.board["0,0"]}|{self.board["0,1"]}|{self.board["0,2"]} \n{self.board["0,3"]}|{self.board["0,4"]}|{self.board["0,5"]} \n{self.board["0,6"]}|{self.board["0,7"]}|{self.board["0,8"]}'
        
    def move(self, x, o, player):
        if self.board[f'{x},{o}'] == " ":
            self.board[f'{x},{o}'] = player.token
        return player.token

        
    def calcwinner(self):
        #write all winning conditions  ?
        if self.board["0,0"] == self.board["0,1"] == self.board["0,2"] != ' ': 
            return True 
        
        elif self.board["0,3"] == self.board["0,4"] == self.board["0,5"] != ' ':
            return True 

        elif self.board["0,6"] == self.board["0,7"] == self.board["0,8"] != ' ':
            return True 

        elif self.board["0,0"] == self.board["0,3"] == self.board["0,6"] != ' ':
            return True 

        elif self.board["0,1"] == self.board["0,4"] == self.board["0,7"] != ' ':
            return True 

        elif self.board["0,2"] == self.board["0,5"] == self.board["0,8"] != ' ':
            return True 

        elif self.board["0,0"] == self.board["0,4"] == self.board["0,8"] != ' ':
            return True 

        elif self.board["0,2"] == self.board["0,4"] == self.board["0,6"] != ' ':
            return True 
        else: 
            return False

        
    def is_full(self):
        # need to check if the board spaces are empty
         # checks to see if there is not a empty space, will return True if the board is full
        if " " not in list(self.board.values()): 
            return True 
        else:
            return False
            
        
    def game_over(self):
        # check if there is a winner; hint: function already made 
        if self.calcwinner() == True: 
            return True
        elif self.is_full() == True:
            return True
        else:
            return False
    
 
#play game 
#first ask for players
#while True:

def main(): 
    game_on = Game()
    input("Welcome to Tic-Tac-Toe. Let's play!")
    user1 = input("What is your name 'x': ")
    user2 = input("What is your name 'o': ")
    
    count = 0
    
    while True:
        if count % 2 == 0:

            x = input("Choose a position {x,o): ")
            o = input("Choose a position {x,o): ")
            player1 = Player(user1, 'x')
            #player2 = Player(user2, 'o')
            game_on.move(x,o, player1)
            print(game_on.__repr__())
            count += 1 
            # check to see if space is available for move, place piece if is, or return that space unavailable and try again
            # check to see if there is a winner, if there a winner quit game, if board full and no winner return "draw", if moves to make keep playing
            if game_on.calcwinner(): 
                print(f'{user1} won!')
                again = input("Play again, Y or N?")
                if again == "N": 
                    break
                else:
                    main()
                break
            
            if count == 9: 
                if game_on.is_full():
                    print("It's a draw")
                    again = input("Play again, Y or N?")
                    if again == "N":
                        break
                    else: 
                        main()

                        
                    

                     
        elif count % 2 == 1: 

            x = input("Choose a position {x,o): ")
            o = input("Choose a position {x,o): ")
            player2 = Player(user2, 'o')
            game_on.move(x,o, player2)
            print(game_on.__repr__())
            count += 1
            if game_on.calcwinner():
                print(f'{user2} won!')
                again = input("Play again, Y or N?")
                if again == "N": 
                    break
                else:
                    main()
                break
            if count == 9: 
                if game_on.is_full():
                    print("It's a draw")
                    again = input("Play again, Y or N?")
                    if again == "N": 
                        break
                    else:
                        main()

        
                    

            # check to see if space is available for move, place piece if is, or return that space unavailable and try again
            # check to see if there is a winner, or not 

        

       
        









if __name__ == "__main__":
    main()




   


