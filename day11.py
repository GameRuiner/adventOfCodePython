import math

# f = open("inputs/input11test.txt", "r")
f = open("inputs/input11.txt", "r")
monkeys = []
monkey = {}
div_mult = 1
for line in f:
    if line == "\n":
        monkey['inspected'] = 0
        monkeys.append(monkey)
        monkey = {}
        continue
    splitted = line.split()
    if splitted[0] == 'Starting':
        items = list(int(c.replace(',', '')) for c in splitted[2:])
        monkey['items'] = items
    if splitted[0] == 'Operation:':
        monkey['operation'] = ' '.join(splitted[3:])
    if splitted[0] == 'Test:':
        div = int(splitted[-1])
        monkey['divisible'] = div
        div_mult *= div
    if splitted[1] == 'true:':
        monkey['true_pass'] = int(splitted[-1])
    if splitted[1] == 'false:':
        monkey['false_pass'] = int(splitted[-1])

monkey['inspected'] = 0
monkeys.append(monkey)

# --- Part 1, 2 ---

# for i in range(20):
for i in range(10000):
    for monkey in monkeys:
        monkey['inspected'] += len(monkey['items'])
        for item in monkey['items']:
            old = item
            # newWorry = math.floor(eval(monkey['operation']) / 3)
            newWorry = math.floor(eval(monkey['operation'])) % div_mult
            throwTo = monkey['true_pass'] if newWorry % monkey['divisible'] == 0 else monkey['false_pass']
            monkeys[throwTo]['items'].append(newWorry)
        monkey['items'] = []

result = list(m['inspected'] for m in monkeys)
result.sort(reverse=True)
print(result[0] * result[1])

f.close()