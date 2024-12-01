import math 

f = open("inputs/input1.txt", "r")

# Part one
left = []
right = [] 
for line in f:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))
left = sorted(left)
right = sorted(right)
res = 0
for l, r in zip(left, right):
    res += abs(l - r)
print(res)
# Part two
res2 = 0
for n in left:
    res2 += n * right.count(n)
print(res2)

f.close()