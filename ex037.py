numero = int(input('Digite um núemro: '))
print('''Digite o número da opção que você deseja

[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal
''')
op = int(input('Digite a opção de conversão: '))
print('\n')

if op == 1:
  print('O número convertido para Binário é: {}'.format(format(numero, 'b')))
elif op == 2:
  print('O número convertido para Octal é: {}'.format(format(numero, 'o')))
elif op == 3:
  numero = format(numero, 'x')
  numero = str(numero)
  print('O número convertido para Hexadecimal é: {}'.format(numero.upper()))
else:
  print('Opção inválida! Tente novamente.')


#Nesse código pode-se usar os métodos bin(), oct() e hex(), aconpnhados do fatiamento de strings [2:]
# para apresentar os números sem as duas letras iniciais que indicam o tipo de conversão.