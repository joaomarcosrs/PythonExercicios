numero = int(input('Digite um número: '))
divisivel = []
for i in range(1, numero + 1):
    if numero % i == 0 and numero % numero == 0:
        divisivel.append(i)
        print(f'\033[33m{i}\033[m', end=' ')
    else:
        print(f'\033[31m{i}\033[m', end=' ')

print(f'\n\nO número {numero} foi divisível {len(divisivel)} vezes')
if len(divisivel) > 2:
    print(f'Não é um número primo')
else:
    print(f'É um número primo')