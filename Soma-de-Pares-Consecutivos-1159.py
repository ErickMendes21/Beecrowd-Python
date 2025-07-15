X = int(input())

while X != 0:
    if X % 2 != 0:
        X += 1
    j = 0
    S = 0
    while j != 5:
        if X % 2 == 0:
            S += X
        X += 2
        j += 1
    print(S)
    X = int(input())