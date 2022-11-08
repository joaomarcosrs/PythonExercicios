lst_parenteses = list()

expressao = str(input('Digite a expressão: ')).strip()
for caractere in expressao:
  if caractere == '(':
    lst_parenteses.append('(')
  elif caractere == ')':
    if len(lst_parenteses) > 0:
      lst_parenteses.pop()
    else:
      lst_parenteses.append(')')
      break

if len(lst_parenteses) == 0:
  print('Sua expressão está válida!')
else:
  print('Sua expressão não é válida!')
