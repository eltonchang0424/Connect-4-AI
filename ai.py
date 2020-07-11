from connect_4_utils import *
import numpy as np
import random

def isMovesLeft(board):
	for col in board[0]:
		if col == 0:
			return True
	return False

def score_window(window, turn):
	score = 0

	if np.count_nonzero(window == turn) == 4:
		score += 100
	elif np.count_nonzero(window == turn) == 3 and np.count_nonzero(window == 0) == 1:
		score += 5
	elif np.count_nonzero(window == turn) == 2 and np.count_nonzero(window == 0) == 2:
		score += 2
	# if np.count_nonzero(window == -turn) == 3 and np.count_nonzero(window == 0) == 1:
	# 	score += 80

	return score

def evaluate(board):
	score = 0

	# center col
	center_col = []
	for i in range(board.shape[0]):
		center_col.append(board[i][board.shape[1]//2])
	score -= center_col.count(-1)*3
	score += center_col.count(1)*3

	# horizontal line
	for i in range(board.shape[0]):
		for j in range(board.shape[1]-3):
			window = board[i][j:j+4]
			score += score_window(window, 1)
			score -= score_window(window, -1)

	# vertical line
	for i in range(board.shape[0]-3):
		for j in range(board.shape[1]):
			window = board[[i,i+1,i+2,i+3],[j,j,j,j]]
			score += score_window(window, 1)
			score -= score_window(window, -1)

	# \ diag
	for i in range(board.shape[0]-3):
		for j in range(board.shape[1]-3):
			window = board[[i,i+1,i+2,i+3],[j,j+1,j+2,j+3]]
			score += score_window(window, 1)
			score -= score_window(window, -1)

	# / diag
	for i in range(board.shape[0]-3):
		for j in range(board.shape[1]-3):
			window = board[[i,i+1,i+2,i+3],[j+3,j+2,j+1,j]]
			score += score_window(window, 1)
			score -= score_window(window, -1)

	return score

def valid_moves(board):
	moves = []
	for col in range(len(board[0])):
		if board[0][col] == 0:
			moves.append(col)
	return moves

def check_winner(board):
	# horizontal line
	for i in range(board.shape[0]):
		for j in range(board.shape[1]-3):
			if board[i][j] == 1 and board[i][j+1] == 1 and board[i][j+2] == 1 and board[i][j+3] == 1:
				return 10
			elif board[i][j] == -1 and board[i][j+1] == -1 and board[i][j+2] == -1 and board[i][j+3] == -1:
				return -10

	# vertical line
	for i in range(board.shape[0]-3):
		for j in range(board.shape[1]):
			if board[i][j] == 1 and board[i+1][j] == 1 and board[i+2][j] == 1 and board[i+3][j] == 1:
				return 10
			elif board[i][j] == -1 and board[i+1][j] == -1 and board[i+2][j] == -1 and board[i+3][j] == -1:
				return -10

	# left diag
	for i in range(board.shape[0]-3):
		for j in range(board.shape[1]-3):
			if board[i][j] == 1 and board[i+1][j+1] == 1 and board[i+2][j+2] == 1 and board[i+3][j+3] == 1:
				return 10
			elif board[i][j] == -1 and board[i+1][j+1] == -1 and board[i+2][j+2] == -1 and board[i+3][j+3] == -1:
				return -10

	# right diag
	for i in range(3, board.shape[0]):
		for j in range(board.shape[1]-3):
			if board[i][j] == 1 and board[i-1][j+1] == 1 and board[i-2][j+2] == 1 and board[i-3][j+3] == 1:
				return 10
			elif board[i][j] == -1 and board[i-1][j+1] == -1 and board[i-2][j+2] == -1 and board[i-3][j+3] == -1:
				return -10

	return 0

def minimax(board, depth, maximizer, alpha, beta):
	score = evaluate(board)
	#print(board)
	#print(score)

	# check if winner
	state = check_winner(board)
	if state > 0:
		return (None, 1000000+depth)
	elif state < 0:
		return (None, -1000000-depth)

	# draw
	if not isMovesLeft(board):
		return (None, 0)

	# reached depth search limit
	if depth == 0:
		return (None, score)

	# if maximizer
	if maximizer: 
		best = float('-inf')
		column = random.choice(valid_moves(board))
		# for each possible move
		for col in valid_moves(board):
			board_copy = np.copy(board)
			# play the move on copy board
			move = play_move(col, board_copy, 1)
			new = minimax(board_copy, depth-1, False, alpha, beta)[1]
			if new > best:
				best = new
				column = col
			#print(board_copy)
			#print("Depth: " + str(depth) + " Score: " + str(new) + " Col: " + str(col) + " Max")
			# print(1, col, new)
			# print(board_copy)
			# randomizer
			elif new == best:
				if bool(random.getrandbits(1)):
					column = col
			# alpha beta pruning
			alpha = max(alpha, best)
			if beta <= alpha:
				break
		#print("Max Best col: " + str(column) + " Score: " + str(best))
		return column, best

	# if minimizer
	else: 
		best = float('inf')
		column = random.choice(valid_moves(board))
		# for each possible move
		for col in valid_moves(board):
			board_copy = np.copy(board)
			# play the move on copy board
			move = play_move(col, board_copy, -1)
			new = minimax(board_copy, depth-1, True, alpha, beta)[1]
			if new < best:
				best = new
				column = col
			#print(board_copy)
			#print("Depth: " + str(depth) + " Score: " + str(new) + " Col: " + str(col) + " Min")
			# print(-1, col, new)
			# print(board_copy)
			# randomizer
			elif new == best:
				if bool(random.getrandbits(1)):
					column = col
			# alpha beta pruning
			beta = min(beta, best)
			if beta <= alpha:
				break
		#print("Min Best col: " + str(column) + " Score: " + str(best))
		return column, best

def bestMove(board):
	# -inf if going second
	bestVal = float('inf')
	bestMove = -1

	for col in valid_moves(board):
		board_copy = np.copy(board)
		move = play_move(col, board_copy, -1)
		# maximizer true if going second
		moveVal = minimax(move, board_copy, 5, True, float('-inf'), float('inf'))
		print("move: " + str(col) + " score: " + str(moveVal))
		print(board_copy)
		# find best value move, if same value, choose random move
		if moveVal == bestVal:
			bestMove = col if np.random.randint(2) else bestMove
		# < if going second
		elif moveVal < bestVal:
			bestMove = col
			bestVal = moveVal
	return bestMove
