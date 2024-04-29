from Pieces.pawn import Pawn
from Pieces.bishop import Bishop
from Pieces.rook import Rook
from Pieces.queen import Queen
from Pieces.king import King

class Board:
	def __init__(self):
		self.board = [["-" for _ in range(8)] for _ in range(8)]
	
	def start(self):
		print('hello')

	def initializeBoard(self):
		self.board[0][0] = Rook()

	def printBoard(self):
		for row in self.board:
			print(" ".join(row))
