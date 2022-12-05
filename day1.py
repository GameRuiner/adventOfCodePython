# Part one
f = open("input1.txt", "r")
maxCalories = 0
currentCalories = 0
for x in f:
    if x == "\n":
        if currentCalories > maxCalories:
            maxCalories = currentCalories
        currentCalories = 0
    else:
      currentCalories+= int(x)

f.close()
print(maxCalories)


# Part two

f = open("input1.txt", "r")
maxCalories = [0,0,0]
minValue = 0
minValueIndex = 0
currentCalories = 0
for x in f:
    if x == "\n":
        if currentCalories > minValue:
            maxCalories[minValueIndex] = currentCalories
            minValue = min(maxCalories)
            minValueIndex = maxCalories.index(minValue)
        currentCalories = 0
    else:
      currentCalories+= int(x)

f.close()
print(sum(maxCalories))