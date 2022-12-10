f = open("inputs/input8.txt", "r")
# f = open("inputs/input8test.txt", "r")

forest = []
for line in f:
    forest.append(list(line.strip()))

visible = 0
maxScore = 0
for row in range(len(forest)):
    for column in range(len(forest[row])):
        # if row == 0 or column == 0 or row == len(forest) - 1 or column == len(forest[row]) - 1:
        #     visible += 1
        #     continue
        currentTree = forest[row][column]

        top = False
        topValue = 0
        rowCheck = row - 1
        while rowCheck >= 0:
            topValue += 1
            if forest[rowCheck][column] >= currentTree:
                top = True
                break
            rowCheck -= 1   
        # if not top:
        #     visible += 1
        #     continue

        bottom = False
        bottomValue = 0
        rowCheck = row + 1
        while rowCheck < len(forest):
            bottomValue += 1
            if forest[rowCheck][column] >= currentTree:
                bottom = True
                break
            rowCheck += 1
        # if not bottom:
        #     visible += 1
        #     continue

        right = False
        rightValue = 0
        columnCheck = column + 1
        while columnCheck < len(forest[row]):
            rightValue += 1
            if forest[row][columnCheck] >= currentTree:
                right = True
                break
            columnCheck += 1 
        # if not right:
        #     visible += 1
        #     continue

        left = False
        columnCheck = column - 1
        leftValue = 0
        while columnCheck >= 0:
            leftValue += 1
            if forest[row][columnCheck] >= currentTree:
                left = True
                break
            columnCheck -= 1
        # if not left:
        #     visible += 1
        #     continue

        # -- Part 2 --
        currentScore = topValue * bottomValue * leftValue * rightValue
        # print(f'({row},{column}) {topValue} {bottomValue} {leftValue} {rightValue} score {currentScore}')
        maxScore = max(currentScore, maxScore)
    
# print(visible)
print(maxScore)

f.close()