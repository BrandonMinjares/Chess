class Board:
	def __init__(self):
		self.board = [["-" for _ in range(8)] for _ in range(8)]
	
	def start(self):
		print('hello')

	def printBoard(self):
		for row in self.board:
			print(" ".join(row))
