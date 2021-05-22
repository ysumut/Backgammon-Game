class Chequer:
    def __init__(self, line, player):
        self.line = line
        self.player = player
    
    def removeLine(self):
        self.line.removeChequer(self)
        self.line = None
