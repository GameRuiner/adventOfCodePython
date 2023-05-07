def checkPair(l1, l2):
    # print(l1, l2)
    if type(l1) == type(l2) == int:
        # print('both int', l1, l2)
        if l1 < l2:
            return True
        if l1 > l2:
            return False
        return None
    if type(l1) == type(l2) == list:
        # print('both lists', l1, l2)
        if len(l1) == len(l2) == 0:
            return None
        if len(l1) == 0:
            return True
        if len(l2) == 0:
            return False
        res = checkPair(l1.pop(0), l2.pop(0))
        if res == None:
            return checkPair(l1, l2)
        return res
    if type(l1) == int:
        return checkPair([l1], l2)
    if type(l2) == int:
        # print('l2 is int', l2)
        return checkPair(l1, [l2])
    # print('none match', l1, l2)


# print(checkPair([[1], [2, 3, 4]],
#                 [[1], 4]))

# f = open("inputs/input13test.txt", "r")
# goodLinesIndexes = []
# lines = []
# pairNumber = 1
# for line in f:
#     if (line == '\n'):
#         [l1, l2] = lines
#         isPairGood = checkPair(l1, l2)
#         if (isPairGood == None):
#             print(pairNumber)
#         if (isPairGood):
#             goodLinesIndexes.append(pairNumber)
#         pairNumber += 1
#         lines = []
#     else:
#         lines.append(eval(line))
# f.close()
# print(goodLinesIndexes)
# print(sum(goodLinesIndexes))

import functools

f = open("inputs/input13.txt", "r")

allLines = ['[[2]]', '[[6]]']
for line in f:
    if line != '\n':
        allLines.append(line.strip())
valuesMapper = {
    False: 1,
    True: -1,
    None: 0
}       

f.close()
sortedLines = sorted(allLines, key=functools.cmp_to_key(lambda x, y: valuesMapper[checkPair(eval(x), eval(y))]))

for i in range(len(sortedLines)):
    if sortedLines[i] == '[[2]]' or sortedLines[i] == '[[6]]':
        print(i+1)


# print(allLines)