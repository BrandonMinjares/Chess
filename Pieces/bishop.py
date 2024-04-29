from piece import Piece

class Bishop(Piece):
	def __init__(self, name, color, position):
		self.moves = []
		super().__init__(name = name, color=color, position = position)

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
