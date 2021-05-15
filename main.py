import os
import random
import time
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
            if(len(p_item) == 3): underscore = '__'
            elif(len(p_item) == 2): underscore = '_'
            else: underscore = ''
            
            new_map_line = new_map_line.replace(item.location['x']+underscore, p_item)
        
        MAP += new_map_line.replace('y_axis', str(i)) + '\n'
        i += 1
    
    print(MAP)


def createEntities():
    for y in y_locations:
        lines_X_axis = []
        
        for x in x_locations:
            l = Line({'x':x, 'y':y})
            
            if(x == 'A' and y == '1'):
                for i in range(0,5): 
                    c = Chequer(l, 'Y')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'A' and y == '5'):
                for i in range(0,5): 
                    c = Chequer(l, 'X')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'E' and y == '1'):
                for i in range(0,3): 
                    c = Chequer(l, 'X')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'E' and y == '5'):
                for i in range(0,3): 
                    c = Chequer(l, 'Y')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'G' and y == '1'):
                for i in range(0,5): 
                    c = Chequer(l, 'X')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'G' and y == '5'):
                for i in range(0,5): 
                    c = Chequer(l, 'Y')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'L' and y == '1'):
                for i in range(0,2): 
                    c = Chequer(l, 'Y')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'L' and y == '5'):
                for i in range(0,2): 
                    c = Chequer(l, 'X')
                    all_chequers.append(c)
                    l.addChequer(c)
            
            all_lines.append(l)
            lines_X_axis.append(l)
        
        lines_2D.append(lines_X_axis)


def findLine(x, y):
    return list(filter(lambda a: a.location['x']==x and a.location['y']==y, all_lines))[0]


def main():
    player = ""
    print("\t\t\tBACKGOMMON GAME")
    #input("1- New game \n2- Continue game \n--> ")
        
    while True:
        os.system("cls")
        
        print("The dice are rolled for X...")
        time.sleep(2)
        r_X = random.randint(1,6)
        print("X dice ->", r_X)
        findLine('F','3').chequers = list(range(r_X))
        
        time.sleep(2)
        
        print("The dice are rolled for Y...")
        time.sleep(2)
        r_Y = random.randint(1,6)
        print("Y dice ->", r_Y)
        findLine('G','3').chequers = list(range(r_Y))
        
        if(r_X == r_Y):
            print("Dice equal! Dice are thrown again.")
            time.sleep(2)
            continue
        elif(r_X > r_Y): player = "X"
        else: player = "Y"
    
        print(player, "player starts!")
        time.sleep(2)
        break
    
    while True:
        os.system("cls")
        
        print(player, "turn:")
        printMap(lines_2D)
        location = input("Location: ")
        
        if(location == 'exit'): break
    
    
if __name__ == "__main__":
    x_locations = ['A','B','C','D','E','F','G','H','I','J','K','L']
    y_locations = ['1','2','3','4','5']
    
    all_chequers = []
    all_lines = []
    lines_2D = []
    
    createEntities()
    
    main()
    
    
                
        
        
        
        
        