import os
import random
import time
from line import Line
from chequer import Chequer

def isInt(x):
    try:
        return int(x)
    except ValueError:
        return x

def printMap(lines_2D, player):
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
    
    os.system("cls")
    print(player, "turn:", "\n")
    print(MAP)


def createEntities():
    for y in y_locations:
        lines_X_axis = []
        
        for x in x_locations:
            l = Line({'x':x, 'y':y})
            
            if(x == 'I' and y == '5'):
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
            elif(x == 'H' and y == '5'):
                for i in range(0,3): 
                    c = Chequer(l, 'Y')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'G' and y == '1'):
                for i in range(0,3): 
                    c = Chequer(l, 'X')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'J' and y == '5'):
                for i in range(0,5): 
                    c = Chequer(l, 'Y')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'K' and y == '5'):
                for i in range(0,2): 
                    c = Chequer(l, 'Y')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'D' and y == '5'):
                for i in range(0,2): 
                    c = Chequer(l, 'X')
                    all_chequers.append(c)
                    l.addChequer(c)
            elif(x == 'E' and y == '3'):
                for i in range(0,2): 
                    c = Chequer(l, 'X')
                    all_chequers.append(c)
                    l.addChequer(c)
            
            all_lines.append(l)
            lines_X_axis.append(l)
        
        lines_2D.append(lines_X_axis)


def findStepLine(from_location, player, step):
    i = route.index(from_location)
    new_index = i-step if player == 'X' else i+step
    
    try:
        return route[new_index]
    except IndexError:
        return False

def findLine(x, y, player = ""):
    if player == "":
        lineList = list(filter(lambda a: a.location['x']==x and a.location['y']==y, all_lines))
    else:
        lineList = list(filter(lambda a: a.location['x']==x and a.location['y']==y and a.player==player, all_lines))  
    return None if len(lineList) == 0 else lineList[0]

def findChequer(x, y, player = ""):
    if player == "":
        chequerList = list(filter(lambda a: a.line.location['x']==x and a.line.location['y']==y, all_chequers))
    else:
        chequerList = list(filter(lambda a: a.line.location['x']==x and a.line.location['y']==y and a.player==player, all_chequers))
    return None if len(chequerList) == 0 else chequerList[0]

def rollDice(player):
    print("{} player rolled...".format(player))
    #time.sleep(1)
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    findLine('F','3').chequers = list(range(r1))
    findLine('G','3').chequers = list(range(r2))
    
    print("The dice are {} and {}".format(r1,r2))
    #time.sleep(1)
    
    if r1 == r2: return [r1, r1, r1, r1]
    else: return [r1, r2]
    
def brokenControl(player, opponent_y_axis, dice_arr):
    line_count = len(list(filter(lambda l: (l.player==player or len(l.chequers)<=1) and (l.location['x'] in player_home) and (l.location['y']==opponent_y_axis) and (player_home.index(l.location['x'])+1 in dice_arr), all_lines)))
    return True if (line_count > 0) else False

# TODO: collectControl yap
# TODO: moveControl yap

def changePlayer(player):
    #time.sleep(1)
    os.system("cls")
    return "Y" if player == "X" else "X"

def main():
    player = ""
    
    print("\t\t\tBACKGOMMON GAME")
    #input("1- New game \n2- Continue game \n--> ")
        
    while True:
        os.system("cls")
        
        print("The dice are rolled for X...")
        #time.sleep(1)
        r_X = random.randint(1,6)
        print("X dice ->", r_X)
        findLine('F','3').chequers = list(range(r_X))
        
        #time.sleep(1)
        
        print("The dice are rolled for Y...")
        #time.sleep(1)
        r_Y = random.randint(1,6)
        print("Y dice ->", r_Y)
        findLine('G','3').chequers = list(range(r_Y))
        
        if(r_X == r_Y):
            print("Dice equal! Dice are thrown again.")
            #time.sleep(1)
            continue
        elif(r_X > r_Y): player = "X"
        else: player = "Y"
    
        print(player, "player starts!")
        #time.sleep(1)
        break
    
    while True:
        dice_arr = rollDice(player)
        home_y_axis = '1' if(player == 'X') else '5'
        opponent_y_axis = '5' if(player == 'X') else '1'
        collect_x_axis = 'E' if(player == 'X') else 'H'
            
        # Broken Chequer
        broken_x_axis = 'E' if(player == 'X') else 'H'
        broken_line = findLine(broken_x_axis, '3')
        if len(broken_line.chequers) != 0:
            print(player, "player have broken chequers!")
            
            while True:
                printMap(lines_2D, player)
                
                if brokenControl(player, opponent_y_axis, dice_arr) == False:
                    print(player, "player passed! Because there are no moves.")
                    break
                
                while True:
                    number = isInt(input("Which number do you want to go to? {}: ".format(dice_arr)))
                    if number == 'exit': return
                    elif number in dice_arr: break
                    else:
                        print("Invalid number! Only {}".format(dice_arr))
                        continue
                
                home_l = findLine(player_home[number-1], opponent_y_axis)
                if (home_l.player == player) or (len(home_l.chequers) <= 1):
                    home_l.addChequer(broken_line.chequers[0], all_lines)
                    dice_arr.remove(number)
                else:
                    print("Invalid move!")
                
                if len(broken_line.chequers) == 0: break
            
            if (len(dice_arr) == 0) or (len(broken_line.chequers) != 0): 
                player = changePlayer(player)
                continue
        
        
        # Collect Chequer
        collect_count = len(findLine(collect_x_axis, '4').chequers)
        home_chequers = list(filter(lambda a: a.line.location['x'] in player_home and a.line.location['y']==home_y_axis and a.player==player, all_chequers))
        if len(home_chequers) + collect_count == 15:
            while True:
                printMap(lines_2D, player)
            
                f = input("From (e.g: E1): ")
                c = findChequer(f[0], f[1], player)
                if(f == 'exit'): return
                elif(c == None):
                    print("{} chequer is not found for {} player!".format(f, player))
                    time.sleep(2)
                    continue
                
                while True:
                    status = input("Step or collect? (Enter: 'step' or 'collect') \n-> ")
                    if status in ['step','collect']: break
                    else: print("You must enter step or collect!")
            
                if status == 'step':
                    while True:
                        step = isInt(input("How many steps? {}: ".format(dice_arr)))
                        if step == 'exit': return
                        elif step in dice_arr: break
                        else:
                            print("Invalid step! Only {}".format(dice_arr))
                            continue
                    
                    t = findStepLine(f, player, step)
                    if t == False:
                        print("Invalid step for {} dice!".format(step))
                        time.sleep(1)
                        continue
                    
                    l = findLine(t[0], t[1])
                    result = l.addChequer(c, all_lines)
                    if(result == False):
                        print("Invalid move!")
                        time.sleep(1)
                        continue
                    
                    dice_arr.remove(step)  
                
                if status == 'collect':
                    home_number = player_home.index(f[0]) + 1
                    if home_number in dice_arr:
                        c.collect(all_lines)
                        dice_arr.remove(home_number)
                    else:
                        print("Invalid collect!")
                        time.sleep(1)
                        continue
                    
                if len(dice_arr) == 0: break
                
            player = changePlayer(player)
            continue
            
            
        # Game Stream
        while True:
            printMap(lines_2D, player)
        
            f = input("From (e.g: E1): ")
            c = findChequer(f[0], f[1], player)
            if(f == 'exit'): return
            elif(c == None):
                print("{} chequer is not found for {} player!".format(f, player))
                time.sleep(2)
                continue
        
            while True:
                step = isInt(input("How many steps? {}: ".format(dice_arr)))
                if step == 'exit': return
                elif step in dice_arr: break
                else:
                    print("Invalid step! Only {}".format(dice_arr))
                    continue
            
            t = findStepLine(f, player, step)
            if t == False:
                print("Invalid step for {} dice!".format(step))
                time.sleep(1)
                continue
            
            l = findLine(t[0], t[1])
            result = l.addChequer(c, all_lines)
            if(result == False):
                print("Invalid move!")
                time.sleep(1)
                continue
        
            dice_arr.remove(step)  
            if len(dice_arr) == 0: break
        
        
        player = changePlayer(player)
    
    
if __name__ == "__main__":
    x_locations = ['A','B','C','D','E','F','G','H','I','J','K','L']
    y_locations = ['1','2','3','4','5']
    route = ['L1','K1','J1','I1','H1','G1','F1','E1','D1','C1','B1','A1','A5','B5','C5','D5','E5','F5','G5','H5','I5','J5','K5','L5']
    player_home = ['L','K','J','I','H','G']
    
    all_chequers = []
    all_lines = []
    lines_2D = []
    
    createEntities()
    
    main()
    
    
                
        
        
        
        
        