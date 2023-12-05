import numpy as np

f = open("inputs/input4.txt", "r")

# Part one 

# points = []
# for card in f:
#   sem_pos = card.find(':')
#   gameID = int(card[5:sem_pos])
#   lists = card[sem_pos+2:]
#   winning, scratched = [l.split() for l in lists.split('|')]
#   numbers = 0
#   for n in scratched:
#     if n in winning:
#       numbers+=1
#   if numbers:
#     points.append(2**(numbers-1))
# print(sum(points))


instances = {}
for card in f:
  sem_pos = card.find(':')
  gameID = int(card[5:sem_pos])
  if gameID in instances:
    copies = instances[gameID]
  else:
    copies = instances[gameID] = 1
  lists = card[sem_pos+2:]
  winning, scratched = [l.split() for l in lists.split('|')]
  numbers = 0
  for n in scratched:
    if n in winning:
      numbers+=1
  for i in range(1, numbers + 1):
    gameNumber = gameID + i
    if gameNumber in instances:
      instances[gameNumber] += copies
    else:
      instances[gameNumber] = copies + 1

print(sum(instances.values()))
# < 1153054879054342523 

f.close()