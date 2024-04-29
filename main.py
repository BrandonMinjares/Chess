from board import Board
from pawn import Pawn

def main():
	obj = Board()
	obj.printBoard()
	new_pawn = Pawn("black", [0, 0])
	new_pawn.printName()

if __name__ == "__main__":
	main()
	
