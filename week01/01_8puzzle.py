class blank:
    def __init__(self, i, j):
        self.i = i
        self.j = j


def swap(a, b):
    return b, a


def misplaced(table):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ct = 0
    for i in range(3):
        for j in range(3):
            if goal[i][j] != table[i][j]:
                ct += 1
    return ct-1


def distanceFormOrgPos(table):
    for i in range(3):
        for j in range(3):
            if table[i][j] != 9:
                return abs(i-orgBlank.i) + abs(j-orgBlank.j)


def swapTable(table, I, J):
    newTable = []
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp.append(table[i][j])
        newTable.append(tmp)
    for i in range(3):
        for j in range(3):
            if newTable[i][j] == 9:
                newTable[i][j], newTable[i+I][j +J] = swap(newTable[i][j], newTable[i+I][j+J])
                return newTable

def findBlank(table):
    for i in range(3):
        for j in range(3):
            if table[i][j] == 9:
                return [i, j]


def printTable(table):
    [[print(table[i][j] if table[i][j]!=9 else "_", end=" ") for j in range(3)] and print()
     for i in range(3)]


# Start the program
print("Input your 8 puzzle")
table = [[int(j) if j != '_' else 9
          for j in input().split(" ")]
         for i in range(3)]

for i in range(3):
    for j in range(3):
        if(table[i][j] == 9):
            orgBlank = blank(i, j)

print("\nStart solving ...\n")
ct = 0
while(misplaced(table) != -1):
    ct+=1
    print(f'\t{ct} time')
    printTable(table)
    print("""------\n""")

    tmp = findBlank(table)
    curBlank = blank(tmp[0], tmp[1])
    up = down = right = left = 1000000
    if(curBlank.i > 0):
        tUp = swapTable(table, -1, 0)
        up = misplaced(tUp) + distanceFormOrgPos(tUp)
    if(curBlank.i < 2):
        tDown = swapTable(table, 1, 0)
        down = misplaced(tDown) + distanceFormOrgPos(tDown)
    if(curBlank.j > 0):
        tLeft = swapTable(table, 0, -1)
        left = misplaced(tLeft) + distanceFormOrgPos(tLeft)
    if(curBlank.j < 2):
        tRight = swapTable(table, 0, 1)
        right = misplaced(tRight) + distanceFormOrgPos(tRight)

    minDirect = min([up, down, right, left])
    # print([up, down, right, left])
    if minDirect == up:
        table = tUp
    elif minDirect == down:
        table = tDown
    elif minDirect == right:
        table = tRight
    elif minDirect == left:
        table = tLeft

print("Solved ...\n")
print(f'\t{ct+1} time')
printTable(table)
