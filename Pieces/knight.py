from piece import Piece

class Knight(Piece):
	def __init__(self, color, position):
		self.moves = []
		self.name = "Knight"
		super().__init__(color=color, position = position)

	def move(self, new_position):
		# piece has moved from initial position
		if self.hasMoved == False: self.hasMoved = True

		self.position = new_position

	def getPosition(self):
		return self.position

	def setPosition(self):
		pass

	def allowableMoves(self):
		x, y = self.getPosition()

	
	def printName(self):
		print(f"Piece: {self.name}, Color: {self.color}, Position: {self.position}")
