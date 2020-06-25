# Tic-Tac-Toe


class Player:
    
    def __init__(self, token, name):
        self.name = name
        self.token = token


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

    def __repr__(self):
        return f"{self.board['0,0']}|{self.board['1,0']}|{self.board['2,0']}\n- - -\n{self.board['0,1']}|{self.board['1,1']}|{self.board['2,1']}\n- - -\n{self.board['0,2']}|{self.board['1,2']}|{self.board['2,2']}"


    def move(self, x, y, player):
        self.board[f'{x},{y}'] = player.token

    def winner(self):
        # if statement?
        pass

    def is_full(self):
        print("The board is full. End of game.") 

    def is_game_over(self):
        self.is_full()


play = Game()

def main():
    print("Let's play Tic-Tac-Toe!")
    
    player1_name = input("Enter the first player's name: ")
    print(f"{player1_name}, you are 'X'.")
    player2_name = input("Enter the second player's name: ")
    print(f"{player2_name}, you are 'O'.")

    count = 0

    while True:

        if count % 2 == 0:
            print(player1_name)
            
            x = input(f"{player1_name}, enter an 'x' horizontal value (0, 1, 2): ")
            y = input("Now enter a 'y' vertical value (0, 1, 2): ")
            
            player1 = Player('X', player1_name)
            play.move(x, y, player1)
            print(play.__repr__())

            count += 1

            if count == 9:
                play.is_full()
            else:
                pass

        elif count % 2 == 1:

            x = input(f"{player2_name}, enter an 'x' horizontal value (0, 1, 2): ")
            y = input("Now enter a 'y' vertical value (0, 1, 2): ")
            
            player2 = Player('O', player2_name)
            play.move(x, y, player2)
            print(play.__repr__())

            count += 1

    
    print(play)

    print(play.board)



main()


    
    
