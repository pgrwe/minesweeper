
import random


def display(grid):
    label = 0
    print("    0   1   2   3   4   5   6   7   8   9\n  -----------------------------------------")
    for i in grid:
        print(label, end=" | ")
        print(" | ".join(str(cell) for cell in i),end=" |\n  -----------------------------------------")
        print()
        label+=1
    

def checkwin(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                return False
    return True


def minesweeper():
    
    grid = [[0 for r in range(10)] for c in range(10)]
    vGrid = [[" " for r in range(10)] for c in range(10)]
    

    # making/placing mines
    minelist = []
    for x in range(10):
        for y in range(10):
            minelist.append((x,y))
    
    for n in range(20):
        mineloc = random.choice(minelist)
        minelist.remove(mineloc)
        x,y = mineloc 
        grid[y][x] = "X"
        # print(mineloc)
        try:
            #below
            if grid[y+1][x] == "X":
                pass
            else:
                grid[y+1][x]+=1 

            #bottom right 
            if grid[y+1][x+1] == "X":
                pass
            else:
                grid[y+1][x+1]+=1 

            #right
            if grid[y][x+1] == "X":
                pass
            else:
                grid[y][x+1]+=1 

            #topright
            if grid[y-1][x+1] == "X":
                pass
            elif y-1 < 0:
                pass
            else:
                grid[y-1][x+1]+=1 

            #above
            if grid[y-1][x] == "X":
                pass
            elif y-1 < 0:
                pass
            else:
                grid[y-1][x]+=1 
            
            #topleft
            if grid[y-1][x-1] == "X":
                pass
            elif y-1 < 0 or x-1 < 0:
                pass
            else:   
                grid[y-1][x-1]+=1 

            #left
            if grid[y][x-1] == "X":
                pass
            elif x-1 < 0:
                pass
            else:
                grid[y][x-1]+=1 

            #bottomleft
            if grid[y+1][x-1] == "X":
                pass
            elif x-1 < 0:
                pass
            else:
                grid[y+1][x-1]+=1

        except IndexError:
            # if the mine is at the bottom rung
            if y+1 > 9 and x+1 < 9: 
                if grid[y][x+1] == "X":
                    pass
                else:
                    grid[y][x+1]+=1 #right
                
                if grid[y-1][x+1] == "X":
                    pass
                else:
                    grid[y-1][x+1]+=1 #topright
                
                if grid[y-1][x] == "X":
                    pass
                else:
                    grid[y-1][x]+=1 #above
                
                if grid[y-1][x-1] == "X":
                    pass
                else:
                    grid[y-1][x-1]+=1 #topleft
                
                if grid[y][x-1] == "X":
                    pass
                else:
                    grid[y][x-1]+=1 #left
               
            #if the mine is at the right wall
            if x+1 > 9 and (y-1 > 0 and y-1 < 8):
                if grid[y][x-1] == "X":
                    pass
                else:
                    grid[y][x-1]+=1 #left
                
                if grid[y-1][x-1] == "X":
                    pass
                else:
                    grid[y-1][x-1]+=1 #topleft
                
                if grid[y-1][x] == "X":
                    pass
                else:
                    grid[y-1][x]+=1 #above

                if grid[y+1][x-1] == "X":
                    pass
                else:
                    grid[y+1][x-1]+=1 #bottomleft
                
            #bottom right corner mine 
            if x+1 > 9 and y+1 > 9:
                if grid[y-1][x] == "X":
                    pass
                else:
                    grid[y-1][x]+=1 #above

                if grid[y-1][x-1] == "X":
                    pass
                else:
                    grid[y-1][x-1]+=1 #topleft
                
                if grid[y][x-1] == "X":
                    pass
                else:
                    grid[y][x-1]+=1 #left
            
            #top right corner mine
            if x+1 > 9 and y-1 < 0:
                if grid[y][x-1] == "X":
                    pass
                else:
                    grid[y][x-1]+=1 #left
                if grid[y+1][x-1] == "X":
                    pass
                else:
                    grid[y+1][x-1]+=1 #bottomleft

            #bottom left corner mine
            if x-1 < 0 and y+1 > 9:
                #-1 for left
                if grid[y][x-1] == "X":
                    pass
                else:
                    grid[y][x-1]-=1
                #-1 for topleft
                if grid[y-1][x-1] == "X":
                    pass
                else:
                    grid[y-1][x-1]-=1 
    #print(minelist)
    display(grid)
    display(vGrid)
    print("In order to win you have to flag each mine and reveal each non-mine space, good luck!")

    
    run = True
    if run == True:
        game = True
        while game:
            try:
                flagyn = input("Press enter to reveal a location, or enter F to place a flag: ")
                xchoice = int(input("Please enter a x location: "))              
                ychoice = int(input("Please enter a y location: "))
            except ValueError:
                xchoice = int(input("Please enter a x location (remember to enter a number!): "))              
                ychoice = int(input("Please enter a y location (remember to enter a number!): "))

            if flagyn == "F" or flagyn == "f":
                vGrid[ychoice][xchoice]  = "F"
                if checkwin(vGrid) == True:
                    print("Congrats you won!")
                    break

            else: 
                vGrid[ychoice][xchoice] = grid[ychoice][xchoice]
                if grid[ychoice][xchoice] == "X":
                    print("Whoops! The location you selected had a bomb, gameover!")
                    break
                elif checkwin(vGrid) == True:
                    print("Congrats you won!")
                    break
            # print(checkwin(grid))
            
            display(vGrid)


        

        
        
minesweeper()
    
