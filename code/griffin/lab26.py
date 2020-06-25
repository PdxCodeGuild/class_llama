class Player:

    def __init__(self,name,token):
        self.name = name
        self.token = token


class Game:

    def __init__(self):
        self.board = {(0,0):" ", (0,1):" ", (0,2):" ", (1,0):" ", (1,1):" ", (1,2):" ",(2,0):" ",(2,1):" ",(2,2):" "}
    
    def __repr__(self):
        return f'''{self.board[(0,0)]}|{self.board[(1,0)]}|{self.board[(2,0)]}
{self.board[(0,1)]}|{self.board[(1,1)]}|{self.board[(2,1)]}
{self.board[(0,2)]}|{self.board[(1,2)]}|{self.board[(2,2)]}'''

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
            elif player.token == self.board[2,0] == self.board[2,1] == self.board[2,2]:
                winner = player
            elif player.token == self.board[0,0] == self.board[1,0] == self.board[2,0]:
                winner = player
            elif player.token == self.board[0,1] == self.board[1,1] == self.board[2,1]:
                winner = player
            elif player.token == self.board[2,0] == self.board[2,1] == self.board[2,2]:
                winner = player
            elif player.token == self.board[0,0] == self.board[1,1] == self.board[2,2]:
                winner = player
            elif player.token == self.board[0,2] == self.board[1,1] == self.board[2,0]:
                winner = player
        return winner

    def is_full(self):
        blank_counter = 0
        for n in self.board:   
            if self.board[n] == " ":
                blank_counter += 1
        if blank_counter == 0:
            return True
        else:
            return False

    def is_game_over(self,player1,player2):
        winner = self.calc_winner(player1,player2)
        full = self.is_full()
        if full == True:
            print("is full")
            return True
        elif winner != '':
            print(f"we have a winner: {winner.name}")
            return True
        else:
            print("keep going")
            return False


def main():
    tictactoe = Game()
    player_x_name = input('What is the name of player X? ')
    player_x = Player(player_x_name,'X')
    player_o_name = input('What is the name of player O? ')
    player_o = Player(player_o_name, 'O')
    player_list = [player_x,player_o]

    game = True
    while game:
        for player in player_list:
            coordinates = input(f"{player.name}, please input the coordinates where you'd like to place your token: ")
            string_list = coordinates.split(',')
            num_list = []
            for item in string_list:
                num_list.append(int(item))
            tictactoe.move(x = num_list[0],y = num_list[1],player = player)
            print(repr(tictactoe))

            winner = tictactoe.calc_winner(player_x,player_o)
            
            game_over = tictactoe.is_game_over(player_x,player_o)
            print(game_over)
            if game_over == True:
                game = False
                break
    if winner == "":
        print("it was a tie")
    else:
        print(f"the winner is {winner.name}")

main()


"""player1 = Player('Glar','X')
player2 = Player('Blar','O')
test = Game()

test.move(0,1,player1)
test.move(0,0,player1)
test.move(0,2,player1)
test.move(1,0,player2)
test.move(1,1,player1)
test.move(1,2,player1)
test.move(2,0,player1)
test.move(2,1,player1)
test.move(2,2,player1)
print(repr(test))

x = test.is_full()
print(f'board full? {x}')

y = test.is_game_over()
print(f'game over? {y}')

winner = test.calc_winner(player1,player2)
print(f'{winner.name} is the winner')"""