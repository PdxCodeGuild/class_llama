# create game board
board = [[0,0,0],
		 [0,0,0],
		 [0,0,0],]

# func that prints game_board
def game_board(player=0, row=0, column=0, just_display=False):
	print("   a  b  c")

	if not just_display:
		board[row][column] = player
	for count, row in enumerate(board):
		print(count, row)

game_board(just_display=True)
game_board(player=1, row=2, column=1)
# board[0][1] = 1
# game_board()






'''##--------------------- Method 1: counter --------------------##
# create header (y) coordinates
print("   0  1  2")

# initialize count (x) coordinates 
count = 0
for row in board:
	print(count, row)
	count += 1


## -------------------- Method 2: enumerate ------------------##
# create header (y) coordinates
print("   a  b  c")

for count, row in enumerate(board):
	print(count, row)'''