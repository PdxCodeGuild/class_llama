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

        self.count = 0

    def __repr__(self):
        return f"{self.board['0,0']}|{self.board['1,0']}|{self.board['2,0']}\n- - -\n{self.board['0,1']}|{self.board['1,1']}|{self.board['2,1']}\n- - -\n{self.board['0,2']}|{self.board['1,2']}|{self.board['2,2']}"

    def move(self, x, y, player):
        self.board[f'{x},{y}'] = player.token

    def winner(self, player):
        if self.count >= 5:
            if self.board['0,0'] == self.board['1,0'] == self.board['2,0']:
                print(f"You win!")
                self.is_game_over()
                return True
            elif self.board['0,1'] == self.board['1,1'] == self.board['2,1']:
                print("You win!")
                self.is_game_over()
                return True
            elif self.board['0,2'] == self.board['1,2'] == self.board['2,2']:
                print("You win!")
                self.is_game_over()
                return True
            elif self.board['0,0'] == self.board['0,1'] == self.board['0,2']:
                print("You win!")
                self.is_game_over()
                return True
            elif self.board['1,0'] == self.board['1,1'] == self.board['1,2']:
                print("You win!")
                self.is_game_over()
                return True
            elif self.board['2,0'] == self.board['2,1'] == self.board['2,2']:
                print("You win!")
                self.is_game_over()
                return True
            elif self.board['0,0'] == self.board['1,1'] == self.board['2,2']:
                print("You win!")
                self.is_game_over()
                return True
            elif self.board['0,2'] == self.board['1,1'] == self.board['2,0']:
                print("You win!")
                self.is_game_over()
                return True
            else:
                pass
                
    def is_full(self):
        print("The board is full. End of game.")

    def is_game_over(self):
        print("End of game.")


play = Game()

def main():
    print("Let's play Tic-Tac-Toe!")
    
    player1_name = input("Enter the first player's name: ")
    print(f"{player1_name}, you are 'X'.")
    player2_name = input("Enter the second player's name: ")
    print(f"{player2_name}, you are 'O'.")

    while True:

        if play.count % 2 == 0:
            print(player1_name)
            
            x = input(f"{player1_name}, enter an 'x' horizontal value (0, 1, 2): ")
            y = input("Now enter a 'y' vertical value (0, 1, 2): ")
            
            player1 = Player('X', player1_name)
            play.move(x, y, player1)
            print(play.__repr__())

            play.count += 1

            if play.winner(player1):
                print("See ya.")
                play_again = input("Would you like to play again (Y/N): ")
                if play_again in ['Y','y','yes']:
                    main()
                elif play_again in ['N','n','no']:
                    print("Exiting.")
                    break

            if play.count == 9:
                play.is_full()
                play_again = input("Would you like to play again (Y/N): ")
                if play_again in ['Y','y','yes']:
                    main()
                elif play_again in ['N','n','no']:
                    print("Exiting.")
                    break
            else:
                pass

        elif play.count % 2 == 1:

            x = input(f"{player2_name}, enter an 'x' horizontal value (0, 1, 2): ")
            y = input("Now enter a 'y' vertical value (0, 1, 2): ")
            
            player2 = Player('O', player2_name)
            play.move(x, y, player2)
            print(play.__repr__())

            play.count += 1

            play.winner(player2)


main()


    
    
