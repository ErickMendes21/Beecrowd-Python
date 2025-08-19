X = int(input())
Y = int(input())
S = int(0)
if Y > X:
    for i in range(X, Y + 1):
        if i % 13 != 0:
            S = S + i
else:
    for i in range(Y, X + 1):
        if i % 13 != 0:
            S = S + i


print(S)