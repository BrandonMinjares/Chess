class Piece:
	def __init__(self, name, color, position):
		self.name = name
		self.color = color
		self.position = position
		self.active = True
		self.hasMoved = False

	def move(self, new_position):
		# piece has moved from initial position
		if self.hasMoved == False: self.hasMoved = True

		self.position = new_position



	# has the piece been captured
	def active(self):
		self.active = False if self.active == True else False
		