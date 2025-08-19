alcool = int(0)
gasolina = int(0)
diesel = int(0)
combustivel = int(input())
while combustivel < 1 or combustivel > 4:
    combustivel = int(input())

if combustivel == 1:
    alcool = alcool + 1
if combustivel == 2:
    gasolina = gasolina + 1
if combustivel == 3:
    diesel = diesel + 1

while combustivel != 4:
    combustivel = int(input())
    if combustivel == 1:
        alcool = alcool + 1
    if combustivel == 2:
        gasolina = gasolina + 1
    if combustivel == 3:
        diesel = diesel + 1

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")