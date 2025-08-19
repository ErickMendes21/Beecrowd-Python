valores = list(map(int, input().split()))

A = valores[0]
N = None
for i in range(1, len(valores)):
    if valores[i] > 0:
        N = valores[i]
        break

S = 0
for i in range(N):
    S += A + i

print(S)