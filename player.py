from Pieces.pawn import Pawn
from Pieces.bishop import Bishop
from Pieces.rook import Rook
from Pieces.knight import Knight
from Pieces.queen import Queen
from Pieces.king import King

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.points = 0

        self.pieces = {
            'king': King(self.color),
            'queen': [Queen(self.color)],
            'rooks': [Rook(self.color) for _ in range(2)],
            'knights': [Knight(self.color) for _ in range(2)],
            'bishops': [Bishop(self.color) for _ in range(2)],
            'pawns': [Pawn(self.color) for _ in range(8)]
        }
