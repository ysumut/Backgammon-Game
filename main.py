from line import Line
from chequer import Chequer


if __name__ == "__main__":
    x_locations = ['A','B','C','D','E','F','G','H','I','J','K','L']
    y_locations = ['1','2','3','4','5']
    all_lines = []
    
    for x in x_locations:
        for y in y_locations:
            l = Line({'x':x, 'y':y})
            
            if(x == 'A' and y == '1'):
                for i in range(0,5): l.addChequer(Chequer(l, 'Y'))
            elif(x == 'A' and y == '5'):
                for i in range(0,5): l.addChequer(Chequer(l, 'X')) 
            elif(x == 'E' and y == '1'):
                for i in range(0,3): l.addChequer(Chequer(l, 'X'))
            elif(x == 'E' and y == '5'):
                for i in range(0,3): l.addChequer(Chequer(l, 'Y'))
            elif(x == 'G' and y == '1'):
                for i in range(0,5): l.addChequer(Chequer(l, 'X'))
            elif(x == 'G' and y == '5'):
                for i in range(0,5): l.addChequer(Chequer(l, 'Y'))
            elif(x == 'L' and y == '1'):
                for i in range(0,2): l.addChequer(Chequer(l, 'Y'))
            elif(x == 'L' and y == '5'):
                for i in range(0,2): l.addChequer(Chequer(l, 'X'))
            
            all_lines.append(l)
    
    
    
    for each in all_lines:
        print(each.location['x'], each.location['y'], '->', each.printChequers())