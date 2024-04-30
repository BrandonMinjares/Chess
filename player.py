class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.points = 0

        # White plays first, then alternates
        self.playerTurn = 1 if self.color == 'white' else 0

        