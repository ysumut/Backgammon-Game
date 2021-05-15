from line import Line
from chequer import Chequer

def printMap(lines_2D):
    MAP = " _A__ _B__ _C__ _D__ _E__ _F__  _G__ _H__ _I__ _J__ _K__ _L__ \n"
    MAP_LINE = "|_A__|_B__|_C__|_D__|_E__|_F__||_G__|_H__|_I__|_J__|_K__|_L__| y_axis"
    
    i = 1
    for each in lines_2D:
        new_map_line = MAP_LINE
        
        for item in each:
            p_item = item.printChequers()
            underscore = '__' if(len(p_item) == 3) else '_'
            
            new_map_line = new_map_line.replace(item.location['x']+underscore, p_item)
        
        MAP += new_map_line.replace('y_axis', str(i)) + '\n'
        i += 1
    
    print(MAP)
    

if __name__ == "__main__":
    x_locations = ['A','B','C','D','E','F','G','H','I','J','K','L']
    y_locations = ['1','2','3','4','5']
    all_lines = []
    lines_2D = []
    
    for y in y_locations:
        lines_X_axis = []
        
        for x in x_locations:
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
            lines_X_axis.append(l)
        
        lines_2D.append(lines_X_axis)
    
    
    printMap(lines_2D)
    
                
        
        
        
        
        