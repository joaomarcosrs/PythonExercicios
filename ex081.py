lst_numero = list()

while True:
    numero = int(input('Digite um número: '))
    lst_numero.append(numero)
    while True:
        keep_loop = str(input('Você deseja continuar? [S/N] ')).strip().upper()[:1]
        if keep_loop not in 'SN':
            print('Respotas Inválida! Digite [S] SIM e [N] NÃO!')
        else:
            break
    if keep_loop in 'N':
        break
print(f'{"-=-"*20}')
print(f'Você digitou {len(lst_numero)} elementos.')
print(f'Os valores em ordem decrescente são {sorted(lst_numero, reverse=True)}')
if 5 in lst_numero:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')

