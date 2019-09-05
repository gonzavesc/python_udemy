def print_board(board):
	print("   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   \n-----------\n   |   |   \n {} | {} | {} \n   |   |   ".format(board[6], board[7], board[8], board[3], board[4], board[5], board[0], board[1],board[2]))
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def check_game(board):
	horizontal = board[6]==board[7]==board[8]!=' ' or board[3]==board[4]==board[5]!=' '  or board[0]==board[1]==board[2]!=' ' 
	vertical = board[0]==board[3]==board[6]!=' '  or board[1]==board[4]==board[7]!=' '  or board[2]==board[5]==board[8]!=' ' 
	diagonal = board[0]==board[4]==board[8]!=' '  or board[6]==board[4]==board[2]!=' ' 
	return horizontal or vertical or diagonal
cont = True
choose = True
while choose:
	player_1 = input("Player 1 choose 'X' or 'O' ")
	if player_1 not in 'XO' or player_1=='':
		print("Choose 'X' or 'O' ")
	else:
		break
if player_1 == 'X':
	player_2 = 'O'
else:
	player_2 = 'X'
cont = True
myset = set()
turn_1 = True
while cont and len(myset)<9:
	if turn_1:
		good = False
		while not good:
			position = int(input("Player 1 choose position: "))
			if position in myset:
				print("Position is already chosen")
			else:
				good = True
				myset.add(position)
				board[position - 1] = player_1
		turn_1 = False
	else:
		good = False
		while not good:
			position = int(input("Player 2 choose position: "))
			if position in myset:
				print("Position is already chosen")
			else:
				good = True
				myset.add(position)
				board[position - 1] = player_2
		turn_1 = True
	print_board(board)
	cont = not check_game(board)
	print(cont)
	if not cont:
		if turn_1:
			print("The winner is player 2")
		else:
			print("The winner is player 1")
		

print("Game over")
