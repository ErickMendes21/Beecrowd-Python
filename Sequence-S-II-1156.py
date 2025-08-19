S = 1 + 3/2 # -> 2.5
cont = 2
for i in range(5, 40, 2):
    cont = cont * 2
    S = S + i / cont

print(f"{S:.2f}")