# Tic-Tac-Toe


class Player:
    
    def __init__(self):
        self.name1 = player1
        self.name2 = player2
        self.token1 = 'X'
        self.token2 = 'O'


class Game:

    def __init__(self):
        
        self.board = {
            '0,0': ' ',
            '1,0': ' ',
            '2,0': ' ',
            '0,1': ' ',
            '1,1': ' ',
            '2,1': ' ',
            '0,2': ' ',
            '1,2': ' ',
            '2,2': ' '
        }

        self.count = 0

    def __repr__(self):
        print(f"{self.board['0,0']}|{self.board['1,0']}|{self.board['2,0']}\n- - -\n{self.board['0,1']}|{self.board['1,1']}|{self.board['2,1']}\n- - -\n{self.board['0,2']}|{self.board['1,2']}|{self.board['2,2']}")


    def move(self, x, y, player):
        play.move(2, 1, player1)
        self.count += 1

    def winner(self):
        # if statement?

    def is_full(self):
        if self.count == 9:
            print("The board is full. End of game.") 
        elif self.count != 9:
            pass

    def is_game_over(self):
        self.is_full()

play = Game()

def main():
    print("Let's play Tic-Tac-Toe!")
    play.__repr__()
    
    player1 = input("Enter the first player's name: ")
    print(f"{player1}, you are 'X'.")
    player2 = input("Enter the second player's name: ")
    print(f"{player2}, you are 'O'.")



main()


    
    
