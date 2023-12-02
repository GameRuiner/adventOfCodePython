f = open("inputs/input15.txt", "r")

# checkLine = 2000000

# lineCover = []
beacons = []
points = []
for line in f:
    spaceSplitted = line.strip().replace(',', '').replace(':', '').split(' ')
    def getNum(x): return int(x.split('=')[1])
    sX = getNum(spaceSplitted[2])
    sY = getNum(spaceSplitted[3])
    bX = getNum(spaceSplitted[8])
    bY = getNum(spaceSplitted[9])
    distance = abs(sX - bX) + abs(sY - bY)
    points.append((sX, sY, distance))
    # if bY == checkLine:
    #     if not beacons.count((bX, bY)):
    #         beacons.append((bX, bY))
for i in range(0, 4000001):
    checkLine = i
    lineCover = []
    for (sX, sY, distance) in points:
        distanceToCheckLine = abs(sY - checkLine)
        if distance >= distanceToCheckLine:
            halfWidth = distance - distanceToCheckLine
            start = sX - halfWidth
            end = sX + halfWidth
            affectedPoints = [(start, end)]
            otherPoints = []
            for (cS, cE) in lineCover:
                if (cS <= start and start <= cE
                        or cS <= end and end <= cE
                        or cS > start and end > cE):
                    affectedPoints.append((cS, cE))
                else:
                    otherPoints.append((cS, cE))
            minStart = affectedPoints[0][0]
            maxEnd = affectedPoints[0][1]
            for (cS, cE) in affectedPoints:
                if (cS < minStart):
                    minStart = cS
                if (cE > maxEnd):
                    maxEnd = cE
            otherPoints.append((minStart, maxEnd))
            lineCover = otherPoints
    # if (len(lineCover) == 2 and lineCover[0][1] + 1 != lineCover[1][0]):
    #     print(lineCover[0][1] + 1, checkLine)
    if (lineCover[0][0] >= 0 or lineCover[0][1] <= 400000):
        print(lineCover, checkLine)
# positionsCount = 0
# print(lineCover)
# for (s, e) in lineCover:
#     positionsCount += (e - s) + 1
# print(beacons, positionsCount - len(beacons))
