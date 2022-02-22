with open('input', 'r') as file:
    depths=[]
    for line in file:
        depths.append(int(line))

    n_increase = 0
    previous = 0
    for d in depths:
        if previous < d:
            n_increase += 1

        previous = d

    print("1 star:", n_increase - 1)

    n_increase = 0
    previous = 0

    for i in range(0, len(depths) - 2):
        d = depths[i] + depths[i+1] + depths[i+2]
        if previous < d:
            n_increase += 1

        previous = d

    print("2 star:", n_increase - 1)
