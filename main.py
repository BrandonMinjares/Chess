from board import Board
from Pieces.pawn import Pawn

def main():
	game = Board()
	game.initializeBoard()
	# game.printBoard()
	pawn = game.board[1][0]
	print(pawn.allowableMoves())
	
	"""
	game.board[3][0] = pawn
	game.board[1][0] = "-"
	game.printBoard()
	"""

if __name__ == "__main__":
	main()
	
