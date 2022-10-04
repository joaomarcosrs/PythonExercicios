tpl_numero = ()
tpl_numero_par = ()
c = 0

for i in range(0, 4):
    numero = (int(input('Digite um número: ')),)
    tpl_numero = tpl_numero + numero

    if tpl_numero[i] % 2 == 0:
        tpl_numero_par = tpl_numero_par + numero
        c = c + 1

if tpl_numero.count(9) == 1:
    plu_sing = 'vez'
else:
    plu_sing = 'vezes'
print(f'\nVocê digitou os valores {tpl_numero}')
print(f'O valor 9 apareceu {tpl_numero.count(9)} {plu_sing}')

if 3 not in tpl_numero:
    print(f'O número 3 não aparece na sequência digitada')
else:
    print(f'O valor 3 apareceu na {tpl_numero.index(3)}ª posição')

if c == 0:
    print(f'Não foi digitado nenhum valor par')
elif c == 1:
    print(f'Foi digitado apenas um número par: {tpl_numero[i]}')
else:
    print(f'Os valores pares digitados foram ', end='')
    for i in range(len(tpl_numero_par)):
        print(f'{tpl_numero_par[i]}', end=' ')
