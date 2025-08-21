C = int(input())
S = 0

for i in range(C):
    N = int(input())
    for j in range(N):
        if j % 2 == 0:
            S = S + 1
        else:
            S = S - 1
    print(S)
    S = 0