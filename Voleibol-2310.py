N = int(input())
somaS = 0
somaS1 = 0
somaB = 0
somaB1 = 0
somaA = 0
somaA1 = 0
for i in range(N):
    nome = input()
    S, B, A = map(int, input().split())
    S1, B1, A1 = map(int, input().split())
    somaS = somaS + S
    somaS1 = somaS1 + S1
    somaB = somaB + B
    somaB1 = somaB1 + B1
    somaA = somaA + A
    somaA1 = somaA1 + A1

tS = somaS1 / somaS * 100
tB = somaB1 / somaB * 100
tA = somaA1 / somaA * 100

print(f"Pontos de Saque: {tS:.2f} %.")
print(f"Pontos de Bloqueio: {tB:.2f} %.")
print(f"Pontos de Ataque: {tA:.2f} %.")