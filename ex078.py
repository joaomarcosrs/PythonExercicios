lst_numero = list()

for i in range(0, 5):
    numero = int(input(f'Digite um valor para a posição {i}: '))
    lst_numero.append(numero)
print(f'{"-=-"*17}')

print(f'Você digitou os valores {lst_numero}')
print(f'O maior valor digitado foi {max(lst_numero)} ', end='')
if lst_numero.count(max(lst_numero)) != 1:
    print(f'nas posições ', end='')
    for i in range(len(lst_numero)):
        if lst_numero[i] == max(lst_numero):
            print(f'{i}...', end='')
else:
    print(f'na posição {lst_numero.index((max(lst_numero)))}')

print(f'\nO menor valor digitado foi {min(lst_numero)} ', end='')
if lst_numero.count(min(lst_numero)) != 1:
    print(f'nas posições ', end='')
    for i in range(len(lst_numero)):
        if lst_numero[i] == min(lst_numero):
            print(f'{i}...', end='')
else:
    print(f'na posição {lst_numero.index((min(lst_numero)))}')
