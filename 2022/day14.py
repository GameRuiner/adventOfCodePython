f = open("inputs/input14.txt", "r")

minX = 10000
maxX = 0
maxY = 0
lines = []
for line in f:
    points = line.strip().split(' -> ')
    line = []
    for point in points:
        [x, y] = [int(n) for n in point.split(',')]
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y
        line.append([x, y])
    lines.append(line)

# print(minX, maxX, maxY)
width = 1000
maxY += 2

cave = [['.' for _ in range(width)] for _ in range(maxY + 1)]

cave[0][500] = '+'

for i in range(len(cave[maxY])):
    cave[maxY][i] = '#'
# for line in lines:
#     for points in line:
#         points[0] = points[0] - minX

for line in lines:
    [currentX, currentY] = line[0]
    for [x, y] in line:
        if x != currentX:
            for i in range(min(currentX, x), max(currentX, x) + 1):
                cave[y][i] = '#'
        if y != currentY:
            for i in range(min(currentY, y), max(currentY, y) + 1):
                cave[i][x] = '#'
        [currentX, currentY] = [x, y]


sandCount = 0
while True:
    [x, y] = (500, 0)
    while True:
        if cave[y+1][x] == '.':
            y += 1
        elif cave[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif cave[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            cave[y][x] = 'o'
            break
    sandCount += 1
    if (x,y) == (500, 0):
        print(sandCount)
        break

# f = open("inputs/output14.txt", "w")
# for row in cave:
#     # print(''.join(row))
#     f.write(''.join(row) + '\n')
# f.close()
