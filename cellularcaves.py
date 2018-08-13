import sys
import random

def printGrid(grid, wallChar, emptyChar):
    finalstr = ""
    finalstr += "\n"
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i]==1:
                finalstr += wallChar
            else:
                finalstr += emptyChar
        finalstr += "\n"
    finalstr += "\n"
    print(finalstr)

def makeGrid(width, height):
    newgrid = [[0 for x in range(height)] for y in range(width)]
    for i in range(len(newgrid)):
        for j in range(len(newgrid[i])):
            if i==0 or j==0 or i==len(newgrid)-1 or j==len(newgrid[0])-1:
                newgrid[i][j]=1
    return newgrid

def populateGrid(grid, chance):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if(random.randint(0,100)<=chance):
                grid[i][j]=1
    return grid

def automataIteration(grid, minCount, makePillars):
    new_grid = [row[:] for row in grid]
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            count = 0
            for k in range(-1,2):
                for l in range(-1,2):
                    if grid[i+k][j+l]==1:
                        count+=1
            if count>=minCount or (count==0 and makePillars==1):
                new_grid[i][j]=1
            else:
                new_grid[i][j]=0
    return new_grid

def main():
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    #chance = 100 - int(input("Enter the percentage chance of randomly generating a wall: "))
    #count = int(input("Enter the min count of surrounding walls for the automata rules: "))
    chance = 40
    count = 5
    iterations = int(input("Enter the number of regular iterations: "))
    pillarIterations = int(input("Enter the number of pillar-generating iterations: "))

    grid = makeGrid(width, height)
    
    print("\nRandomly populated grid:")
    grid = populateGrid(grid, chance)
    printGrid(grid, '# ', '· ')

    for i in range(pillarIterations):
        print("{0} iteration(s) of automata with pillars:".format(i+1))
        grid = automataIteration(grid, count, 1)
        printGrid(grid, '# ', '· ')

    for i in range(iterations):
        print("{0} iteration(s) of regular automata:".format(i+1))
        grid = automataIteration(grid, count, 0)
        printGrid(grid, '# ', '· ')

    print("")
    main()
    

if __name__ == "__main__":
    main()
