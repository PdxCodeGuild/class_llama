# Tic-Tac-Toe


# class Player:
    
    # def __init__(self):
        # self.name1 = player1
        # self.name2 = player2
        # self.token1 = 'X'
        # self.token2 = 'O'


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

        count = 0

    def __repr__(self):
        print(f"{self.board['0,0']}|{self.board['1,0']}|{self.board['2,0']}\n- - -\n{self.board['0,1']}|{self.board['1,1']}|{self.board['2,1']}\n- - -\n{self.board['0,2']}|{self.board['1,2']}|{self.board['2,2']}")


#     def move(self, x, y, player): 
#         # place a player's token character string at a given coordinate
#         # (top-left is 0, 0), x is horizontal position, y is vertical position
#         play.move(2, 1, player_1)
            # count += 1

#     def cal_winner(self):
#         # what token character string has won or None if no one has
#         play.calc_winner()

#     def is_full(self):
#         # returns True if the game board is full
#         play.is_full()
        # print("The board is full. End of game.") 

#     def is_game_over(self):
#         # returns True if the game board is full or a player has won
#         play.is_game_over()

# player = Player()
play = Game()

def main():
    print("Let's play Tic-Tac-Toe!")
    play.__repr__()


main()


    
    
