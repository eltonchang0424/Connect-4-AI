from connect_4_utils import *
from ai import *

game_over = False
turn = 1

length = int(input("Enter board length: "))
width = int(input("Enter board width: "))
board = create_game(length,width)
print(print_board(board))
moveNo = 1

playing = False
depth = 5

while not game_over:
	if turn > 0:
		if not isMovesLeft(board):
			print("\nIt's a draw")
			break
		# player code
		if playing:
			valid_move = False
			while not valid_move:
				move = int(input("\nEnter column to play: "))
				piece = play_move(move-1, board, 1)
				if piece == None:
					print("Invalid move, try again")
				else:
					valid_move = True
			print("\nMove number " + str(moveNo) + ": Player played " + str(move + 1))
			print(print_board(board))
			state = check_win(piece[0]+3, piece[1]+3, board)
			if state != 0:
				print("\nPlayer wins")
				game_over = True
			turn -= 2
			moveNo += 1
		# ai code
		else:		
			move, score = minimax(board, depth, False, float('-inf'), float('inf'))
			piece = play_move(move, board, 1)
			print("\nMove number " + str(moveNo) + ": Computer 1 played " + str(move + 1))
			print(print_board(board))
			state = check_win(piece[0]+3, piece[1]+3, board)
			if state != 0:
				print("\nComputer 1 wins")
				game_over = True
			turn -= 2
			moveNo += 1

	elif turn < 0:
		if not isMovesLeft(board):
			print("\nIt's a draw")
			break
		# multiplayer code
		# move = int(input("\nPlayer 2, enter column to play: "))
		# piece = play_move(move-1, board, -1)
		# print(print_board(board))

		# ai code
		move, score = minimax(board, depth, True, float('-inf'), float('inf'))
		piece = play_move(move, board, -1)
		print("\nMove number " + str(moveNo) + ": Computer 2 played " + str(move + 1))
		print(print_board(board))
		state = check_win(piece[0]+3, piece[1]+3, board)
		if state != 0:
			print("\nComputer 2 wins")
			game_over = True
		turn += 2
		moveNo += 1
