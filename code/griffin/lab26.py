class Player:

    def __init__(self,name,token):
        self.name = name
        self.token = token


class Game:

    def __init__(self):
        self.board = {(0,0):" ", (0,1):" ", (0,2):" ", (1,0):" ", (1,1):" ", (1,2):" ",(2,0):" ",(2,1):" ",(2,2):" "}
    
    def __repr__(self):
        return f'''{self.board[(0,0)]}|{self.board[(0,1)]}|{self.board[(0,2)]}
{self.board[(1,0)]}|{self.board[(1,1)]}|{self.board[(1,2)]}
{self.board[(2,0)]}|{self.board[(2,1)]}|{self.board[(2,2)]}'''

    def move(self,x,y,player):
        for n in self.board:
            if n == (x,y):
                self.board[n] = player.token

    def calc_winner(self,player1,player2):
        winner = ''
        players = [player1,player2]
        for player in players:
            if player.token == self.board[0,0] == self.board[0,1] == self.board[0,2]:
                winner = player
            elif player.token == self.board[1,0] == self.board[1,1] == self.board[1,2]:
                winner = player
            elif player.token == self.board[2,0] == self.board[2,1] == self.board[3,2]:
                winner = player
            elif player.token == self.board[0,0] == self.board[1,0] == self.board[1,0]:
                winner = player
            elif player.token == self.board[0,1] == self.board[1,1] == self.board[2,1]:
                winner = player
            elif player.token == self.board[2,0] == self.board[2,1] == self.board[2,2]:
                winner = player
            elif player.token == self.board[0,0] == self.board[0,1] == self.board[0,2]:
                winner = player
            elif player.token == self.board[0,0] == self.board[1,1] == self.board[2,2]:
                winner = player
            elif player.token == self.board[0,2] == self.board[1,1] == self.board[2,0]:
                winner = player
        return winner
            


player1 = Player('Glar','X')
player2 = Player('Blar','O')
test = Game()
test.move(0,1,player1)
test.move(0,0,player1)
test.move(0,2,player1)
print(repr(test))
winner = test.calc_winner(player1,player2)
print(f'{winner.name} is the winner')