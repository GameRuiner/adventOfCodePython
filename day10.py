# f = open("inputs/input10test.txt", "r")
f = open("inputs/input10.txt", "r")

register = 1
cycle = 1
queue = []

def do_job(queue, register):
    (cycles_left, num) = queue[0]
    cycles_left -= 1
    if cycles_left == 0:
        register += num
        queue.pop(0)
    else:
        queue[0] = [cycles_left, num]
    return register

# --- Part 1 ---

# cycles_to_check = [20, 60, 100, 140, 180, 220]
# result = 0

# for instruction in f:
#     if cycle == cycles_to_check[0]:
#         result += cycles_to_check[0] * register
#         cycles_to_check.pop(0)
#     splitted = instruction.split()
#     if splitted[0] != 'noop':
#         queue.append([2, int(splitted[1])])
#     else:
#         queue.append([1, 0])
#     if len(queue) > 0:
#         register = do_job(queue, register)
#     cycle += 1

# while len(queue) > 0:
#     if cycle == cycles_to_check[0]:
#         result += cycles_to_check[0] * register
#         cycles_to_check.pop(0)
#         if len(cycles_to_check) == 0:
#             break
#     register = do_job(queue, register)
#     cycle += 1

# --- Part 2 ---

line = ['-'] * 40
result = []
for _ in range(6):
    result.append(line.copy())


for instruction in f:
    splitted = instruction.split()
    result[(cycle-1)//40][(cycle-1)%40] = '#' if abs(((cycle - 1) %40) - register) < 2 else '.'
    if splitted[0] != 'noop':
        queue.append([2, int(splitted[1])])
    else:
        queue.append([1, 0])
    if len(queue) > 0:
        register = do_job(queue, register)
    cycle += 1

while len(queue) > 0 :
    result[(cycle-1)//40][(cycle-1)%40] = '#' if abs(((cycle - 1) %40) - register) < 2 else '.'
    register = do_job(queue, register)
    cycle += 1

f.close()

for line in result:
    print(''.join(line))
