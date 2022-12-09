f = open("inputs/input9.txt", "r")
# f = open("inputs/input9test2.txt", "r")

HPos = (0,0)
TPos = (0,0)
positions = set([(TPos)])

def makeMove(currentPos, direction):
    if direction == 'U':
        return (currentPos[0], currentPos[1] - 1)
    if direction == 'D':
        return (currentPos[0], currentPos[1] + 1)
    if direction == 'R':
        return (currentPos[0] + 1, currentPos[1])
    if direction == 'L':
        return (currentPos[0] - 1, currentPos[1])

def isTouching(HPos, TPos):
    return abs(HPos[0] - TPos[0]) < 2 and abs(HPos[1] - TPos[1]) < 2

def moveCloser(HPos, TPos):
    x = TPos[0]
    if HPos[0] > TPos[0]:
        x += 1 
    if HPos[0] < TPos[0]:
        x -= 1
    y = TPos[1] 
    if HPos[1] > TPos[1]:
        y += 1 
    if HPos[1] < TPos[1]:
        y -= 1
    return (x, y) 

# -- Part 1 --

# for move in f:
#     (direction, amount) = move.split()
#     for i in range(int(amount)):
#         HPos = makeMove(HPos, direction)
#         if not isTouching(HPos, TPos):
#             TPos = moveCloser(HPos, TPos)
#             positions.add(TPos)

# print(len(positions))

# -- Part 2 --

poss = []
for i in range(10):
    poss.append((0,0))

positions2 = set([poss[-1]])

for move in f:
    (direction, amount) = move.split()
    for i in range(int(amount)):
        poss[0] = makeMove(poss[0], direction)
        currentPos = 0
        while currentPos + 1 != len(poss) and not isTouching(poss[currentPos], poss[currentPos+1]):
            poss[currentPos+1] = moveCloser(poss[currentPos], poss[currentPos+1])
            currentPos += 1
            if currentPos == len(poss) - 1:
                positions2.add(poss[currentPos])

print(len(positions2))