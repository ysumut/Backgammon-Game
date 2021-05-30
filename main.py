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
    
    with open('Table.dat', 'w') as file:
        file.write(MAP)


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

    
def getSavedEntities():
    chequers = []
    
    with open('Save.dat', 'r') as file:
        for each in file.readlines():
            data = each.split(' / ')
            if data[0] == 'turn':
                player = data[1]
                allDices = data[2].split(',')
                currentDices = data[3].split(',')
            if data[0] == 'chequer':
                is_collect = True if (data[3]=='True') else False
                chequers.append([eval(data[1]), data[2], is_collect])
        
    for y in y_locations:
        lines_X_axis = []
        
        for x in x_locations:
            l = Line({'x':x, 'y':y})
            all_lines.append(l)
            lines_X_axis.append(l)
        
        lines_2D.append(lines_X_axis)
    
    for each in chequers:
        line = list(filter(lambda l: each[0]['x']==l.location['x'] and each[0]['y']==l.location['y'], all_lines))[0]
        
        c = Chequer(line, each[1])
        c.is_collect = each[2]
        all_chequers.append(c)
        line.addChequer(c)
    
    all_dices = []
    dice_arr = []
    for d in allDices: 
        if d != "": all_dices.append(int(d))
    for d in currentDices: 
        if d != "": dice_arr.append(int(d))
    
    findLine('F','3').chequers = list(range(all_dices[0]))
    findLine('G','3').chequers = list(range(all_dices[1]))
    return (player, all_dices, dice_arr)
    

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
    time.sleep(1)
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    findLine('F','3').chequers = list(range(r1))
    findLine('G','3').chequers = list(range(r2))
    
    print("The dice are {} and {}".format(r1,r2))
    time.sleep(1)
    
    with open('Log.dat', 'a') as file:
        file.write("{} {} {}\n".format(player, r1, r2))
    
    if r1 == r2: return [r1, r1, r1, r1]
    else: return [r1, r2]

def rollFirstDices():
    while True:
        os.system("cls")
        
        print("The dice are rolled for X...")
        time.sleep(1)
        r_X = random.randint(1,6)
        print("X dice ->", r_X)
        findLine('F','3').chequers = list(range(r_X))
        
        time.sleep(1)
        
        print("The dice are rolled for Y...")
        time.sleep(1)
        r_Y = random.randint(1,6)
        print("Y dice ->", r_Y)
        findLine('G','3').chequers = list(range(r_Y))
        
        if(r_X == r_Y):
            print("Dice equal! Dice are thrown again.")
            time.sleep(1)
            continue
        else:
            with open('Log.dat', 'w') as file:
                file.write("{}\n{}\n".format(r_X, r_Y))
        
        if(r_X > r_Y): player = "X"
        else: player = "Y"
    
        print(player, "player starts!")
        time.sleep(1)
        return player
    

def brokenControl(player, opponent_y_axis, dice_arr):
    line_count = len(list(filter(lambda l: (l.player==player or len(l.chequers)<=1) and (l.location['x'] in player_home) and (l.location['y']==opponent_y_axis) and (player_home.index(l.location['x'])+1 in dice_arr), all_lines)))
    return True if (line_count > 0) else False

def collectControl(player, home_y_axis, dice_arr):
    lines = list(filter(lambda l: (l.player==player and len(l.chequers)>=1) and (l.location['x'] in player_home) and (l.location['y']==home_y_axis), all_lines))
    for l in lines:
        home_number = player_home.index(l.location['x']) + 1
        if len(list(filter(lambda d: d >= home_number, dice_arr))) > 0:
            return True
    return False

def moveControl(player, dice_arr):
    chequers = list(filter(lambda c: (c.player==player) and (c.is_collect==False) and (c.line.location['y'] in ['1','5']), all_chequers))
    
    for c in chequers:
        c_location = c.line.location['x'] + c.line.location['y']
        for dice in dice_arr:
            str_line = findStepLine(c_location, player, dice)
            if str_line != False:
                line = findLine(str_line[0], str_line[1])
                if (line.player == "" or line.player == c.player) or (line.player != c.player and len(line.chequers) == 1):
                    return True
    return False

def finishControl(player):
    return len(list(filter(lambda c: c.player==player and c.is_collect==True, all_chequers))) == 15

def changePlayer(player):
    time.sleep(1)
    os.system("cls")
    return "Y" if player == "X" else "X"

def saveGame(player, allDices, currentDices):
    print("The game saved.")
    
    all_dices = ""
    current_dices = ""
    for d in allDices: all_dices += str(d) + ','
    for d in currentDices: current_dices += str(d) + ','
    
    with open('Save.dat', 'w') as file:
        file.write("turn / {} / {} / {} / \n".format(player, all_dices, current_dices))
        i = 1
        for c in all_chequers:
            if (i == len(all_chequers)): text = "chequer / {} / {} / {} / "
            else: text = "chequer / {} / {} / {} / \n"
        
            file.write(text.format(c.line.location, c.player, c.is_collect))
            i += 1

def main():
    player = ""
    roll_control = True
    print("\t\t\tBACKGOMMON GAME \n")
    
    while True:
        choose = isInt(input("1- New game \n2- Continue saved game \n--> "))
        if choose in [1,2]: break
        else:
            print("Invalid choose! You should type 1 or 2")
            continue
    
    if choose == 1: 
        print("NOTE: Type 'save' into any entry to save the game.")
        time.sleep(2)
        createEntities()
        player = rollFirstDices()
    else: 
        roll_control = False
        player, all_dices, dice_arr = getSavedEntities()
    
    while True:
        if roll_control == True:
            all_dices = rollDice(player)
            dice_arr = all_dices.copy()
        
        roll_control = True
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
                    if number == 'save': return ['save', player, all_dices, dice_arr]
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
                
                if moveControl(player, dice_arr) == False and collectControl(player, home_y_axis, dice_arr) == False:
                    print(player, "player passed! Because there are no moves.")
                    break
                
                f = input("From (e.g: E1): ")
                if len(f) < 2:
                    print("{} line is incorrect! (e.g: A5)".format(f))
                    time.sleep(2)
                    continue
            
                c = findChequer(f[0], f[1], player)
                if(f == 'save'): return ['save', player, all_dices, dice_arr]
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
                        if step == 'save': return ['save', player, all_dices, dice_arr]
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
                    is_dice_bigger = len(list(filter(lambda d: d >= home_number, dice_arr))) > 0
                    has_bigger_chequer = False
                    
                    for each in player_home[home_number : ]:
                        home_c = findChequer(each, home_y_axis, player)
                        if home_c != None and home_c.is_collect == False:
                            has_bigger_chequer = True
                            break
                    
                    if (home_number in dice_arr):
                        c.collect(all_lines)
                        dice_arr.remove(home_number)
                    elif (is_dice_bigger == True and has_bigger_chequer == False):
                        c.collect(all_lines)
                        dice_arr.remove(max(dice_arr))
                    else:
                        print("Invalid collect!")
                        time.sleep(1)
                        continue
                    
                    if finishControl(player) == True: return ['finish', player]
                    
                if len(dice_arr) == 0: break
                
            player = changePlayer(player)
            continue
            
            
        # Game Stream
        while True:
            printMap(lines_2D, player)
            
            if moveControl(player, dice_arr) == False:
                print(player, "player passed! Because there are no moves.")
                break
        
            f = input("From (e.g: E1): ")
            if len(f) < 2:
                print("{} line is incorrect! (e.g: A5)".format(f))
                time.sleep(2)
                continue
                
            c = findChequer(f[0], f[1], player)
            if(f == 'save'): return ['save', player, all_dices, dice_arr]
            elif(c == None):
                print("{} chequer is not found for {} player!".format(f, player))
                time.sleep(2)
                continue
        
            while True:
                step = isInt(input("How many steps? {}: ".format(dice_arr)))
                if step == 'save': return ['save', player, all_dices, dice_arr]
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
    
    result = main()
    
    if result[0] == 'finish':
        input("\t\t\t {} PLAYER WON!".format(result[1]))
    elif result[0] == 'save':
        saveGame(result[1], result[2], result[3])
    
                
        
        
        
        
        