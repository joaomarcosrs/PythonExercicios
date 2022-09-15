numero = 0
i = 0
soma = 0
while numero != 999:
  numero = int(input(f'\nDigite um número.'
                     f'\nCaso queira encerrar o programa digite {"999"}\n'))
  if numero != 999:
    soma = numero + soma
    i = i + 1

print(f'\nForam digitados \033[33m{i}\033[0m números inteiros')
print(f'A soma de todos os valores digitados é igual a \033[33m{soma}\033[0m')
print('\n\033[32mFIM\033[0m')