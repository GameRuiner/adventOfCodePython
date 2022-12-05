# --- Part 1,2 ---

f = open("input5.txt", "r")
queues = []
for x in f:
    if len(queues) == 0:
        for ch in range(len(x) // 4):
            queues.append([])
    for index, char in enumerate(x): 
        if char == '1':
            break
        if (index - 1) % 4 == 0 and char != ' ':
            column = (index - 1) // 4
            queues[column].append(char)
    if x == "\n":
        break

for x in f: 
    splitted = x.split()
    amount = int(splitted[1])
    fromColumn = int(splitted[3]) - 1
    toColumn = int(splitted[5]) - 1
    toMove = queues[fromColumn][:amount]
    # For Part 1 uncomment this line
    # toMove.reverse()
    del queues[fromColumn][:amount]
    queues[toColumn] = toMove + queues[toColumn]
f.close()

res = ''
for queue in queues:
    res += queue[0]
print(res)
