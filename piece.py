class Piece:
	def __init__(self, color, position):
		self.color = color
		self.position = position
		self.active = True

	def move(self, new_position):
		self.position = new_position

	# has the piece been captured
	def active(self):
		self.active = False if self.active == True else False
		
