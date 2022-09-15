from numpy import mean

lst_numero = []
lst_numero_str = []
cont = 'S'
erro = 'S'
while cont != 'N':
    if erro == 'S':
        numero = int(input('Digite um número: '))
        lst_numero.append(numero)
        lst_numero_str.append(str(numero))

    cont = str(input('Você deseja continuar [S/N]?\n')).strip().upper()
    cont = cont[:1]
    if cont != 'S' and cont != 'N':
        print(f'Digite [S] se deseja continuar ou [N] caso deseje parar')
        erro = cont
    elif cont == 'S':
        erro = 'S'

print(f'\nOs valores digitados foram:\n{" - ".join(lst_numero_strs)}\n'
      f'\nA média dos valores é: \033[33m{mean(lst_numero)}\033[0m\n'
      f'O maior valor foi: \033[33m{max(lst_numero)}\033[0m\n'
      f'O maior valor foi: \033[33m{min(lst_numero)}\033[0m\n')
