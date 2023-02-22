import random


def display(grid,diff):
    label = 0
    print("     ", end = "")
    for i in range(0,diff):
             print(f"{i}   ", end="")
    #print("    0   1   2   3   4   5   6   7   8   9\n  -----------------------------------------")
    print("")
    if diff < 5:
        line = diff*"----"
    else:
        line = diff*"----"
    for i in grid:
        print(label, end="  | ")
        print(" | ".join(str(cell) for cell in i),end=f" |\n   {line}\n")
        label+=1
    

def checkwin(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == " ":
                return False
    return True

def checkflags(grid):
    flags = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "F":
                flags+=1
                
    return flags

def depthfirst(vGrid,grid,ystart,xstart,diff):
    #bounds
    if ystart < 0 or ystart > diff or xstart < 0 or xstart > diff:
        return
    if vGrid[ystart][xstart]!= " ":
        return
    if grid[ystart][xstart] == "X":
        return
    if grid[ystart][xstart] != 0:
        vGrid[ystart][xstart] = grid[ystart][xstart] 
        return

    
    vGrid[ystart][xstart] = grid[ystart][xstart] 
    #recursion above
    depthfirst(vGrid,grid,ystart-1,xstart,diff)
    #recursion below
    depthfirst(vGrid,grid,ystart+1,xstart,diff)
    #recursion left
    depthfirst(vGrid,grid,ystart,xstart-1,diff)
    #recursion right
    depthfirst(vGrid,grid,ystart,xstart+1,diff)
    # #recursion topleft
    # depthfirst(vGrid,grid,ystart-1,xstart-1,diff)
    # #recursion topright
    # depthfirst(vGrid,grid,ystart-1,xstart+1,diff)
    # #recursion bottomleft
    # depthfirst(vGrid,grid,ystart+1,xstart-1,diff)
    # #recursion bottomright
    # depthfirst(vGrid,grid,ystart+1,xstart+1,diff)

    
    


    
    

    
    



def minesweeper():

    diff = 5
    rungs = diff-1 
    mines = rungs*2 - 2
    grid = [[0 for r in range(diff)] for c in range(diff)]
    vGrid = [[" " for r in range(diff)] for c in range(diff)]
    

    # making/placing mines
    minelist = []
    for x in range(diff):
        for y in range(diff):
            minelist.append((x,y))
    
    for n in range(mines):
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
            if y+1 > rungs and x+1 <= rungs:
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
             #bottom right corner mine 
            if y+1 > rungs and x+1 > rungs:
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
            if x+1 > rungs and y-1 > 0 and y < rungs:
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
                
            
            #top right corner mine
            if x+1 > rungs and y-1 < 0:
                if grid[y][x-1] == "X":
                    pass
                else:
                    grid[y][x-1]+=1 #left
                if grid[y+1][x-1] == "X":
                    pass
                else:
                    grid[y+1][x-1]+=1 #bottomleft

            #bottom left corner mine
            if x-1 < 0 and y+1 > rungs:
                #above
                if grid[y-1][x] == "X":
                    pass
                else:
                    grid[y-1][x]+=1
                #topright
                if grid[y-1][x+1] == "X":
                    pass
                else:
                    grid[y-1][x+1]+=1 
                #right
                if grid[y][x+1] == "X":
                    pass
                else:
                    grid[y][x+1]+=1
            
   
    display(grid,diff)
    display(vGrid,diff)
    print("VISUAL MODE")
    print(f"In order to win you have to flag each mine and reveal each non-mine space, good luck!\nThere are {mines} bombs:\nYou have {mines} flags:")
    run = True
    if run == True:
        game = True
        while game:
            try:
                select = True
                while select:
                    if checkflags(vGrid) == 20:
                        flagyn = input("Out of flags, replace a flagged location or continue: ")
                        hasFlags = False
                    else:
                        flagyn = input("Press enter to reveal a location, or enter F to place a flag: ")
                        hasFlags = True
                    if flagyn == "F" or flagyn == "f" and hasFlags == True:
                        print("FLAG MODE: ")
                        xchoice = int(input("Please enter a x location: "))              
                        ychoice = int(input("Please enter a y location: "))
                    else:
                        print("SELECTION MODE: ")
                        xchoice = int(input("Please enter a x location: "))              
                        ychoice = int(input("Please enter a y location: "))
                    select = False
            except ValueError:
                select = True

                
            if select == False:
                if flagyn == "F" or flagyn == "f" and hasFlags == True:
                    vGrid[ychoice][xchoice]  = "F"
                    if checkwin(vGrid) == True:
                        print("Congrats you won!")
                        break

                else: 
                    if grid[ychoice][xchoice] == 0:
                        depthfirst(vGrid,grid,ychoice,xchoice,diff-1)
                    else:
                        vGrid[ychoice][xchoice] = grid[ychoice][xchoice]
                    if grid[ychoice][xchoice] == "X":
                        print("Whoops! The location you selected had a bomb, gameover!")
                        break
                    elif checkwin(vGrid) == True:
                        display(vGrid,diff)
                        print("Congrats you won!")
                        break
                # print(checkwin(grid))
            
            display(vGrid,diff)
    display(grid,diff)

    


        

        
        
minesweeper()

    
