from board import Board
from pawn import Pawn
from piece import Piece

def main():
	obj = Board()
	obj.printBoard()

	new_pawn = Pawn(Piece())
	new_pawn.printName()

if __name__ == "__main__":
	main()
	
