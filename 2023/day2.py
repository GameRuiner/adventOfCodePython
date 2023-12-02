import numpy as np

f = open("inputs/input2.txt", "r")

# Part one 
conf = {
  'red': 12,
  'green': 13,
  'blue': 14
}

ids = []
for game in f:
  sem_pos = game.find(':')
  gameID = int(game[5:sem_pos])
  sets = game[sem_pos+2:]
  game_is_possible = True
  for s in sets.split(';'):
    for balls in s.split(','):
      count, color = balls.split()
      if int(count) > conf[color]:
        game_is_possible = False
        break
    if not game_is_possible:
      break
  if game_is_possible:
    ids.append(gameID)
print(sum(ids))


# Part two 
powers = []
for game in f:
  sem_pos = game.find(':')
  sets = game[sem_pos+2:]
  balls_needed = {
    'red': 0,
    'green': 0,
    'blue': 0
  }
  for s in sets.split(';'):
    for balls in s.split(','):
      count, color = balls.split()
      balls_needed[color] = max(int(count), balls_needed[color])
  powers.append(np.prod(list(balls_needed.values())))


f.close()
print(sum(powers))