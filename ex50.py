soma = 0
for i in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma = numero + soma
print(f'\nA soma dos números pares é {soma}')
