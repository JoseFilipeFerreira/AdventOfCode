import math
total = 0
f = open("input.txt", 'r')
mass = list(map(int, f.readlines()))
for m in mass:
    f = math.floor(m/3) - 2
    if (f > 0):
        total += f
        mass.append(f)
print(total)
