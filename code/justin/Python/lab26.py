class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        


class Game:
    def __init__(self):
        pass

    def move(Player):
        pass
        
    def board():
        line0 = '  A B C'  #   MOVES        INDICES
        line1 = '1| | | |' # 10, 12, 14     8  - 15
        line2 = '2| | | |' # 19, 21, 23     17 - 24
        line3 = '3| | | |' # 28, 30, 32     26 - 33
        board = line0 + '\n' + line1 + '\n' + line2 + '\n' + line3 + '\n'
        print(board)

    def player_move(self, player, move):
        
        spaces = {
        a1: Game.board[10],
        a2: Game.board[19],
        a3: Game.board[28],
        b1: Game.board[12],
        b2: Game.board[21],
        b3: Game.board[30],
        c1: Game.board[14],
        c2: Game.board[23],
        c3: Game.board[32]
        }

        # winning combinations
        a1 + b1 + c1
        a2 + b2 + c2
        a3 + b3 + c3
        a1 + a2 + a3
        b1 + b2 + b3
        c1 + c2 + c3
        a1 + b2 + c3
        a3 + b2 + c1


# enter usernames
# assign X or O

# display board
# player makes move
# board changes
# new display board
#   etc.
# checks (row, column, diagonal) for wins (optionally at and after move 5)
#   declare winner if applicable
# ends when board is full



# REPL
def begin():
    
    player_1 = Player(input('First player name: '), 'X')
    print(f'{player_1.name} will be X.')
    player_2 = Player(input('Second player name: '), 'O')
    print(f'{player_2.name} will be O.')

    Game.board()



begin()