
soma = 0
for i in range(1, 501, 2):
     if i % 3 == 0:
         soma = soma + i
         contador = contador + 1
print(f'A soma de todos os {contador} valores é {soma}')
