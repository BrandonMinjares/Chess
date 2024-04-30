class Player:
    def __init__(self, name, color, points):
        self.name = name
        self.color = color
        self.points = points

        # White plays first, then alternates
        self.playerTurn = 1 if self.color == 'white' else 0

        