tpl_numero = ()

for i in range(0, 4):
  numero = (int(input('Digite um número: ')), )
  tpl_numero = tpl_numero + numero

if tpl_numero.count(9) == 1:
    plu_sing = 'vez'
else:
    plu_sing = 'vezes'
print(f'\nVocê digitou os valores {tpl_numero}')
print(f'O valor 9 apareceu {tpl_numero.count(9)} {plu_sing}')
print(f'O valor 3 apareceu na {tpl_numero.index(3)}ª posição')

c = 0
for i in range(len(tpl_numero)):
  if tpl_numero[i] % 2 == 0:
    c = c + 1
  # else:
  #   c = 0
if c == 0:
  print(f'Não foi digitado nenhum valor par')
else:
  if c == 1:
    print(f'Foi digitado apenas um número par')
  else:
    print(f'Os valores pares digitados foram {c}')