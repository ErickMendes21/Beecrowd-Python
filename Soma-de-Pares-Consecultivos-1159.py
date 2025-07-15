N = int(input())
S = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X % 2 == 0:
        X = X + 1
    j = 0
    while j != Y:
        S = S + X
        j += 1
        X += 2
    print(S)
    S = 0