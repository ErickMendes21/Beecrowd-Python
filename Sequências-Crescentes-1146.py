X = int(input())
while X != 0:
    for i in range(1, X+1):
        if i == X:
            print(i, end='')
            print("")
        else:
            print(i, end=' ')
    X = int(input())