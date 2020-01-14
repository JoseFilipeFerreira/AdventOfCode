import itertools
total = 0
f = open("input.txt", 'r')
opcodesFixed = list(map(int, f.readline().split(',')))

result = 0
comb = list(itertools.product(list(range(1, 129)), list(range(1, 129))))
noun, verb = comb.pop()
while (result != 19690720 and comb):
    opcodes = opcodesFixed.copy()

    opcodes[1] = noun
    opcodes[2] = verb

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
    result = opcodes[0]

    print(result, noun, verb, 100 * noun + verb)

    noun, verb = comb.pop()
