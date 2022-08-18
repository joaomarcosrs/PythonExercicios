num = int(input('Digite um número: '))
print('A tabuada de {} é'. format(num))


### SOMA ###
print('\nSoma')
for contador in range(1,11):
    soma = num + contador
    print('{:<} + {:2} = {}'. format(num, contador, soma))

### SUBTRAÇÃO ###
print('\nSubtração')
for contador in range(1,11):
    sub = num - contador
    print('{:<} - {:2} = {}'. format(num, contador, sub))

### MULTIPLICAÇÃO ###
print('\nMultiplicação')
for contador in range(1,11):
    mult = num * contador
    print('{:<} * {:2} = {}'. format(num, contador, mult))

### Divisão ###
print('\nDivisão')
for contador in range(1,11):
    div = num / contador
    print('{:<} / {:2} = {:.2f}'. format(num, contador, div))