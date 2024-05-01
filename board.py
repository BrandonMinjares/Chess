from Pieces.pawn import Pawn
from Pieces.bishop import Bishop
from Pieces.rook import Rook
from Pieces.knight import Knight
from Pieces.queen import Queen
from Pieces.king import King

class Board():
	def __init__(self):
		self.board = [["-" for _ in range(8)] for _ in range(8)]
	
	def start(self):
		print('Start game')

	def initializeBoard(self):
        # Set up white pieces
		self.board[0][0] = self.players['white'].get_pieces()['rooks'][0]
		self.board[0][1] = self.players['white'].get_pieces()['knights'][0]
		self.board[0][2] = self.players['white'].get_pieces()['bishops'][0]
		self.board[0][3] = self.players['white'].get_pieces()['queen']
		self.board[0][4] = self.players['white'].get_pieces()['king']
		self.board[0][5] = self.players['white'].get_pieces()['bishops'][1]
		self.board[0][6] = self.players['white'].get_pieces()['knights'][1]
		self.board[0][7] = self.players['white'].get_pieces()['rooks'][1]
		for i in range(8):
			self.board[1][i] = self.players['white'].get_pieces()['pawns'][i]

		# Set up black pieces
		self.board[7][0] = self.players['black'].get_pieces()['rooks'][0]
		self.board[7][1] = self.players['black'].get_pieces()['knights'][0]
		self.board[7][2] = self.players['black'].get_pieces()['bishops'][0]
		self.board[7][3] = self.players['black'].get_pieces()['queen']
		self.board[7][4] = self.players['black'].get_pieces()['king']
		self.board[7][5] = self.players['black'].get_pieces()['bishops'][1]
		self.board[7][6] = self.players['black'].get_pieces()['knights'][1]
		self.board[7][7] = self.players['black'].get_pieces()['rooks'][1]
		for i in range(8):
			self.board[6][i] = self.players['black'].get_pieces()['pawns'][i]

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
