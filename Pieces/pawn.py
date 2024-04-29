from piece import Piece

class Pawn(Piece):
	def __init__(self, name, color, position):
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
		moves = []
		x, y = self.getPosition()
		
		if self.color == "white":
			# square is less than edge of board
			# need to check if square is free though
			if self.hasMoved == False:
				moves.append([x + 2, y])
			if x < 7:
				moves.append([x + 1, y])

				# capture enemy piece
				if y < 7: 
					moves.append([x + 1, y + 1])
				if y > 0:
					moves.append([x + 1, y - 1])
			
		return moves
	
	def printName(self):
		print(f"Piece: {self.name}, Color: {self.color}, Position: {self.position}")
