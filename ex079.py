lst_numero = list()

while True:
    numero = int(input('Digite um valor: '))
    if numero not in lst_numero:
        lst_numero.append(numero)
        print('Valor adcionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        keep_loop = str(input('Quer continuar? [S/N] ')).strip().upper()[:1]
        if keep_loop not in 'SN':
            print('Comando Inválido! Digite (S) SIM e (N) NÃO')
        else:
            break
    if keep_loop in 'N':
        break
print(f'{"-=-"*15}')
print(f'Você digitou  os valores {sorted(lst_numero)}')
