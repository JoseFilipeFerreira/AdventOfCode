total = 0
f = open("input.txt", 'r')
opcodes = list(map(int, f.readline().split(',')))
opcodes[1] = 12
opcodes[2] = 2

ip = 0
while(opcodes[ip] != 99):
    v1   = opcodes[ opcodes[ip + 1]] 
    v2   = opcodes[ opcodes[ip + 2]]
    pout = opcodes[ip + 3]
    if (opcodes[ip] == 1):
        opcodes[pout] = v1 + v2
    if (opcodes[ip] == 2):
        opcodes[pout] = v1 * v2

    ip += 4
print(opcodes[0])
