f = open("inputs/input2.txt", "r")

# --- Part 1 ---

# A X Rock
# B Y Paper
# C Z Scissors
points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
resultPoints = {
    "won": 6,
    "lost": 0,
    "draw": 3
}
duels = {
    'AX': "draw", 
    'AY': "won", 
    'AZ': "lost", 
    
    'BX': "lost", 
    'BY': "draw", 
    'BZ': "won", 

    'CX': "won", 
    'CY': "lost", 
    'CZ': "draw", 
}

score = 0
for x in f:
    (opponent, me) = x.strip().split()
    score+= points[me]
    score+= resultPoints[duels[opponent+me]]

f.close()
print(score)

# --- Part 2 ---

# A Rock
# B Paper
# C Scissors

# X lose
# Y draw
# Z win

resultPoints = {
    "Z": 6,
    "X": 0,
    "Y": 3
}

duelsResult = {
    'AX': "C", 
    'AY': "A", 
    'AZ': "B", 
    
    'BX': "A", 
    'BY': "B", 
    'BZ': "C", 

    'CX': "B", 
    'CY': "C", 
    'CZ': "A", 
}

points = {
    'A': 1,
    'B': 2,
    'C': 3
}

f = open("inputs/input2.txt", "r")

score = 0
for x in f:
    (opponent, result) = x.strip().split()
    score+= resultPoints[result]
    score+= points[duelsResult[opponent+result]]

f.close()
print(score)
