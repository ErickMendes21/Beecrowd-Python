N = int(input())
num = []
cont = int(0)
for i in range(N):
    val = int(input())
    num.append(val)
    if i >= 1:
        if num[i] != num[i - 1]:
            cont += 1
            
cont += 1

print(cont)