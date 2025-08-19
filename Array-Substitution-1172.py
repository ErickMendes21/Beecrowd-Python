X = []
for j, i in enumerate(X):
    valor = int(input())
    if valor <= 0:
        valor = 1
    X.append(valor)
    print(f"X[{j}] = X[{i}]")
