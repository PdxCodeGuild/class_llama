# Tic-Tac-Toe


class Player:
    # name = player name
    token = 'X' or 'O'


class Game:

    def __init__(self):
        
        self.board = {
            '0,0': '',
            '1,0': '',
            '2,0': '',
            '0,1': '',
            '1,1': '',
            '2,1': '',
            '0,2': '',
            '1,2': '',
            '2,2': ''
        }

    def __repr__(self):
        print(f"{self.board['0,0']}|{self.board['1,0']}|{self.board['2,0']}\n---\n{self.board['0,1']}|{self.board['1,1']}|{self.board['2,1']}\n---\n{self.board['0,2']}|{self.board['1,2']}|{self.board['2,2']}")


#     def move(x, y, player): 
#         # place a player's token character string at a given coordinate
#         # (top-left is 0, 0), x is horizontal position, y is vertical position
#         board.move(2, 1, player_1)

#     def cal_winner():
#         # what token character string has won or None if no one has
#         board.calc_winner()

#     def is_full():
#         # returns True if the game board is full
#         board.is_full()

#     def is_game_over():
#         # returns True if the game board is full or a player has won
#         board.is_game_over()

# def main():
#     while True:

    
    
