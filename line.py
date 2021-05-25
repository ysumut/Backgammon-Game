class Line:
    def __init__(self, location):
        self.location = location
        self.chequers = []
        self.player = ""
    
    def addChequer(self, c, all_lines = []):
        if(self.player == "" or self.player == c.player): # Normal taş ekleme
            
            if(self != c.line): c.line.removeChequer(c)
            
            c.line = self
            self.chequers.append(c)
            self.player = c.player
            return True
        
        elif(self.player != c.player and len(self.chequers) == 1): # Taş kırma işlemi
            broken_c = self.chequers[0]
            broken_c.line.removeChequer(broken_c)
            self.addBrokenChequer(broken_c, all_lines)
            
            if(self != c.line): c.line.removeChequer(c)
            
            c.line = self
            self.chequers.append(c)
            self.player = c.player
            return True
        
        else:
            return False
        
    def removeChequer(self, c):
        self.chequers.remove(c)
        if(len(self.chequers) == 0):
            self.player = ""
        
    def printChequers(self):
        if len(self.chequers) == 0 or ((self.location['x']=='E' or self.location['x']=='H') and self.location['y']=='4'):
            return "__"
        else:
            return str(len(self.chequers)) + self.player
    
    def addBrokenChequer(self, c, all_lines):
        x_axis = 'E' if(c.player == 'X') else 'H'
        l = list(filter(lambda a: a.location['x']==x_axis and a.location['y']=='3', all_lines))[0]
        
        c.line = l
        l.addChequer(c)




