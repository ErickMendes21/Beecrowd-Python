O = str(input())
S = 0
cont = 0
M = [[0 for _ in range(12)] for _ in range(12)]
for i in range(0, 12):
    for j in range(0, 12):
        M[i][j] = float(input())
        if i != j and j > i:
            S = S + M[i][j]
            cont += 1

if O == 'S':
    print(S)
else:
    R = S/cont
    print(f"{R:.1f}")