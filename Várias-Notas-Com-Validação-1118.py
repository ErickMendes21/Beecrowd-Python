nota1 = float(input())

while nota1 < 0 or nota1 > 10:
    print("nota invalida")
    nota1 = float(input())

nota2 = float(input())

while nota2 < 0 or nota2 > 10:
    print("nota invalida")
    nota2 = float(input())

media = float((nota1 + nota2) / 2)
print(f"media = {media:.2f}")
print("novo calculo (1-sim 2-nao)")
X = int(input())
while X < 1 or X > 2:
    print("novo calculo (1-sim 2-nao)")
    X = int(input())

while X == 1:
    nota1 = float(input())

    while nota1 < 0 or nota1 > 10:
        print("nota invalida")
        nota1 = float(input())

    nota2 = float(input())

    while nota2 < 0 or nota2 > 10:
        print("nota invalida")
        nota2 = float(input())

    media = float((nota1 + nota2) / 2)
    print(f"media = {media:.2f}")
    print("novo calculo (1-sim 2-nao)")
    X = int(input())
    while X < 1 or X > 2:
        print("novo calculo (1-sim 2-nao)")
        X = int(input())