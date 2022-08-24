num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

maior = num1 > num2
menor = num1 < num2
print('\n')

if maior:
  print('O primeiro valor é maior!')
elif menor:
  print('O segundo valor é maior!')
else:
  print('Não existe valor maior, os dois valores são iguais!')