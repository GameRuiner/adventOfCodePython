import string

priorities = {}
for index, letter in enumerate(string.ascii_lowercase):
   priorities[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
   priorities[letter] = index + 27


# --- Part 1 ---

f = open("input3.txt", "r")
result = 0
for x in f:
    rucksack = list(x.strip())
    middle = len(rucksack)//2
    compartments1 = rucksack[middle:]
    compartments2 = set(rucksack[:middle])
    for item in compartments1:
        if item in compartments2:
            result+= priorities[item]
            break

f.close()
print(result)

# -- Part 2 ---

f = open("input3.txt", "r")
result = 0
groupCounter = 0
group = []
for x in f:
    rucksack = set(x.strip())
    if groupCounter == 2:
        groupCounter = 0
        common = group[0].intersection(group[1]).intersection(rucksack).pop()
        result += priorities[common]
        group = []
    else:
        group.append(rucksack)
        groupCounter +=1
f.close()
print(result)