class Chequer:
    def __init__(self, line, player):
        self.line = line
        self.player = player
    
    def collect(self, all_lines):
        # E4 or H4
        x_axis = 'E' if(self.player == 'X') else 'H'
        l = list(filter(lambda a: a.location['x']==x_axis and a.location['y']=='4', all_lines))[0]
        
        l.addChequer(self)
