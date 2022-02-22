with open('input', 'r') as file:
    n1 = [0] * 12

    values=[]
    for line in file:
        values.append(line.strip())

    total = len(values)
    for line in values:
        for i, n in enumerate(line):
            n1[i] += int(n)


    n1.reverse()
    gamma = 0
    epsilon = 0
    for i, n in enumerate(n1):
        if n > total / 2:
            gamma += 2**i
        else:
            epsilon += 2**i

    print("gamma:", gamma)
    print("epsilon:", epsilon)
    print("star 1:", gamma * epsilon)

    n1.reverse()
    oxygen = values.copy()
    carbon = values.copy()

    def get_common(v, pos):
        local_n = 0
        for l in v:
            local_n += int(l[pos])
        return 1 if local_n > len(v) / 2 else 0


    for i in range(0,12):
        if len(oxygen) > 1:
            n_oxygen = list(filter(lambda x: int(x[i]) != get_common(oxygen, i), oxygen))
            if len(n_oxygen) != 0:
                oxygen = n_oxygen
        if len(carbon) > 1:
            n_carbon = list(filter(lambda x: int(x[i]) == get_common(carbon, i), carbon))
            if len(n_carbon) != 0:
                carbon = n_carbon

    print("oxygen:", oxygen)
    print("carbon:", carbon)
    oxygen = int(oxygen[0], 2)
    carbon = int(carbon[0], 2)
    print("oxygen:", oxygen)
    print("carbon:", carbon)
    print("star 2:", oxygen * carbon)
