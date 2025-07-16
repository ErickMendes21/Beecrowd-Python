C = int(input())
T = str(input())
S = 0

matriz = [[0 for _ in range(12)] for _ in range(12)]
for i in range(0, 12):
    for j in range(0, 12):
        matriz[i][j] = float(input())
        if j == C:
            S = S + matriz[i][j]
if T == 'S':
    print(S)
else:
    media = S / 12
    print(f"{media:.1f}")