T = int(input())
res = list(map(int, input().split()))
aux = 0
for i in res:
    if i == T:
        aux += 1

print(aux)