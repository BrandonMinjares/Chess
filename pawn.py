from piece import Piece

class Pawn(Piece):
	def __init__(self):
		super().__init__(color = "black", position = 0)
		self.name = "pawn"

	def printName(self):
		print(f"Piece: {self.name}, Color: {self.color}, Position: {self.position}")
