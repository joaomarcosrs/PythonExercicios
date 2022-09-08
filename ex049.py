numero = int(input('Digite um número: '))
print(f'A tabuada de {numero} é')


### SOMA ###
print('\nSoma')
for i in range(0, 11):
    print(f'{i:>2} + {numero} = {i + numero:>2}')

### SUBTRAÇÃO ###
print('\nSubtração')
for i in range(0, 11):
    print(f'{i:>2} - {numero} = {i - numero:>2}')

### MULTIPLICAÇÃO ###
print('\nMultiplicação')
for i in range(0, 11):
    print(f'{i:>2} * {numero} = {i * numero:>2}')

### Divisão ###
print('\nDivisão')
for i in range(0, 11):
    print(f'{i:>2} / {numero} = {i / numero:>2}')
