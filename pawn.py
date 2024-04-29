from piece import Piece

class Pawn(Piece):
	def __init__(self, color, position):
		self.name = "pawn"
		self.moves = []
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
		
		if self.color == "black":
			# square is less than edge of board
			# need to check if square is free though
			if y < 7:
				self.moves.append([x, y + 1])

			if x < 7:
				self.moves.append([x + 1, y + 1])

			if x > 0:
				self.moves.append([x - 1, y + 1])

		else:
			if y > 7:
				self.moves.append([x, y - 1])

			if x < 7:
				self.moves.append([x + 1, y - 1])

			if x > 0:
				self.moves.append([x - 1, y - 1])

	
	def printName(self):
		print(f"Piece: {self.name}, Color: {self.color}, Position: {self.position}")
