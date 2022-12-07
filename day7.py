f = open("input7.txt", "r")
fileSystem = {'size': None, 'content': {'/': {'size': None, 'content': {}}}}
currentPass = []

def getCurrentPlace(fileSystem, currentPass):
    currentPlace = fileSystem
    for folder in currentPass:
        currentPlace = currentPlace['content'][folder]
    return currentPlace

for line in f:
    splitted = line.split()
    if splitted[0] == '$':
        if splitted[1] == 'cd':
            if splitted[2] == '..':
                currentPass =  currentPass[:-1]
            else:
                currentPass.append(splitted[2])
        if splitted[1] == 'ls':
            pass
    elif splitted[0] == 'dir':
        currentPlace = getCurrentPlace(fileSystem, currentPass)
        currentPlace['content'][splitted[1]] = {'size': None, 'content': {}}
    else:
        size = int(splitted[0])
        currentPlace = getCurrentPlace(fileSystem, currentPass)
        currentPlace['content'][splitted[1]] = {'size': size}

# print(fileSystem)

resultSum = 0
overkill = 70000000
result2 = 0

def countSize(fs):
    global resultSum
    global result2
    global overkill
    if fs['size']:
        return fs['size']
    else:
        size = 0
        for item in fs['content']:
            size+= countSize(fs['content'][item])
        fs['size'] = size
        # Part 1 if
        if (size <= 100000 and size > 0):
            resultSum+= size
        # Part 2 if
        if (size >= 3313415 and size - 3313415 < overkill):
            result2 = size
            overkill = size - 3313415
        return size

totalSize = countSize(fileSystem)

# print(fileSystem)
# print(resultSum)
print(result2)
print(30000000 - (70000000 - totalSize)) # 3313415 we space we need

f.close()