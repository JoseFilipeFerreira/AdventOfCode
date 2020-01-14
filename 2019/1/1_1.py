import math
total = 0
f = open("input.txt", 'r')
for l in f:
    v = int(l)
    total += math.floor(v/3) - 2
print(total)
