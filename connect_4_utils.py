import numpy as np

def create_game(length, width):
	board = np.zeros((width, length))
	return board

def print_board(board):
	display = np.copy(board)
	display = np.where(display == 0, '-', display)
	display = np.where(display == '1.0', 'O', display)
	display = np.where(display == '-1.0', 'X', display)
	return display	

def play_move(col, board, mark):
	if col >= board.shape[1] or col < 0:
		return None
	elif board[0][col] != 0:
		return None
	else:
		first_open_row = 0
		for i in range(board.shape[0]-1, -1, -1):
			if board[i][col] == 0:
				first_open_row = i
				break
		board[first_open_row][col] = mark
		return (first_open_row, col)

def check_win(piecex, piecey, board):
	# pad board with zeros to avoid full board check, better runtime
	tboard = np.pad(board, 3, mode='constant')

	# left diag
	if tboard[piecex-3][piecey-3] + tboard[piecex-2][piecey-2] + tboard[piecex-1][piecey-1] + tboard[piecex][piecey] == 4 or tboard[piecex-2][piecey-2] + tboard[piecex-1][piecey-1] + tboard[piecex][piecey] + tboard[piecex+1][piecey+1] == 4 or tboard[piecex-1][piecey-1] + tboard[piecex][piecey] + tboard[piecex+1][piecey+1] + tboard[piecex+2][piecey+2] == 4 or tboard[piecex][piecey] + tboard[piecex+1][piecey+1] + tboard[piecex+2][piecey+2] + tboard[piecex+3][piecey+3] == 4:
		return 10
	elif tboard[piecex-3][piecey-3] + tboard[piecex-2][piecey-2] + tboard[piecex-1][piecey-1] + tboard[piecex][piecey] == -4 or tboard[piecex-2][piecey-2] + tboard[piecex-1][piecey-1] + tboard[piecex][piecey] + tboard[piecex+1][piecey+1] == -4 or tboard[piecex-1][piecey-1] + tboard[piecex][piecey] + tboard[piecex+1][piecey+1] + tboard[piecex+2][piecey+2] == -4 or tboard[piecex][piecey] + tboard[piecex+1][piecey+1] + tboard[piecex+2][piecey+2] + tboard[piecex+3][piecey+3] == -4:
		return -10

	# right diag
	if tboard[piecex-3][piecey+3] + tboard[piecex-2][piecey+2] + tboard[piecex-1][piecey+1] + tboard[piecex][piecey] == 4 or tboard[piecex-2][piecey+2] + tboard[piecex-1][piecey+1] + tboard[piecex][piecey] + tboard[piecex+1][piecey-1] == 4 or tboard[piecex-1][piecey+1] + tboard[piecex][piecey] + tboard[piecex+1][piecey-1] + tboard[piecex+2][piecey-2] == 4 or tboard[piecex][piecey] + tboard[piecex+1][piecey-1] + tboard[piecex+2][piecey-2] + tboard[piecex+3][piecey-3] == 4:
		return 10
	elif tboard[piecex-3][piecey+3] + tboard[piecex-2][piecey+2] + tboard[piecex-1][piecey+1] + tboard[piecex][piecey] == -4 or tboard[piecex-2][piecey+2] + tboard[piecex-1][piecey+1] + tboard[piecex][piecey] + tboard[piecex+1][piecey-1] == -4 or tboard[piecex-1][piecey+1] + tboard[piecex][piecey] + tboard[piecex+1][piecey-1] + tboard[piecex+2][piecey-2] == -4 or tboard[piecex][piecey] + tboard[piecex+1][piecey-1] + tboard[piecex+2][piecey-2] + tboard[piecex+3][piecey-3] == -4:
		return -10

	# vertical line
	if tboard[piecex-3][piecey] + tboard[piecex-2][piecey] + tboard[piecex-1][piecey] + tboard[piecex][piecey] == 4 or tboard[piecex-2][piecey] + tboard[piecex-1][piecey] + tboard[piecex][piecey] + tboard[piecex+1][piecey] == 4 or tboard[piecex-1][piecey] + tboard[piecex][piecey] + tboard[piecex+1][piecey] + tboard[piecex+2][piecey] == 4 or tboard[piecex][piecey] + tboard[piecex+1][piecey] + tboard[piecex+2][piecey] + tboard[piecex+3][piecey] == 4:
		return 10
	if tboard[piecex-3][piecey] + tboard[piecex-2][piecey] + tboard[piecex-1][piecey] + tboard[piecex][piecey] == -4 or tboard[piecex-2][piecey] + tboard[piecex-1][piecey] + tboard[piecex][piecey] + tboard[piecex+1][piecey] == -4 or tboard[piecex-1][piecey] + tboard[piecex][piecey] + tboard[piecex+1][piecey] + tboard[piecex+2][piecey] == -4 or tboard[piecex][piecey] + tboard[piecex+1][piecey] + tboard[piecex+2][piecey] + tboard[piecex+3][piecey] == -4:
		return -10

	# horizontal line
	if tboard[piecex][piecey-3] + tboard[piecex][piecey-2] + tboard[piecex][piecey-1] + tboard[piecex][piecey] == 4 or tboard[piecex][piecey-2] + tboard[piecex][piecey-1] + tboard[piecex][piecey] + tboard[piecex][piecey+1] == 4 or tboard[piecex][piecey-1] + tboard[piecex][piecey] + tboard[piecex][piecey+1] + tboard[piecex][piecey+2] == 4 or tboard[piecex][piecey] + tboard[piecex][piecey+1] + tboard[piecex][piecey+2] + tboard[piecex][piecey+3] == 4:
		return 10
	if tboard[piecex][piecey-3] + tboard[piecex][piecey-2] + tboard[piecex][piecey-1] + tboard[piecex][piecey] == -4 or tboard[piecex][piecey-2] + tboard[piecex][piecey-1] + tboard[piecex][piecey] + tboard[piecex][piecey+1] == -4 or tboard[piecex][piecey-1] + tboard[piecex][piecey] + tboard[piecex][piecey+1] + tboard[piecex][piecey+2] == -4 or tboard[piecex][piecey] + tboard[piecex][piecey+1] + tboard[piecex][piecey+2] + tboard[piecex][piecey+3] == -4:
		return -10
		
	return 0