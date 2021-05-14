class Line:
    def __init__(self, location):
        self.location = location
        self.chequers = []
        self.player = None
    
    def addChequer(self, c, all_chequers = []):
        if(self.player == None or self.player == c.player): # Normal taş ekleme
            c.location = self.location
            self.chequers.append(c)
            self.player = c.player
            return True
        
        elif(self.player != c.player and len(self.chequers) == 1): # Taş kırma işlemi
            broken_c = self.chequers[0]
            c.location = self.location
            
            self.removeChequer(broken_c)
            self.player = c.player
            self.addBrokenChequer(broken_c, all_chequers)
            return True
        
        else:
            return False
        
    def removeChequer(self, c):
        self.chequers.remove(c)
        if(len(self.chequers) == 0):
            self.player = None
        
    def printChequers(self):
        if(len(self.chequers) == 0):
            return ""
        else:
            return str(len(self.chequers)) + self.player
    
    def addBrokenChequer(self, c, all_chequers):
        broken_x_axis = ['E' if c.player == 'X' else 'H']
        l = list(filter(lambda a: a.location['x']==broken_x_axis and a.location['y']=='3'))[0]
        l.addChequer(c)











