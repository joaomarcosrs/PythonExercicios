numero = int(input('Digite um número inteiro: '))
i = 0
c = 1
soma = 0

while soma <= numero:
    soma = i + c
    n_soma = soma + c
    c = n_soma
    print(f'{soma}')
# 1 = 0 + 1
# 2 = 1 + 1
# 3 = 2 + 1
# 5 = 3 + 2

