with open("input.txt", 'r') as file:
    file = file.read()
    file = file.split("\n")
    file = file[:-1]

    n2 = 0
    n3 = 0

    for word in file:
        dic = {}
        for car in word:
            if car not in dic:
                dic[car]= 1
            else:
                dic[car] += 1
        for car in dic.keys():
            if dic[car] == 2: 
                n2 += 1
                break
        for car in dic.keys():
            if dic[car] == 3:
                n3 += 1
                break
    print("cheksum:")
    print(n2*n3)


    while(len(file) > 2):
        for word1 in file:

            remove = True

            for word2 in file:
                if word1 is not word2:
                    diff = 0
                    for pos in range(len(word1)):
                        if word1[pos] != word2[pos]:
                            diff +=1
                                       

                    if  diff == 1 :
                        remove = False

            if(remove):
                file.remove(word1)
    print("results:")
    print('\n'.join(file))
