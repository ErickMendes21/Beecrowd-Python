N = int(input())
cont = 0
for i in range(N):
    X = int(input())
    for k in range(1, X+1):
        if X % k == 0:
            cont += 1
    if cont == 2:     
        print(f"{X} eh primo")    
    else:
        print(f"{X} nao eh primo")
    cont = 0
