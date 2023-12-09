import re

f = open("inputs/input3.txt", "r")

# Part one 
gears = {}
def check_pos(x, y, schematic, number):
  if x < 0 or y < 0 or y >= len(schematic) or x >= len(schematic[y]):
    return False
  if not schematic[y][x].isnumeric() and schematic[y][x] != '.':
    if (schematic[y][x] == '*'):
      if (x, y) in gears:
        gears[(x, y)].append(number)
      else:
        gears[(x, y)] = [number]
    return True
  return False

def check_number(start, end, schematic, row_number, number):
  pos_to_check = [
    (start - 1, row_number), 
    *[(x, row_number - 1) for x in range(start - 1, end + 1)],
    (end, row_number), 
    *[(x, row_number + 1) for x in range(start - 1, end + 1)]
    ]
  return any(check_pos(x, y, schematic, number) for x, y in pos_to_check)

schematic = [line[:-1] for line in f]
numbers = []
for row_number, line in enumerate(schematic):
  line_numbers = [int(m.group(0)) 
         for m in re.finditer('\d+', line) 
         if check_number(m.start(), m.end(), schematic, row_number, int(m.group(0)))
  ]
  numbers.append(sum(line_numbers))

print(sum(numbers))

# Part two
print(sum([numbers[0]*numbers[1] for numbers in gears.values() if len(numbers) == 2]))

f.close()
