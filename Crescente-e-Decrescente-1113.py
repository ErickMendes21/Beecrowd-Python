while True:
    X, Y = map(int, input().split())
    if X == Y:
        break
    if X > Y:
        print("Decrescente")
    else:
        if X < Y:
            print("Crescente")