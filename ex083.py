lst_parenteses = list()

expressao = str(input('Digite a expressão: ')).strip()
for caractere in range(len(expressao)):
  lst_parenteses.append(expressao[caractere])

if lst_parenteses.count('(') == lst_parenteses.count(')'):
  print('Sua expressão está válida!')
else:
  print('Sua expressão não é válida!')
