f = open("inputs/input12.txt", "r")

heightmap = []
startPos = None
endPos = None

currentVertex = 0
zeroHeight = []
for line in f:
    # heightmap.append(list(ord(c) - ord('a') for c in line.strip()))
    row = []
    for i in range(len(line.strip())):
        if line[i] == 'S':
            startPos = currentVertex
            row.append(0)
        elif line[i] == 'E':
            endPos = currentVertex
            row.append(25)
        else:
            row.append(ord(line[i]) - ord('a'))
            if line[i] == 'a':
                zeroHeight.append(currentVertex)
        currentVertex += 1
    heightmap.append(row)
f.close()


rows = len(heightmap)
cols = len(heightmap[0])
vCount = rows*cols
adj = [[] for _ in range(vCount)]

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# dirDL = [(1, 0), (0, 1)]

currentVertex = 0
for i in range(rows):
    for j in range(cols):
        currentHeight = heightmap[i][j]
        for d in dir:
            newPos = (i + d[0], j + d[1])
            destVertex = newPos[0] * cols + newPos[1]
            if (newPos[0] >= 0 and newPos[0] < rows
                    and newPos[1] >= 0 and newPos[1] < cols):
                newHeight = heightmap[newPos[0]][newPos[1]]
                if newHeight <= currentHeight + 1:
                    adj[currentVertex].append(destVertex)
        currentVertex += 1

# for a in adj:
#     print(a)
# print(startPos, endPos, vCount)

dist = [100000 for i in range(vCount)]
pred = [-1 for i in range(vCount)]

# BFS
queue = []
visited = [False for i in range(vCount)]

# visited[startPos] = True
dist[startPos] = 0
for a in zeroHeight:
    queue.append(a)
    dist[a] = 0

def BFS():
    while (len(queue) != 0):
        u = queue.pop(0)
        for av in adj[u]:
            if visited[av] == False:
                visited[av] = True
                dist[av] = min(dist[u] + 1, dist[av])
                pred[av] = u
                queue.append(av)

                if (av == endPos):
                    return True
    return False

BFS()

f = open("inputs/output12.txt", "w")
f.write('')
f.close()
f = open("inputs/output12.txt", "a")

for i in range(len(dist)):
    if i % cols == 0:
        # print()
        f.write('\n')
    # print(dist[i], end=' ')
    f.write(str(dist[i]) + ' ')
print(dist[endPos])
f.close()

