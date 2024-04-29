from piece import Piece

class Pawn(Piece):
	def __init__(self, color, position):
		self.name = "pawn"
		super().__init__(color=color, position = position)


	def printName(self):
		print(f"Piece: {self.name}, Color: {self.color}, Position: {self.position}")

