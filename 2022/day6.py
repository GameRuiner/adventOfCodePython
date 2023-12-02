# --- Part 1,2 ---

f = open("inputs/input6.txt", "r")
for line in f:
    marker = []
    index = 1
    for ch in line:
        while ch in marker:
            marker.pop(0)
        marker.append(ch)
        # change if for switching between Part 1 and Part 2
        # if len(marker) == 4:
        if len(marker) == 14:
            print(marker)
            print(index)
            break
        index+=1


f.close()
