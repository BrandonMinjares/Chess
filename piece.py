class Piece:
	def __init__(self, color, position, name):
		self.color = color
		self.position = position
		self.active = True
		self.name = name

	def move(self, new_position):
		self.position = new_position

	# has the piece been captured
	def active(self):
		self.active = False if self.active == True else False
		
	def printName(self):
		print(f"Piece: {self.name}, Color: {self.color}, Position: {self.position}")
