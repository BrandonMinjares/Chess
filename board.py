from Pieces.pawn import Pawn
from Pieces.bishop import Bishop
from Pieces.rook import Rook
from Pieces.knight import Knight
from Pieces.queen import Queen
from Pieces.king import King

class Board:
	def __init__(self):
		self.board = [["-" for _ in range(8)] for _ in range(8)]
	
	def start(self):
		print('Start game')

	def initializeBoard(self):
		for x in range(0, 8):
			self.board[1][x] = Pawn("Pawn", "white", [1, x])

		self.board[0][0] = Rook("Rook", "white", [0, 0])
		self.board[0][1] = Knight("Knight", "white", [0, 1])
		self.board[0][2] = Bishop("Bishop", "white", [0, 2])
		self.board[0][3] = Queen("Queen", "white", [0, 3])
		self.board[0][4] = King("King", "white", [0, 4])
		self.board[0][5] = Bishop("Bishop", "white", [0, 5])
		self.board[0][6] = Knight("Knight", "white", [0, 6])
		self.board[0][7] = Rook("Rook", "white", [1, 7])

		for x in range(0, 8):
			self.board[6][x] = Pawn("Pawn", "black", [9, x])

		self.board[7][0] = Rook("Rook", "black", [7, 0])
		self.board[7][1] = Knight("Knight", "black", [7, 1])
		self.board[7][2] = Bishop("Bishop", "black", [7, 2])
		self.board[7][3] = Queen("Queen", "black", [7, 3])
		self.board[7][4] = King("King", "black", [7, 4])
		self.board[7][5] = Bishop("Bishop", "black", [7, 5])
		self.board[7][6] = Knight("Knight", "black", [7, 6])
		self.board[7][7] = Rook("Rook", "black", [7, 7])

	def printBoard(self):
		for i, row in enumerate(self.board):
			print(f"{8 - i} | {' '.join(self.get_piece_symbol(piece) for piece in row)} |")

	def get_piece_symbol(self, piece):
		if piece is None:
			return '.'
		elif isinstance(piece, Pawn):
			return 'p' if piece.color == 'black' else 'P'
		elif isinstance(piece, Rook):
			return 'r' if piece.color == 'black' else 'R'
		elif isinstance(piece, Knight):
			return 'n' if piece.color == 'black' else 'N'
		elif isinstance(piece, Bishop):
			return 'b' if piece.color == 'black' else 'B'
		elif isinstance(piece, Queen):
			return 'q' if piece.color == 'black' else 'Q'
		elif isinstance(piece, King):
			return 'k' if piece.color == 'black' else 'K'
		else:
			return '.'
