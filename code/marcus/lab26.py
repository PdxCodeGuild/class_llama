class tic_tac_toe:

    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
        self.moves_count = 0

    def create_board(self):
        print()
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()


    def player1(self):
        print('Player X')
        player_move = int(input('Where would you like to go?: '))
        if self.board(player_move) != 'X' and self.board(player_move) != 'O':
            self.board(player_move) = 'X'
            self.create_board()
            self.moves_count += 1
        else:
            print('Someone already picked that spot')
            self.player1()
        self.check_win()

    def player2(self):
        print('Player O')
        player_move = int(input('Where would you like to go?: '))
        if self.board(player_move) != 'X' and self.board(player_move) != 'O':
            self.board(player_move) = 'O'
            self.create_board()
            self.moves_count += 1
        else:
            print('Someone already picked that spot')
            self.player2()
        self.check_win()


    def check_win(self):
        for a in self.win_conditions:
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == 'X':
                print('Player X wins!')
                self.play_again()
            if self.board[a[0]] == self.board[a[1]] == self.board[a[2]] == 'O':
                print('Player O wins!')
                self.play_again()
            elif self.moves_count == 9:
                print('Thats a draw if Ive ever seen one')
                exit()

    def sendit(self):
        while True:
            self.player1()
            self.player2()


    def fullsend(self):
        self.create_board()
        self.sendit()



    def senditagain(self):
        
    

    
