import copy
start = [[1,2,3],[8,0,4],[7,6,5]]
goal = [[2,0,3], [1,8,4],[7,6,5]]
visited = []

def compare(curr):
    return curr==goal
def blankTile(curr):
    for i in range(len(curr)):
        for j in range(len(curr[0])):
            if (curr[i][j]==0):
                return ([i,j])
def up(curr):
    pos=blankTile(curr)
    i=pos[0]
    j=pos[1]
    if (i == 0):
        return curr
    else:
        temp=copy.deepcopy(curr)
        temp[i][j],temp[i-1][j] = temp[i-1][j],temp[i][j]
        return temp
def down(curr):
    pos=blankTile(curr)
    i=pos[0]
    j=pos[1]
    if (i == len(curr)-1):
        return curr
    else:
        temp=copy.deepcopy(curr)
        temp[i][j],temp[i+1][j] = temp[i+1][j],temp[i][j]
        return temp
def left(curr):
    pos=blankTile(curr)
    i=pos[0]
    j=pos[1]
    if (j == 0):
        return curr
    else:
        temp=copy.deepcopy(curr)
        temp[i][j],temp[i][j-1] = temp[i][j-1],temp[i][j]
        return temp
def right(curr):
    pos=blankTile(curr)
    i=pos[0]
    j=pos[1]
    if (j == len(curr[0])-1):
        return curr
    else:
        temp=copy.deepcopy(curr)
        temp[i][j],temp[i][j+1] = temp[i][j+1],temp[i][j]
        return temp

def misplaced(s):
    count=0
    for i in range(len(s)):
        for j in range(len(s[0])):
           if(s[i][j]!=goal[i][j]):
               count+=1
    return count
def getStates(curr):
    states = []
    states.append(up(curr))
    states.append(down(curr))
    states.append(left(curr))
    states.append(right(curr))

    arr = []
    for i in states:
        if (i not in visited):
            arr.append(i)

    if(len(arr)==0):
        return -1
    return min(arr)

    heuristic = []
    for state in arr:
        heuristic.append(misplaced(state))
    ind=heurisic.index(min(heuristic))

    return(arr[ind])

def display(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end = " ")
        print()
    print()
def EightPuzzle(curr):
    global steps
    steps = 0
    if (curr == goal):
        return curr
    else:
        while(compare(curr)==0):
            steps+=1
            display(curr)
            visited.append(curr)

            curr = getStates(curr)
            if (curr == -1):
                return "no solution"
        return curr

display(EightPuzzle(start))
print("The total number of steps are: ",steps)

'''End of program'''
