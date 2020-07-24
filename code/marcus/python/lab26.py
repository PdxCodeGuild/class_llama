class tic_tac_toe:
    # sets the ground work for the game board and the win conditions
    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))
        self.moves_count = 0
    # sets the layout for the actual board
    def create_board(self):
        print()
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])
        print()


    def player1(self):
    # this sets the rules for player x and how they move
        try:
            print('Player X')
            player_move = int(input('Where would you like to go?: '))
            # this part makes sure a player doesn't select an already occupied space
            if self.board(player_move) != 'X' and self.board(player_move) != 'O':
                self.board(player_move) == 'X'
                self.create_board()
                self.moves_count += 1
            else:
                print('Someone already picked that spot')
                self.player1(board)
            self.check_win()
        except ValueError:
            print('Select a valid option')
            self.player1()


    def player2(self):
    # this sets the rules for player o and how they move
        try:
            print('Player O')
            player_move1 = int(input('Where would you like to go?: '))
            if self.board(player_move) != 'X' and self.board(player_move) != 'O':
                self.board(player_move) == 'O'
                self.create_board()
                self.moves_count += 1
            else:
                print('Someone already picked that spot')
                self.player2()
            self.check_win()
        except ValueError:
            print('Select a valid option')
            self.player2()

    # this function houses the win conditions and the move counter in case there is a tie
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
    # function designed to keep the players in turn until win conditions are met
    def sendit(self):
        while True:
            self.player1()
            self.player2()

    # function that starts the game
    def fullsend(self):
        self.create_board()
        self.sendit()


    # function toplay the game again
    def senditagain(self):
        user_quest = input('Play again?y/n: ')
        if user_quest == 'y':
            self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.sendit()
        elif user_quest == 'n':
            print('Alright, fine then. Bye Felicia')
            quit()

yo_boy_were_about_to_do_this_thang = tic_tac_toe()
yo_boy_were_about_to_do_this_thang.fullsend()
    