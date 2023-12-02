import re

f = open("inputs/input1.txt", "r")

# Part one 
calibration_values = []
for x in f:
  numbers = []
  for ch in x:
    if ch.isnumeric():
      numbers.append(ch)
  calibration_values.append(int(numbers[0] + numbers[-1]))

# Part two
text_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
calibration_values = []
for x in f:
  numbers = []
  for index, ch in enumerate(x):
    if ch.isnumeric():
      numbers.append((ch, index))
  for (number_index, text_number) in enumerate(text_numbers):
    indexes = [m.start() for m in re.finditer(text_number, x)]
    for index in indexes:
      numbers.append((str(number_index+1), index))
  numbers.sort(key=lambda n: n[1])
  # print(numbers)
  calibration_values.append(int(numbers[0][0] + numbers[-1][0]))


f.close()
print(sum(calibration_values))