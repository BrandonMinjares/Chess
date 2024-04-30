import random
from board import Board
from Pieces.pawn import Pawn
from player import Player

def main():
	game = Board()
	game.initializeBoard()

	# chooses who is black and white
	num = random.randint(0, 1)

	playerOne = Player("Bran", "white")
	playerTwo = Player("Adam", "black")

	while(1):
		if playerOne.playerTurn == 1:
			print("Player one turn")
			playerOne.playerTurn = 0
			playerTwo.playerTurn = 1
		else:
			print("Player two turn")
			playerTwo.playerTurn = 0
			playerOne.playerTurn == 1

	


if __name__ == "__main__":
	main()
	
