def hasOneToNine(string):
    count=0
    for x in range (1,10):
        if (not (str(x) in string)):
            return False
    return True

def isImpossible(grid):
    for row in range (9):
        for col in range (9):
            if (grid[row][col]=='' or grid[row][col]==None):
                return True
    return False

def isValidSolution(grid):
    count=0
    for row in range (9):
        for col in range (9):
            if (len(grid[row][col])==1):
                count+=1
    if (count<81):
        return False

    for row in range (0,9,3):
        for col in range (0,9,3):
            if (not hasOneToNine(grid[row][col]+testQuadrant(grid,row,col))):
                return False

    for row in range (9):
        if (not hasOneToNine(grid[row][0]+testRow(grid,row,0))):
            return False

    for col in range (9):
        if (not hasOneToNine(grid[0][col]+testCol(grid,0,col))):
            return False

    return True

def testQuadrant(grid,y,x):
    retarray=[]
    for row in range((y//3)*3,(y//3)*3+3):
        for col in range((x//3)*3,(x//3)*3+3):
            if (len(grid[row][col])==1 and not (row==y and col==x)):
                retarray.append(grid[row][col])
    return "".join(retarray)

def testRow(grid,y,x):
    row=y
    retarray=[]
    for col in range(9):
        if (len(grid[row][col])==1 and not (row==y and col==x)):
            retarray.append(grid[row][col])
    return "".join(retarray)

def testCol(grid,y,x):
    col=x
    retarray=[]
    for row in range(9):
        if (len(grid[row][col])==1 and not (row==y and col==x)):
            retarray.append(grid[row][col])
    return "".join(retarray)

def remNum(remVals,retVals):
    retArray=[]
    for ch in retVals:
        if (not ch in remVals):
            retArray.append(ch)
    return "".join(retArray)

def replaceZeros(grid):
    for y in range (9):
        for x in range (9):
            if (grid[y][x]=="0"):
                grid[y][x]="123456789"
    return grid

def setString(grid):
    for row in range (9):
        for col in range (9):
            grid[row][col]=str(grid[row][col])
    return grid

def printGrid(grid):
    for row in range (9):
        if ((row)%3==0):
            if (row==0):
                print ("-------------------")
            else:
                print ("|-----|-----|-----|")
        for col in range(9):
            if ((col)%3==0):
                print ("|", end="")
            else:
                print (" ", end="")
            if (len(grid[row][col])==1):
                print (grid[row][col], end = "")
            else:
                print("0", end = "")
        print("|")
    print ("-------------------")
def tempPrintGrid(grid):
    for row in range (9):
        print (grid[row])

def findSingleNum(array):
    allnum=[]
    for string in array:
        for ch in string:
            allnum.append(ch)
    joined="".join(allnum)
    for x in range (1,10):
        if (joined.count(str(x))==1):
            return str(x)
    return None

def findIndex(array, num):
    for x in range (9):
        if (num in array[x]):
            return x

def checkByPossibilities(grid):
    for row in range (9):
        possibilities=[]
        for col in range (9):
            if (not len(grid[row][col])==1):
                possibilities.append(grid[row][col])
        if (len(possibilities)>1):
            num=findSingleNum(possibilities)
            if (num!=None):
                grid[row][findIndex(grid[row],num)]=num
                grid=checkByRules(grid)

    for col in range (9):
        possibilities=[]
        temp=[]
        for row in range (9):
            temp.append(grid[row][col])
            if (not len(grid[row][col])==1):
                possibilities.append(grid[row][col])

        if (len(possibilities)>1):
            num=findSingleNum(possibilities)
            if (num!=None):
                grid[findIndex(temp,num)][col]=num
                grid=checkByRules(grid)

    for row in range (0,9,3):
        for col in range (0,9,3):
            possibilities=[]
            temp=[]
            for qrow in range (row,row+3):
                for qcol in range (col,col+3):
                    temp.append(grid[qrow][qcol])
                    if (not len(grid[qrow][qcol])==1):
                        possibilities.append(grid[qrow][qcol])
            if (len(possibilities)>1):
                num=findSingleNum(possibilities)
                if (num!=None):
                    ind=findIndex(temp,num)
                    grid[row+(ind//3)][col+(ind%3)]=num
                    grid=checkByRules(grid)

    return grid


def checkByRules(grid):
    count=0
    temp=0
    for blah in range (1000):

        count=0
        for y in range (9):
            for x in range (9):
                if (len(grid[y][x])==1):
                    count+=1
                    continue
                grid[y][x]=remNum(testQuadrant(grid,y,x), grid[y][x])
                grid[y][x]=remNum(testRow(grid,y,x), grid[y][x])
                grid[y][x]=remNum(testCol(grid,y,x), grid[y][x])

        if (count==81 or count==temp):

            break
        temp=count
    return grid


def createTempGrid(grid):
    tempgrid=[]
    for row in range (9):
        temp=[]
        for col in range (9):
            temp.append(grid[row][col])
        tempgrid.append(temp)
    return tempgrid


def testTheoretical(grid,depth):
    tempgrid=[]
    #printGrid(grid)
    #input("")
    for row in range (9):
        for col in range (9):
            if (not len(grid[row][col])==1):
                for ind in range(len(grid[row][col])):
                    tempgrid=createTempGrid(grid)
                    tempgrid[row][col]=grid[row][col][ind]
                    tempgrid=checkByRules(tempgrid)
                    tempgrid=checkByPossibilities(tempgrid)


                    if (not isImpossible(tempgrid)):
                        if (isValidSolution(tempgrid)):
                            return tempgrid
                        else:
                            print ("Recursion", "Depth:", depth, "Row/col", row, col)
                            tempgrid=testTheoretical(tempgrid, depth+1)

                return tempgrid
    return grid

def main(grid):
    grid=setString(grid)
    printGrid(grid)
    grid=replaceZeros(grid)
    #while(not isValidSolution(grid)):
    for x in range (3):
        grid=checkByRules(grid)
        grid=checkByPossibilities(grid)
    grid=testTheoretical(grid, 0)
    print (isValidSolution(grid))
    printGrid(grid)
    return grid

def solve(grid):
    grid=setString(grid)
    grid=replaceZeros(grid)
    for x in range (3):
        grid=checkByRules(grid)
        grid=checkByPossibilities(grid)
    grid=testTheoretical(grid, 0)
    if isValidSolution(grid):
        return grid
    else:
        return None


def run(grid):
    grid=[]
    for x in range (9):
        array=str(input("enter values: "))
        grid.append(array)

    while (True):
        count=0
        for row in range(len(grid)):
            if (len(grid[row])!=9):
                print ("Row",(row+1), "has", len(grid[row]), "numbers, please re-write it to have 9 numbers.")
                grid[row]=input ("Row "+str(row+1)+": ")
            else:
                count+=1
        if (count==9):
            break
    temp=[]
    retgrid=[]
    for string in grid:
        for ch in string.strip():
            temp.append(ch)
        retgrid.append(temp)
    printGrid(retgrid)


samplegrid1=[[5,3,0,0,7,0,0,0,0],
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,0],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9]]

samplegrid2=[[0,5,9,0,3,0,0,0,0],
             [0,4,0,0,0,0,0,0,7],
             [7,8,0,0,4,0,0,0,0],
             [5,0,0,0,0,0,0,9,0],
             [0,0,2,9,0,0,7,0,0],
             [0,0,0,0,1,6,0,2,0],
             [0,0,0,1,0,0,0,6,3],
             [3,7,0,0,0,0,8,0,0],
             [6,0,0,5,9,0,0,0,0]]


samplegrid3=[[1,0,0,4,0,0,5,2,0],
             [3,0,6,0,0,2,0,0,4],
             [0,0,4,0,0,0,1,0,0],
             [0,0,0,0,0,7,0,0,1],
             [0,3,0,2,0,1,0,5,0],
             [8,0,0,6,0,0,0,0,0],
             [0,0,1,0,0,0,6,0,0],
             [5,0,0,3,0,0,7,0,8],
             [0,4,3,0,0,8,0,0,2]]

samplegrid4=[[1,0,0,0,0,0,0,0,9],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,1,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,2,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,4,0,0,0,0,0]]

samplegrid5=[[0,0,4,0,6,0,0,0,2],
             [8,0,5,0,0,2,0,3,0],
             [0,0,0,0,3,0,0,6,0],
             [0,2,8,0,0,0,0,0,0],
             [0,0,0,0,0,4,0,0,0],
             [7,0,0,0,5,0,0,0,9],
             [0,0,2,0,0,1,0,0,0],
             [0,7,0,0,4,0,9,5,0],
             [6,0,0,0,0,0,0,4,0]]

samplegrid6=[[0,0,2,0,0,0,0,4,0],
             [0,0,0,0,3,0,0,0,0],
             [7,0,5,0,9,0,0,0,0],
             [0,0,0,9,0,7,0,0,0],
             [0,0,0,0,0,2,0,0,8],
             [0,0,9,0,0,5,6,0,3],
             [4,0,0,5,0,0,3,1,0],
             [0,9,0,0,0,0,0,0,0],
             [0,8,0,0,4,0,2,0,6]]

if __name__ == "__main__":
    main(samplegrid5)
