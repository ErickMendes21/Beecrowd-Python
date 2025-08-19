O = str(input())
M = [[0 for _ in range(12)] for _ in range(12)]
S = 0
cont = 0
for i in range(0, 12):
    for j in range(0, 12):
        M[i][j] = float(input())

for i in range(0, 12):
    for j in range(0, 11 - i):
        S = S + M[i][j]
        cont = cont + 1


if O == 'S':
    print(S)
else:O = str(input())
M = [[0 for _ in range(12)] for _ in range(12)]
S = 0
cont = 0
for i in range(0, 12):
    for j in range(0, 12):
        M[i][j] = float(input())

for i in range(0, 12):
    for j in range(0, 11 - i):
        S = S + M[i][j]
        cont = cont + 1


if O == 'S':
    print(S)
else:
    R = S / cont
    print(f"{R:.1f}")
    R = S / cont
    print(f"{R:.1f}")