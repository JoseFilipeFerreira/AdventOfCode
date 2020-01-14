
with open("input.txt", 'r') as file:
    file = file.read()
    file = file.split("\n")
    file = file[:-1]
    file = [int(i) for i in file]
    frequency = 0
    prev = set()
    prev.add(0)
    stop = True
    while (stop):
        for n in file:
            frequency += n
            if frequency not in prev:
                prev.add(frequency)
            else:
                stop=False
                break
        print(len(prev))
    print("repeated frequency:")
    print(frequency)
