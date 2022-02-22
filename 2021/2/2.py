with open('input', 'r') as file:
    aim = 0
    horizontal = 0
    depth = 0
    simple_depth=0

    for line in file:
        [com, n] = line.split(' ')
        n = int(n)
        if com == 'forward':
            horizontal += n
            depth += aim * n
        elif com == 'down':
            aim += n
            simple_depth += n
        elif com == 'up':
            aim -= n
            simple_depth -= n

    print("1 star:", horizontal * simple_depth)
    print("2 star:", horizontal * depth)
