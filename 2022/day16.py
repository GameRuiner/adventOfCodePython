f = open("inputs/input16.txt", "r")

pipes = {}
allPipes = []

totalFlow = 0

for line in f:
    splitted = line.strip().replace(';', '').replace(',', '').split(' ')
    pipe = splitted[1]
    flow = int(splitted[4].split('=')[1])
    other = tuple(splitted[9:])
    totalFlow += flow
    pipes[pipe] = {'name': pipe, 'flow':flow, 'other':other}
    if flow > 0:
        allPipes.append(pipe)

# print(pipes)

def BFS(currentPipe, pipesLeft):
    visited = [currentPipe]
    depth = 0
    queue = [(currentPipe, depth)]
    res = []
    while len(queue) != 0 and len(res) != len(pipesLeft):
        [cPipe, cdepth] = queue.pop(0)
        n_depth = cdepth + 1
        for pipe in pipes[cPipe]['other']:
            if pipe not in visited:
                visited.append(pipe)
                queue.append((pipe, n_depth))
                if pipe in pipesLeft:
                    res.append((pipe, n_depth + 1))
    return res

for pipe in pipes:
   pipes[pipe]['distances'] = BFS(pipe, allPipes)


# def find_pressure(timeLeft, currentPressure, totalPressure, currentPipe, pipesLeft):
#     # print(timeLeft, currentPressure, totalPressure, currentPipe, pipesLeft)
#     if not timeLeft:
#         return totalPressure
#     currentPressure += pipes[currentPipe]['flow']
#     if currentPressure == totalFlow:
#         totalPressure += timeLeft * currentPressure
#         return totalPressure
#     distances = list(filter(lambda x: x[1] in pipesLeft, pipes[currentPipe]['distances']))
#     res = []
#     for [distance, pipeName] in distances:
#         if distance < timeLeft:
#             newTimeLeft = timeLeft - (distance + 1)
#             newTotalPressure = totalPressure + (distance + 1) * currentPressure
#             res.append(find_pressure(newTimeLeft, currentPressure, newTotalPressure, pipeName, list(filter(lambda x: x != pipeName, pipesLeft))))
#     if timeLeft > 0:
#         res.append(totalPressure + currentPressure * timeLeft)

#     # print(distances)
#     return(max(res))

# def find_pressure2(openTime1, openTime2, currentPressure, totalPressure, currentPipe1, currentPipe2, pipesLeft, currentTime):
#     if currentTime > openTime1 and currentTime > openTime2:
#         return(totalPressure + currentPressure * (27 - currentTime))
#     newTime = currentTime + 1
#     newPressure = currentPressure + totalPressure
#     res = []
#     if currentTime == openTime1 and currentTime != openTime2:
#         newTotalPressure = totalPressure + currentPressure
#         currentPressure += pipes[currentPipe1]['flow']
#         distances = list(filter(lambda x: x[1] in pipesLeft, pipes[currentPipe1]['distances']))
#         for [distance, pipeName] in distances:
#             newOpenTime = openTime1 + distance 
#             res.append(find_pressure2(newOpenTime, openTime2, currentPressure, newTotalPressure, pipeName, currentPipe2, list(filter(lambda x: x != pipeName, pipesLeft)), newTime))

#     elif currentTime == openTime2 and currentTime != openTime1:
#         newTotalPressure = totalPressure + currentPressure
#         currentPressure += pipes[currentPipe2]['flow']
#         distances = list(filter(lambda x: x[1] in pipesLeft, pipes[currentPipe2]['distances']))
#         for [distance, pipeName] in distances:
#             newOpenTime2 = openTime2 + distance 
#             res.append(find_pressure2(openTime1, newOpenTime2, currentPressure, newTotalPressure, currentPipe1, pipeName, list(filter(lambda x: x != pipeName, pipesLeft)), newTime))
    
#     elif currentTime == openTime1 and currentTime == openTime2:
#         newTotalPressure = totalPressure + currentPressure
#         currentPressure += pipes[currentPipe1]['flow'] + pipes[currentPipe2]['flow']
#         distances1 = list(filter(lambda x: x[1] in pipesLeft, pipes[currentPipe1]['distances']))
#         distances2 = list(filter(lambda x: x[1] in pipesLeft, pipes[currentPipe2]['distances']))
#         if (len(distances1) == 1):
#             [d1, p1] = distances1[0]
#             [d2, p2] = distances2[0]
#             if d1 < d2:
#                 newOpenTime1 = openTime1 + d1 
#                 res.append(find_pressure2(newOpenTime1, openTime2, currentPressure, newTotalPressure, p1, currentPipe2, [], newTime))
#             else:
#                 newOpenTime2 = openTime2 + d2 
#                 res.append(find_pressure2(openTime1, newOpenTime2, currentPressure, newTotalPressure, currentPipe1, p2, [], newTime))
#         else:
#             for [distance1, pipeName1] in distances1:
#                 for [distance2, pipeName2] in distances2:
#                     if pipeName2 != pipeName1:
#                         newOpenTime1 = openTime1 + distance1 
#                         newOpenTime2 = openTime2 + distance2 
#                         res.append(find_pressure2(newOpenTime1, newOpenTime2, currentPressure, newTotalPressure, pipeName1, pipeName2, list(filter(lambda x: x not in [pipeName1, pipeName2], pipesLeft)), newTime))
#     if newTime < 26:
#         res.append(find_pressure2(openTime1, openTime2, currentPressure, newPressure, currentPipe1, currentPipe2, pipesLeft, newTime))
#     res.append(totalPressure + currentPressure * (26 - newTime))
#     return(max(res))

savedAnswers = {}


def find_pressure3(openers, currentPressure, totalPressure, pipesLeft, currentTime):
    f_print = str(openers) + str(currentPressure) + str(totalPressure) + str(pipesLeft) + str(currentPressure)
    if f_print in savedAnswers:
       return savedAnswers[f_print]
    totalPressure += currentPressure
    if len(openers) == 0:
        return totalPressure + currentPressure * (26 - currentTime)
    if len(openers) == 1:
        [_, pipe] = openers[0]
        currentPressure += pipes[pipe]['flow']
        return totalPressure + currentPressure * (26 - currentTime)
    [time1, pipe1] = openers[0]
    [time2, pipe2] = openers[1]
    res = []
    if time1 == time2:
        if len(pipesLeft) == 0:
            return totalPressure + currentPressure * (26 - currentTime)
        currentPressure += pipes[pipe1]['flow'] + pipes[pipe2]['flow']
        distances1 = list(sorted(filter(lambda x: x[0] in pipesLeft, pipes[pipe1]['distances'])))
        distances2 = list(sorted(filter(lambda x: x[0] in pipesLeft, pipes[pipe2]['distances'])))
        d1s = []
        d2s = []
        for i in range(len(distances1)):
            if distances1[i][1] > distances2[i][1]:
                d2s.append(distances2[i])
            elif distances1[i][1] < distances2[i][1]:
                d1s.append(distances1[i])
            else:
                d2s.append(distances2[i])
                d1s.append(distances1[i])
        if len(d1s) == 0:
            res.append(find_pressure3([(time2 + d2s[0][1], d2s[0][0])], currentPressure, totalPressure + currentPressure * ( time2 + d2s[0][1] - currentTime - 1), list(filter(lambda x: x != d2s[0][0], pipesLeft)), time2 + d2s[0][1]))
        if len(d2s) == 0:
            res.append(find_pressure3([(time1 + d1s[0][1], d1s[0][0])], currentPressure, totalPressure + currentPressure * ( time1 + d1s[0][1] - currentTime - 1), list(filter(lambda x: x != d1s[0][0], pipesLeft)), time1 + d1s[0][1]))
        openersL = []
        for [p1, d1] in d1s:
            for [p2, d2] in d2s:
                if p1 != p2 or (len(d1s) == len(d2s) == 1):
                    newO = tuple(sorted([(time1 + d1, p1), (time2 + d2, p2)]))
                    if newO not in openersL:
                        openersL.append(newO)
        for op in openersL:
            res.append(find_pressure3(op, currentPressure, totalPressure + currentPressure * (op[0][0] - currentTime - 1), list(filter(lambda x: x not in [op[0][1], op[1][1]], pipesLeft)), op[0][0]))
                       
    else:
        currentPressure += pipes[pipe1]['flow']
        if len(pipesLeft) == 0:
            res.append(find_pressure3([(time2, pipe2)], currentPressure, totalPressure + currentPressure * (time2 - currentTime - 1), [], time2))
        else:
            distances1 = list(sorted(filter(lambda x: x[0] in pipesLeft, pipes[pipe1]['distances'])))
            for [p1, d1] in distances1:
                openers = sorted([(time1 + d1, p1), (time2, pipe2)])
                res.append(find_pressure3(openers, currentPressure, totalPressure + currentPressure * (openers[0][0] - currentTime - 1), list(filter(lambda x: x != p1, pipesLeft)), openers[0][0]))
    if len(res) == 0:
        print(openers, currentPressure, totalPressure, pipesLeft, currentTime)
    ret_res = max(res)
    savedAnswers[f_print] = ret_res
    return ret_res


# distances = BFS('AA', allPipes)
# for p in pipes:
#     print(pipes[p]['name'], pipes[p]['distances'])
# print(pipes)
# variants = []
# for [d,pipe] in distances:
#     if d < 30:
#         variants.append(find_pressure(30 - (d + 1), 0, 0, pipe, list(filter(lambda x: x != pipe, allPipes))))
# for [d1,pipe1] in distances:
#     for [d2,pipe2] in distances:
#         if pipe1 != pipe2:
#             variants.append(find_pressure2(d1, d2, 0, 0, pipe1, pipe2, list(filter(lambda x: x not in [pipe1, pipe2], allPipes)), 1))
print(len(allPipes), allPipes)
print(find_pressure3([(0, 'AA'), (0, 'AA')], 0, 0, allPipes, 1))


# print(max(variants))
