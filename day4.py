def getSet(elf):
    (start, end) = elf.split("-")
    return set(range(int(start), int(end)+1))

# --- Part 1 ---

f = open("input4.txt", "r")
result = 0
for x in f:
    (elf1, elf2) = x.strip().split(",")
    set1 = getSet(elf1)
    set2 = getSet(elf2)
    result += set1.issubset(set2) or set2.issubset(set1)

f.close()
print(result)


# --- Part 2 ---

f = open("input4.txt", "r")
result = 0
for x in f:
    (elf1, elf2) = x.strip().split(",")
    set1 = getSet(elf1)
    set2 = getSet(elf2)
    result += len(set1.intersection(set2)) > 0

f.close()
print(result)